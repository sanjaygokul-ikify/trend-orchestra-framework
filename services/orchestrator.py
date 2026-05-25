from packages.core.types import Agent, Task
from packages.core.engine import Engine
from packages.utils.logging import logger

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        try:
            self.engine.run()
        except EngineException as e:
            logger.error(e)

    def stop(self):
        self.engine.stop()
