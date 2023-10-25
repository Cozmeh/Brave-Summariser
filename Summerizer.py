import requests,time
from bs4 import BeautifulSoup

def get_summary(question):
    
    formatted_sentence = question.replace(" ", "%20")
    search_formatted_sentence = question.replace(" ", "+")

    api_url = f'https://search.brave.com/api/summarizer?key={formatted_sentence}%3Aus%3Aen'
    search_url = f'https://search.brave.com/search?q={search_formatted_sentence}'

    try:
        search_response = requests.get(search_url)
        if search_response.status_code == 200:
                time.sleep(1)
                result = requests.get(api_url).json()["results"][0].get("text")
                parsed_text = BeautifulSoup(result, 'html.parser')
                text = parsed_text.get_text()
                return text
        else:
            return "Sorry, I couldn't find anything."
        
    except requests.exceptions.RequestException as e:
        return "Sorry, there was an error."


print(get_summary("what is book?"))
