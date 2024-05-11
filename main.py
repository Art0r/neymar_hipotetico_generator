from dotenv import load_dotenv
from src.formulate_sentence import formulate_sentence
from src.login import Login
from src.setup_selenium import setup_selenium
from src.tweet import Tweet

def main():
    load_dotenv()

    generated_text = formulate_sentence()

    wait = setup_selenium()

    login = Login(wait=wait)

    login.start()

    tweet = Tweet(wait=wait)

    tweet.start(text=generated_text)

if __name__ == '__main__':
    main()