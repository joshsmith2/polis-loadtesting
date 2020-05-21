from locust import HttpLocust, TaskSet, task
import os

try:
    target = os.environ['LOCUST_TARGET']
except KeyError:
    print("You're missing the environment variable 'LOCUST_TARGET'; this "
          "should be set to the URL for the server to test")
    raise

