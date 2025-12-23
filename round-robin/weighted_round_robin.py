import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class Server:
    def __init__(self, name, response_time, weight):
        self.name = name
        self.response_time = response_time
        self.weight = weight

    def handle_request(self, request_id):
        logging.info(f"{self.name} START handling request {request_id}")
        time.sleep(self.response_time)
        logging.info(f"{self.name} FINISHED request {request_id}")

class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = []
        for server in servers:
            self.servers.extend([server] * server.weight)

        self.index = 0

        logging.info (
            "Weighted server pool: " + ", ".join(s.name for s in self.servers)
        )

    def route(self, request_id):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)

        logging.info(
            f"LB routing request {request_id} -> {server.name}"
        )

        server.handle_request(request_id)
    
servers = [
    Server("Fast-Server", 0.2),
    Server("Medium-Server", 0.5),
    Server("Slow-Server", 1.2),
]

lb = RoundRobinLoadBalancer(servers)

for i in range(1, 12):
    lb.route(i)