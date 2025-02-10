import os
from dotenv import load_dotenv
from modules.agents.agent_a import AgentA
from modules.agents.agent_b import AgentB
from modules.agents.supervisor import Supervisor
from modules.utils.scheduler import TaskScheduler

from modules.utils.logger import setup_logging

setup_logging()

load_dotenv()

if __name__ == "__main__":
    # Initialize components
    agent_a = AgentA()
    agent_b = AgentB()
    supervisor = Supervisor()
    
    # Configure scheduler
    scheduler = TaskScheduler()
    scheduler.add_agent_task(agent_a, "15 minutes")  # Every 15 minutes
    scheduler.add_agent_task(agent_b, "1 hour")      # Every hour
    scheduler.add_agent_task(supervisor, "1 day")    # Daily
    
    # Start the system
    scheduler.start()