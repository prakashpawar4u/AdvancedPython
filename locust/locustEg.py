from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1,5)

    def index(self):
        self.client.get("/") ## Simulate a GET request to the homepage

    @task(2)  # The weight of the task (the number indicates the likelihood it will run)
    def about(self):
        self.client.get("/about")  # Simulate a GET request to the /about page



#locust -f .\locustEg.py