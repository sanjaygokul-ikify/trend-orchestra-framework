import unittest
from packages.core.engine import Engine
from packages.core.types import Agent, Task
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine(logger=logging.getLogger(__name__))
        orchestrator = Orchestrator(engine)
        agent = Agent(name='Test Agent', tasks=[])#
        task1 = Task(name='Task1', agent=agent)
        task2 = Task(name='Task2', agent=agent)
        engine.register_agent(agent)
        engine.dispatch_task(task1)
        engine.dispatch_task(task2)
        orchestrator.start()
        self.assertEqual(len(engine.results), 2)

if __name__ == '__main__':
    unittest.main()
