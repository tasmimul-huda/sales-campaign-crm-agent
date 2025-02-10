import schedule
import time

import logging
logger = logging.getLogger(__name__)


class TaskScheduler:
    def __init__(self):
        self.jobs = []

    def add_agent_task(self, agent, interval: str):
        """Add a task to the scheduler.
        
        Args:
            agent: The agent instance with an `execute_task` method.
            interval: A string representing the schedule interval (e.g., '15 minutes').
        """
        job = schedule.every().__getattribute__(interval).do(agent.execute_task)
        self.jobs.append(job)
        logger.info(f"Scheduled {agent.__class__.__name__} to run every {interval}")

    def start(self):
        """Start the scheduler and keep it running."""
        logger.info("Starting scheduler...")
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            self.stop()

    def stop(self):
        """Stop all scheduled jobs."""
        for job in self.jobs:
            schedule.cancel_job(job)
        logger.info("All scheduled jobs stopped.")