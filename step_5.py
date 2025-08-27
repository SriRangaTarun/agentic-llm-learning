import logging

logging.basicConfig(level=logging.INFO)
def agent_action(action):
    logging.info(f"Agent performs action: {action}")

agent_action("Query database")
