import unittest
from packages.core.engine import Engine
from packages.core.types import Agent, Task

class TestRuntime(unittest.TestCase):
    def test_engine(self):
        engine = Engine(logger=logging.getLogger(__name__))
        agent = Agent(name='Test Agent', tasks=[])
        engine.register_agent(agent)
        self.assertIn(agent, engine.agents)

    def test_task_execution(self):
        engine = Engine(logger=logging.getLogger(__name__))
        agent = Agent(name='Test Agent', tasks=[])
        task = Task(name='Test Task', agent=agent)
        engine.dispatch_task(task)
        engine.execute_task(task)
        self.assertIn(task.name, engine.results)

if __name__ == '__main__':
    unittest.main()
