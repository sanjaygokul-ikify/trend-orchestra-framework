class EngineException(Exception):
    pass

class AgentException(EngineException):
    pass

class TaskException(EngineException):
    pass