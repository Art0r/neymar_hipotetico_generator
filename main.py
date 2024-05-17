import datetime
import logging
from dotenv import load_dotenv
from src.formulate_sentence import formulate_sentence
from src.login import Login
from src.setup_selenium import setup_selenium
from src.tweet import Tweet
import time
from src.utils import get_resource_path, write_log, retrieve_log_and_verify


def timer() -> None:
    time.sleep(5 * 60)


def main():

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    while True:

        now = datetime.datetime.now()
        
        if retrieve_log_and_verify(now):
            logger.info(f"Skipping: {now.isoformat()}")
            timer()
            continue
        
        logger.info(f"Starting Routine: {now.isoformat()}")

        generated_text = formulate_sentence()

        wait = setup_selenium()

        login = Login(wait=wait)

        login.start()

        tweet = Tweet(wait=wait)

        tweet.start(text=generated_text)

        write_log()

        logger.info(f"Finishing Routine: {now.isoformat()}")

        timer()


if __name__ == '__main__':
    load_dotenv(get_resource_path(".env"))
    main()