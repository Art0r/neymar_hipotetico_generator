import datetime
import logging
from dotenv import load_dotenv
from src.formulate_sentence import formulate_sentence
from src.login import Login
from src.setup_selenium import setup_selenium
from src.tweet import Tweet
import time

def main():

    target_schedule: dict[str, int] = {
        "hour": 19,
        "minute": 00
    }

    last_execution_date = None

    while True:

        logging.info("Starting Routine")
        
        now = datetime.datetime.now()
        target = datetime.datetime(
            year=now.year,
            day=now.day,
            month=now.month,
            second=now.second,
            hour=target_schedule["hour"],
            minute=target_schedule["minute"]
        )

        if now.date() != last_execution_date and now >= target:

            generated_text = formulate_sentence()

            wait = setup_selenium()

            login = Login(wait=wait)

            login.start()

            tweet = Tweet(wait=wait)

            tweet.start(text=generated_text)

        last_execution_date = now.date()

        logging.info("Finishing Routine")

        time.sleep(5 * 60)


if __name__ == '__main__':
    load_dotenv()
    main()