from locust import HttpUser, between, task
class DemoUser(HttpUser):
    wait_time = between(1, 3)
    @task(3)
    def health(self):
        self.client.get("/health", name="/health")
    @task(1)
    def projects(self):
        self.client.get("/projects", name="/projects")
