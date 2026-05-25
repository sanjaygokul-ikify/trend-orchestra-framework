from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    name: str
    tasks: List[str]

    def start(self):
        print(f"Agent {self.name} started")

    def stop(self):
        print(f"Agent {self.name} stopped")

@dataclass
class Task:
    name: str
    agent: Agent

    def execute(self):
        print(f"Task {self.name} executed")
        return Result(self.name, self.agent.name)

@dataclass
class Result:
    task_name: str
    agent_name: str

class Notification:
    def __init__(self, message: str):
        self.message = message

    def notify(self):
        print(f"Notification: {self.message}")