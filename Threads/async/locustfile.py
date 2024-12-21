from locust import HttpUser, task, between

class WebUser(HttpUser):
    wait_time = between(1,5)

    @task
    def load_homepage(self):
        self.client.get("/")
        