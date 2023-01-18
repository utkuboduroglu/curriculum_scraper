# scrape_curriculum -- a very specialized scraper
This is a very specialized scraping script written in python, for the sole purpose of being able to compile a document containing all the course information provided by METU Math, which was requested by TUM.de. There probably was an easier way of obtaining this information (such as just asking for it), but I felt that the task could be handled with ease.

## Drawbacks
At this point, the script accounts for both the `prog=236` parameter, as well as the content of the `iframe`s, though the output is definitely not pretty. In order to combat the unwanted tags, I've begun to use the following sed rule for post-processing:

```
./scrape_curriculum.py course_codes.txt | sed 's/^<.*>$//g;
    s/METU\ |\ Course\ Syllabus//g' > course_descriptions.txt
```
