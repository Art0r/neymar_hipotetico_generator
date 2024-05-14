import os
import google.generativeai as genai

from src.utils import get_resource_path

def formulate_sentence() -> str:

    GEMINI_KEY = os.getenv("GEMINI_KEY")

    genai.configure(api_key=GEMINI_KEY)

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    with open(get_resource_path('prompt.txt'), 'r') as file:
        texts = file.read().split(' -\n')

        formatted_texts = [text.replace('\n', '') for text in texts]

        all_text = '; '.join(formatted_texts)

        all_text  = all_text.replace('$-', ': \n')

        response = chat.send_message(all_text)

        file.close()

    if len(response.text) > 240:
        return formulate_sentence()

    return response.text