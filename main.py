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

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    while True:

        now = datetime.datetime.now()
        now_isoformat = now.isoformat()
        
        if retrieve_log_and_verify(now):
            logger.info(f"Skipping: {now_isoformat}")
            timer()
            continue
        
        logger.info(f"Starting Routine: {now_isoformat}")

        # adding error tolerance of 3
        for i in range(3):
            
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
                logger.warning(f"Routine raised error: {now_isoformat}")
                # if error is raised just skip
                continue

        write_log()

        logger.info(f"Finishing Routine: {now_isoformat}")

        timer()


if __name__ == '__main__':
    load_dotenv(get_resource_path(".env"))
    main()