from prefect import flow, get_run_logger
from messager.messager import send_message

@flow
def daily_message_flow(env: str = "production", config_path: str = "configs/production.json") -> None:
    logger = get_run_logger()
    logger.info(f"Starting daily flow in environment: {env} with config file: {config_path}")
    message = send_message(env, config_path)
    logger.info(f"Message sent: {message}")

if __name__ == "__main__":
    daily_message_flow()
