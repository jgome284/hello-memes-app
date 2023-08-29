# import dependencies
import json
import redis
import requests
import time
from flask import Flask, render_template

# create app instance with resources in current working directory
app = Flask(__name__)


# create a connection to the Redis server
cache = redis.Redis(host='redis', port=6379)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-1]
    subreddit = response["subreddit"]
    post = response["postLink"]
    return meme_large, subreddit, post

# increment the page hits counter that is stored in the redis cache
def get_hit_count():
    # specify the max number of connection attempts to the Redis server
    retries = 5
    while True:
        try:
            # increment the value of the page hits key by 1
            return cache.incr('hits')
        # in case of a connection error
        except redis.exceptions.ConnectionError as exc:
            # if there are no more retry attempts
            if retries == 0:
                # raise the ConnectionError exception
                raise exc
            # adjust remaining allowed connection attempts
            retries -= 1
            # wait before attempting a new connection
            time.sleep(0.5)

# set app route at '/'
@app.route('/')
# define view function for route
def show_memes():
    # get new meme url and it's subreddit
    meme_pic, subreddit, post = get_meme()
    # increment page hit count in cache whenever this page is called 
    count = get_hit_count()
    # display page hit count
    return render_template("memes.html", meme_pic=meme_pic, subreddit=subreddit, count=count, post=post)
