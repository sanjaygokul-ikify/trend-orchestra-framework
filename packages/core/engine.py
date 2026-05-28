from typing import List, Dict
from logging import Logger
from .types import Agent, Task, Result
from .exceptions import EngineException, AgentException, TaskException

class Engine:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.agents: List[Agent] = []
        self.tasks: List[Task] = []
        self.results: Dict[str, Result] = {}

    def register_agent(self, agent: Agent):
        self.agents.append(agent)
        self.logger.info(f"Agent {agent.name} registered")

    def dispatch_task(self, task: Task):
        self.tasks.append(task)
        self.logger.info(f"Task {task.name} dispatched")

    def execute_task(self, task: Task):
        try:
            result = task.execute()
            self.results[task.name] = result
            self.logger.info(f"Task {task.name} executed successfully")
        except Exception as e:
            self.logger.error(f"Task {task.name} execution failed: {e}")
            raise TaskException(f"Task {task.name} execution failed: {e}")

    def aggregate_results(self):
        aggregated_results: Dict[str, List[Result]] = {}
        for result in self.results.values():
            if result.task_name not in aggregated_results:
                aggregated_results[result.task_name] = []
            aggregated_results[result.task_name].append(result)
        return aggregated_results

    def run(self):
        for agent in self.agents:
            agent.start()
        for task in self.tasks:
            try:
                self.execute_task(task)
            except TaskException as e:
                self.logger.error(f"Task {task.name} execution failed: {e}")
            else:
                self.logger.info(f"Task {task.name} executed successfully")
        aggregated_results = self.aggregate_results()
        self.logger.info(f"Aggregated results: {aggregated_results}")

    def stop(self):
        for agent in self.agents:
            agent.stop()
        self.logger.info("Engine stopped")

    def __str__(self):
        return f"Engine(agents={self.agents}, tasks={self.tasks}, results={self.results})"
