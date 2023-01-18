# scrape_curriculum -- a very specialized scraper
This is a very specialized scraping script written in python, for the sole purpose of being able to compile a document containing all the course information provided by METU Math, which was requested by TUM.de. There probably was an easier way of obtaining this information (such as just asking for it), but I felt that the task could be handled with ease.

## Drawbacks
The script only considers scraping `prog=236`, and does not account for the `iframe` content in the pages themselves. These two changes can definitely help generalize the script for use by more peers.
