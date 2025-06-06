from prefect import flow, get_run_logger
from messager.src import send_message

@flow
def daily_message_flow(env: str = "production", cfg_file: str = "configs/prod.json") -> None:
    logger = get_run_logger()
    logger.info(f"Starting daily flow in environment: {env} with config file: {cfg_file}")
    message = send_message(env, cfg_file)
    logger.info(f"Message sent: {message}")

if __name__ == "__main__":
    daily_message_flow()
