import unittest
from packages.core.types import Agent, Task, Result
from packages.core.engine import Engine

class TestCore(unittest.TestCase):
    def test_agent(self):
        agent = Agent(name='Test Agent', tasks=['Task1', 'Task2'])
        self.assertEqual(agent.name, 'Test Agent')
        self.assertEqual(agent.tasks, ['Task1', 'Task2'])

    def test_task(self):
        agent = Agent(name='Test Agent', tasks=[])
        task = Task(name='Test Task', agent=agent)
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.agent, agent)

    def test_result(self):
        result = Result(task_name='Test Task', agent_name='Test Agent')
        self.assertEqual(result.task_name, 'Test Task')
        self.assertEqual(result.agent_name, 'Test Agent')

if __name__ == '__main__':
    unittest.main()
