from agents.agent_marketing import marketing_agent
from agents.agent_data import data_retrieval_agent

class Supervisor:
    def __init__(self):
        self.agents = {
            "marketing": marketing_agent,
            "data": data_retrieval_agent
        }

    def route_task(self, prompt):
        if "Marketing" in prompt:
            return self.agents["marketing"](prompt, self)
        elif "Data" in prompt:
            return self.agents["data"](prompt)
        else:
            return "Agent not found"
