from locust import HttpLocust, TaskSet, task, between
import os

try:
    target = os.environ['LOCUST_TARGET']
except KeyError:
    print("You're missing the environment variable 'LOCUST_TARGET'; this "
          "should be set to the URL for the server to test")
    raise


class VoterBehavior(TaskSet):
    def on_start(self):
        """ Called before any task is executed """

    @task(1)
    def open_survey(self):
        self.client.get('/')

class Voter(HttpLocust):
    task_set = VoterBehavior
    wait_time = between(3, 9)
