from dotenv import load_dotenv
from src.formulate_sentence import formulate_sentence
from src.login import Login
from src.setup_selenium import setup_selenium
from src.tweet import Tweet
from src.utils import get_resource_path
from src.config import DEBUG
import datetime
import logging


def main(logger: logging.Logger, now: datetime.date):
    
    logger.info(f"Starting Routine: {now.isoformat()}")

    # adding error tolerance of 3
    for _ in range(3):
        
        try:
            generated_text = formulate_sentence()

            wait = setup_selenium()

            login = Login(wait=wait)

            login.start()

            tweet = Tweet(wait=wait)

            tweet.start(text=generated_text)
            
            # if complete without errors break the loop
            break

        except Exception as e:
            logger.warning(f"Routine raised error: {now.isoformat()}")
            # if error is raised just skip
            continue


    logger.info(f"Finishing Routine: {now.isoformat()}")


if __name__ == '__main__':
    if DEBUG:
        load_dotenv(get_resource_path(".env"))
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    now = datetime.datetime.now()

    main(logger=logger, now=now)