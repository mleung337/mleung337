"""CSCA08 Assignment 3

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bilal Syed.

"""

import copy  # needed in examples of functions that modify input dict
from typing import TextIO
from constants import (ID, HEADLINE, LISTED, FEATURES, LOC, DESC, END, SEP,
                       LocType, ListingValueType, ListingType, BookSysType)


EXAMPLE_BOOK_SYS = {
    '137': {
        'identifier': '137',
        'headline': 'Beautiful 4-bedroom home on lakeside',
        'listed': '2024-07-17',
        'features': ['4 bedroom', '3 bath', 'Pool'],
        'location': ('New York', 'USA'),
        'description': '''This is a beautiful 4-bedroom, 3-bath detached house
with an outdoor pool.'''},
    '001': {
        'identifier': '001',
        'headline': 'House',
        'listed': None,
        'features': ['clean'],
        'location': ('Hamilton', 'Canada'),
        'description': None},
    '05': {
        'identifier': '05',
        'headline': 'Stunning lakeside cottage',
        'listed': '2021-02-08',
        'features': [],
        'location': ('Oxford', 'UK'),
        'description': 'This is lakeside!'}
}

EXAMPLE_BY_COUNTRY = {
    'USA': ['137'],
    'Canada': ['001'],
    'UK': ['05']
}


def get_listings(book_sys_file: TextIO) -> list[list]:
    '''Return a list of lists containing lines for listings based on
    information from booking system info in 'book_sys_file'.

    Precondition: 'book_sys_file' is open for reading
                  'book_sys_file' is in the format described in the handout
    '''

    new_list = []
    inner_list = []
    file_list = book_sys_file.readlines()

    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip()

    for line in file_list:
        if line != END:
            inner_list.append(line)
        else:
            new_list.append(inner_list)
            inner_list = []

    return new_list


def get_location(listing: list) -> tuple[str, str]:
    """Return a location as a tuple based on information from listing
    'listing'.

    >>> get_location(['001', 'House', '', 'clean', '', 'Canada;Hamilton',
    ... '']) == ('Hamilton', 'Canada')
    True
    >>> get_location(['137', 'Beautiful 4-bedroom home on lakeside',
    ... '2024-07-17', '4 bedroom', '3 bath', 'Pool', '', 'USA;New York',
    ... '''This is a beautiful 4-bedroom, 3-bath detached house
    ... with an outdoor pool.''']) == ('New York', 'USA')
    True
    """

    loc_index = listing.index('', 3) + 1

    if listing[loc_index] != '':
        location = listing[loc_index].split(';')
        location[0], location[1] = location[1], location[0]
        location = tuple(location)
    else:
        location = None

    return location


def get_desc(listing: list) -> str:
    """Return a description as a string based on information from listing
    'listing'.

    >>> get_desc(['001', 'House', '', 'clean', '', 'Canada;Hamilton',
    ... '']) == ''
    True
    >>> desc = get_desc(['137', 'Beautiful 4-bedroom home on lakeside',
    ... '2024-07-17', '4 bedroom', '3 bath', 'Pool', '', 'USA;New York',
    ... '''This is a beautiful 4-bedroom, 3-bath detached house
    ... with an outdoor pool.'''])
    >>> desc == '''This is a beautiful 4-bedroom, 3-bath detached house
    ... with an outdoor pool.'''
    True
    """

    feats_end = listing.index('', 3)
    desc = ''

    for j in range(len(listing[feats_end + 2:])):
        desc += listing[feats_end + 2:][j] + '\n'

    return desc.strip()


# We provide the header and docstring for this function to get you
# started and to demonstrate that there are no docstring examples in
# functions that read from files.
def read_book_sys_file(book_sys_file: TextIO) -> BookSysType:
    """Return a dict containing all booking system info in 'book_sys_file'.

    Precondition: 'book_sys_file' is open for reading
                  'book_sys_file' is in the format described in the handout
    """

    listings = get_listings(book_sys_file)
    book_sys = {}

    for listing in listings:
        listing_dict = {}

        feats_end = listing.index('', 3)
        feats = listing[3:feats_end]

        location = get_location(listing)

        desc = get_desc(listing)

        listing_dict[ID] = listing[0]
        listing_dict[HEADLINE] = listing[1]
        listing_dict[LISTED] = listing[2]
        listing_dict[FEATURES] = feats
        listing_dict[LOC] = location
        listing_dict[DESC] = desc

        for info in listing_dict.items():
            if info[1] == '':
                listing_dict[info[0]] = None

        book_sys[listing[0]] = listing_dict

    return book_sys


# We provide the header and PART of a docstring for this function to
# get you started and to demonstrate the use of example data.
def make_country_to_listings(
        book_sys: BookSysType) -> dict[str, list[str]]:
    """Return a dict that maps each country to a list of IDs of listings in
    that country based on the information in booking system data 'book_sys'.

    >>> make_country_to_listings(EXAMPLE_BOOK_SYS) == EXAMPLE_BY_COUNTRY
    True
    >>> make_country_to_listings({'001': {'identifier': '001',
    ... 'headline': None,
    ... 'listed': None, 'features': None, 'location': ('Hamilton', 'Canada'),
    ... 'description': None}}) == {'Canada':['001']}
    True
    """

    new_dict = {}

    for listing in book_sys:
        if book_sys[listing][LOC] is None or book_sys[listing][ID] is None:
            return {}

        country = book_sys[listing][LOC][1]
        identifier = book_sys[listing][ID]

        if country in new_dict:
            new_dict[country].append(identifier)
        else:
            new_dict[country] = [identifier]

    return new_dict


def get_most_popular_countries(book_sys: BookSysType) -> list[str]:
    '''Return a list of countries with the most listings based on the
    information in booking system data 'book_sys'. In case of a tie, list will
    have more than one entry.

    >>> get_most_popular_countries(EXAMPLE_BOOK_SYS) == ['Canada', 'UK', 'USA']
    True
    >>> get_most_popular_countries({'137': {'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None}, '001': {'identifier': '001', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}, '05': {'identifier': '05', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}}) == ['UK']
    True
    '''

    new_list = []
    country_dict = make_country_to_listings(book_sys)

    for country in country_dict:
        country_dict[country] = len(country_dict[country])

    for country in country_dict.items():
        if len(new_list) == 0:
            new_list.append(country[0])
        else:
            if country[1] > country_dict[new_list[0]]:
                new_list = [country[0]]
            elif country[1] == country_dict[new_list[0]]:
                new_list.append(country[0])

    new_list.sort()

    return new_list


def get_most_features(book_sys: BookSysType) -> list[str]:
    '''Return a list of IDs of listings with the most features based on the
    information in booking system data 'book_sys'. In case of a tie, list will
    have more than one entry.

    >>> get_most_features(EXAMPLE_BOOK_SYS) == ['137']
    True
    >>> get_most_features({'137': {'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None}, '001': {'identifier': '001', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}, '05': {'identifier': '05', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}}) == ['001', '05', '137']
    True
    '''

    new_list = []
    feature_dict = {}

    for listing in book_sys:
        feature_dict[listing] = len(book_sys[listing][FEATURES])

    for listing in feature_dict.items():
        if len(new_list) == 0:
            new_list.append(listing[0])
        else:
            if listing[1] > feature_dict[new_list[0]]:
                new_list = [listing[0]]
            elif listing[1] == feature_dict[new_list[0]]:
                new_list.append(listing[0])

    new_list.sort()

    return new_list


def assign_ratings(book_sys: BookSysType) -> None:
    """Update the metadata in booking system data 'book_sys' such that each
    listing gets new key 'rating' mapping to int. For listings that have the
    most features, assign a rating of 5, while the rest will get a rating of 3.

    >>> book_sys_copy = copy.deepcopy(EXAMPLE_BOOK_SYS)
    >>> assign_ratings(book_sys_copy)
    >>> book_sys_copy == {'137': {'identifier': '137',
    ... 'headline': 'Beautiful 4-bedroom home on lakeside',
    ... 'listed': '2024-07-17', 'features': ['4 bedroom', '3 bath', 'Pool'],
    ... 'location': ('New York', 'USA'),
    ... 'description': '''This is a beautiful 4-bedroom, 3-bath detached house
    ... with an outdoor pool.''', 'rating': 5}, '001': {'identifier': '001',
    ... 'headline': 'House', 'listed': None, 'features': ['clean'],
    ... 'location': ('Hamilton', 'Canada'), 'description': None, 'rating': 3},
    ... '05': {'identifier': '05', 'headline': 'Stunning lakeside cottage',
    ... 'listed': '2021-02-08', 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': 'This is lakeside!', 'rating': 3}}
    True
    >>> book_system = {'137': {'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None}, '001': {'identifier': '001', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}, '05': {'identifier': '05', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}}
    >>> assign_ratings(book_system)
    >>> book_system == {'137': {'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None, 'rating': 5}, '001': {'identifier': '001',
    ... 'headline': None, 'listed': None, 'features': [],
    ... 'location': ('Oxford', 'UK'), 'description': None, 'rating': 5},
    ... '05': {'identifier': '05', 'headline': None, 'listed': None,
    ... 'features': [], 'location': ('Oxford', 'UK'), 'description': None,
    ... 'rating': 5}}
    True
    """

    most_features = get_most_features(book_sys)

    for listing in book_sys:
        if listing in most_features:
            book_sys[listing]['rating'] = 5
        else:
            book_sys[listing]['rating'] = 3


def is_complete(listing: ListingType) -> bool:
    """Return True if and only if listing 'listing' is complete, meaning it is
    not missing any information.

    >>> is_complete({'identifier': '137',
    ... 'headline': 'Beautiful 4-bedroom home on lakeside',
    ... 'listed': '2024-07-17', 'features': ['4 bedroom', '3 bath', 'Pool'],
    ... 'location': ('New York', 'USA'),
    ... 'description': '''This is a beautiful 4-bedroom, 3-bath detached house
    ... with an outdoor pool.'''}) == True
    True
    >>> is_complete({'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None}) == False
    True
    """

    for key in listing:
        info = listing[key]

        if info in [None, []]:
            return False

    return True


# We provide the header and PART of a docstring for this function to
# get you started and to demonstrate the use of function deepcopy in
# examples that modify input data.
def keep_complete_listings(book_sys: BookSysType) -> None:
    """Update the booking system data 'book_sys' so that it only contains
    listings that are not missing any information.

    >>> book_sys_copy = copy.deepcopy(EXAMPLE_BOOK_SYS)
    >>> keep_complete_listings(book_sys_copy)
    >>> book_sys_copy == {'137': EXAMPLE_BOOK_SYS['137']}
    True
    >>> book_system = {'137': {'identifier': '137',
    ... 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('New York', 'USA'),
    ... 'description': None}, '001': {'identifier': '001', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}, '05': {'identifier': '05', 'headline': None,
    ... 'listed': None, 'features': [], 'location': ('Oxford', 'UK'),
    ... 'description': None}}
    >>> keep_complete_listings(book_system)
    >>> book_system == {}
    True
    """

    listing_to_pop = []

    for listing in book_sys:
        if not is_complete(book_sys[listing]):
            listing_to_pop.append(listing)

    for listing in listing_to_pop:
        book_sys.pop(listing)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # uncomment to test with example data files
    # with open('example_data.txt', 'r') as example_data:
    #     RESULT = read_book_sys_file(example_data)
    #     print('Did we produce a correct dict? ', RESULT == EXAMPLE_BOOK_SYS)

    # uncomment to work with a larger data set
    # with open('data.txt') as data_txt:
    #     EXAMPLE = read_book_sys_file(data_txt)

    # EXAMPLE_COUNTRY_TO_LISTING = make_country_to_listings(EXAMPLE)
    # EXAMPLE_MOST_POPULAR_COUNTRIES = get_most_popular_countries(EXAMPLE)
    # print(EXAMPLE_MOST_POPULAR_COUNTRIES)
