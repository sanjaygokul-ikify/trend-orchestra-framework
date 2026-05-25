from typing import List
from . import Executor
from ..core.engine import Engine
from ..core.types import Agent, Task, Result
from ..core.exceptions import EngineException, TaskException
from logging import Logger

class Executor:
    def __init__(self, engine: Engine, logger: Logger):
        self.engine = engine
        self.logger = logger

    def execute(self, task: Task):
        try:
            result = self.engine.execute_task(task)
            self.logger.info(f"Task {task.name} executed successfully")
            return result
        except TaskException as e:
            self.logger.error(f"Task {task.name} execution failed: {e}")
            raise

    def run(self, tasks: List[Task]):
        for task in tasks:
            self.execute(task)
        self.logger.info("Executor finished")

    def stop(self):
        self.engine.stop()
        self.logger.info("Executor stopped")