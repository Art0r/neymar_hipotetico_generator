from formulate_sentence import formulate_sentence
from login import Login
from setup_selenium import setup_selenium
from tweet import Tweet

def main():

    generated_text = formulate_sentence()

    wait = setup_selenium()

    login = Login(wait=wait)

    login.start()

    tweet = Tweet(wait=wait)

    tweet.start(text=generated_text)

if __name__ == '__main__':
    main()