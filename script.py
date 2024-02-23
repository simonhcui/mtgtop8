import requests
import re
from bs4 import BeautifulSoup

def get_event_links():
    event_list = []
    last_event_list_size = 0
    page_number = 1

    while True:
        req = requests.get("https://www.mtgtop8.com/format?f=ST&meta=97&cp=" + str(page_number))
        soup = BeautifulSoup(req.content, "html.parser")
        events_on_page = soup.find_all('a',  attrs={'href': re.compile("^event")})

        for link in events_on_page[:-1]: 
            event_link = link.get('href')
            if(event_link not in event_list):
                event_list.append(event_link)

        if(len(event_list) > last_event_list_size):
            last_event_list_size = len(event_list)
        else:
            break
        page_number = page_number + 1

    return event_list

def check_for_creature(event, creature):
    req = requests.get("https://www.mtgtop8.com/" + event)
    soup = BeautifulSoup(req.content, "html.parser")
    event_info = soup.find_all('div', class_ = 'event_title')
    winning_decklist = []

    for card in soup.find_all('span', class_ = 'L14'):
        winning_decklist.append(card.text)
    if(creature in winning_decklist):
        print(event_info[0].text + " " + event_info[1].text)

def main():
    events = get_event_links()
    for event in events:
        check_for_creature(event, "Swamp")

if __name__ == "__main__":
    main()