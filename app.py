# import dependencies
import redis
import time
from flask import Flask

# create app instance with resources in current working directory
app = Flask(__name__)


# create a connection to the Redis server
cache = redis.Redis(host='redis', port=6379)


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
def hello():
    # increment page hit count in cache whenever this page is called 
    count = get_hit_count()
    # display page hit count
    return 'Hello World! I have been seen {} times.\n'.format(count)
