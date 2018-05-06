#!/usr/bin/env python3

import random
import requests
from bs4 import BeautifulSoup

"""
Grab a random url from https://www.simplyrecipes.com/ to go to FlavorTown
"""

BASE_URL = 'https://www.simplyrecipes.com/recipes/ingredient/'

INGREDIENT_CATEGORIES = ['chicken', 'beef', 'fish_and_seafood', 'pasta', 'cheese', 'duck', 'egg', 'pork', 'rice',
                         'seafood', 'turkey', 'vegetables',
]  # /recipes/ingredient/{this}

# TODO: do we care about this?
# MEAL_TYPES = [ 'quick', 'budget', 'baking', 'cookie' ]  # /type/{this}


# so, LOTS of stuff on simplyrecipes 403s for no fucking reason at all.
def random_meal(category=None, debug=False):
    """
    try to get a random thing from simplyrecipes
    :param category: string
    :param debug: bool
    :return:
    """
    success = None
    max_retry_count = 0
    rec_list = None
    while success != 200:
        if max_retry_count == 10:
            if debug:
                print("We can't get a reply, simplyrecipes is bad.")
                exit()
        if not category:
            category = INGREDIENT_CATEGORIES[random.randint(0, len(INGREDIENT_CATEGORIES) - 1)]
        else:
            if category not in INGREDIENT_CATEGORIES:
                raise Exception("We don't have " + category)
        item_url = BASE_URL + category + "/"
        rec_list = requests.get(item_url)
        success = rec_list.status_code
        if success != 200:
            max_retry_count += 1
            if debug:
                print("Oops, problem fetching " + item_url + " (code " + str(success) + ")")
                print("Going to try again")

    thesoup = BeautifulSoup(rec_list.content, "html.parser")
    some_items = thesoup.find_all("h2", itemprop="name")
    # pick one at random!
    return some_items[random.randint(0, len(some_items)-1)].string


if __name__ == "__main__":
    print(random_meal(debug=True))