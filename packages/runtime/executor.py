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

    def execute_task_with_timeout(self, task: Task, timeout: int):
        import signal
        import time
        def timeout_handler(signum, frame):
            raise TimeoutError()
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        try:
            result = self.engine.execute_task(task)
            signal.alarm(0)
            return result
        except TimeoutError:
            self.logger.error(f"Task {task.name} timed out")
            raise TaskException(f"Task {task.name} timed out")