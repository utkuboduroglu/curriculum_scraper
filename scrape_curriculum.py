#!/usr/bin/env python
# let's use env for finding our appropriate python binary
from bs4 import BeautifulSoup
import requests

# we import these to read cmdline arguments and check whether
# the specified course file exists
import sys
import os

# Our request will be made to the following URI:
# https://catalog.metu.edu.tr/course.php?prog=236&course_code=<course code>
# The GET request will send us an HTML page, from which we want to extract
# the object <div class="field-body"></div>
#
# We want to get rid of the object(s):
#     * <div id="navbar"></div>
#     * <table class="course"></table>

# we define a special type of exception for use with failed lookups
class LookupException(Exception):
    pass

def getCourseHTML(course_code):
    metuURL = "https://catalog.metu.edu.tr/course.php"
    payload = { "prog": 236, "course_code": course_code }

    r = requests.get(metuURL, params=payload)
    if (r.status_code != 200):
        raise LookupException("Failed to get page!")
    return r.text

def getCourseDescription(course_code):
    html_source = getCourseHTML(course_code)
    soup = BeautifulSoup(html_source, 'html.parser')

    # We have obtained the description text we desire, but we still
    # have to 'decompose' the navbar and the table
    description = soup.find('div', { "class": "field-body" })

    navbar = description.find('div', { 'id': 'navbar' })
    navbar.decompose()

    # the program outcomes matrix does not display correctly;
    # hence we decompose all tables
    for table in description.find_all('table'):
        table.decompose()

    # the above does not work for the outcome matrix, instead we may
    # attempt to remove the third iframe object (lol what :)
    iframeCount = 0
    for iframe in description.find_all('iframe'):
        if iframeCount == 2:
            iframe.decompose()
            break
        iframeCount += 1


    return description


def main():
    if len(sys.argv) < 2:
        raise Exception("No file specified!")

    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception("The specified file does not exist!")

    with open(filename, 'r') as file:
        for line in file:
            try:
                # we strip the line of its newline character
                print(getCourseDescription(line.rstrip()))
            # we may obtain AttributeErrors from decompose() calls
            # it's safe to ignore them
            except (LookupException, AttributeError):
                continue
                

if __name__ == "__main__":
    main()

