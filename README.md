# mtgtop8

Python script that scrapes mtgtop8.com to check for winning decklists involving the specified creature.
This is the prettified snapshot of the overall mess that I quickly jumbled together while bored. 

This version requires hard coding the format URL (Line 11) to be scraped and the creature name (Line 42) to be searched up. 
For example, if we wanted to look up all Standard Pro Tours, we would use the following link: https://www.mtgtop8.com/format?f=ST&meta=91
There is logic for reading all pages of events.

When I actually compiled all of my data fed in an input file with all the creatures and format links beforehand. 
The creature list came from manually singling up unemployed creatures from the first page of the formats on: https://www.mtgtop8.com/topcards

Output on my original version was sent to a CSV file which contained more data such as date of the event. 
For this simplified example I just spit out the event title, winning decklist, and player name in the command line. 

## Setup
pip install the necessary dependencies
* BeautifulSoup
* re
* requests

## Running
py script.py
