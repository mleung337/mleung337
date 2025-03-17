"""CSCA08 Assignment 3

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bilal Syed.

"""

from copy import deepcopy
import unittest
from booking_system import get_most_popular_countries as get_mpcs


class TestGetMostPopularCountries(unittest.TestCase):
    """Test the function get_most_popular_countries."""

    def setUp(self):
        self.example = {
            '137': {
                'identifier': '137',
                'headline': 'Beautiful 4-bedroom home on lakeside',
                'listed': '2024-07-17',
                'features': ['4 bedroom', '3 bath', 'Pool'],
                'location': ('New York', 'USA'),
                'description': 'This is a beautiful 4-bedroom, 3-bath detached'
                ' house\nwith an outdoor pool.'},
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

    def test_handout_example(self):
        """Test get_most_popular_countries with the handout example."""

        book_sys_copy = deepcopy(self.example)
        expected = ['Canada', 'UK', 'USA']
        actual = get_mpcs(self.example)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_bad_system(self):
        """Test get_most_popular_countries with a system that has invalid
        listing."""

        book_system = {'999': {
                           'identifier': '999',
                           'headline': None,
                           'listed': None,
                           'features': None,
                           'location': None,
                           'description': None}}
        book_sys_copy = deepcopy(self.example)
        expected = []
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_no_listings(self):
        '''Test get_most_popular_countries with no listings.'''
        
        book_system = {}
        book_sys_copy = deepcopy(book_system)
        expected = []
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test__single_listing(self):
        '''Test get_most_popular_countries with one listing.'''
        
        book_system = {'137': {
            'identifier': '137',
            'headline': 'Beautiful 4-bedroom home on lakeside',
            'listed': '2024-07-17',
            'features': ['4 bedroom', '3 bath', 'Pool'],
            'location': ('New York', 'USA'),
            'description': 'This is a beautiful 4-bedroom, 3-bath detached'
            ' house\nwith an outdoor pool.'}}
        book_sys_copy = deepcopy(book_system)
        expected = ['USA']
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)    

    def test_one_winner_example1(self):
        '''Test get_most_popular_countries with multiple listings, one winner'''
        
        book_system = {'137': {
            'identifier': '137',
            'headline': 'Beautiful 4-bedroom home on lakeside',
            'listed': '2024-07-17',
            'features': ['4 bedroom', '3 bath', 'Pool'],
            'location': ('New York', 'USA'),
            'description': 'This is a beautiful 4-bedroom, 3-bath detached'
            ' house\nwith an outdoor pool.'},
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
                           'location': ('Hamilton', 'Canada'),
                           'description': 'This is lakeside!'}}
        book_sys_copy = deepcopy(book_system)
        expected = ['Canada']
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_one_winner_example2(self):
        '''Test get_most_popular_countries with multiple listings, one winner'''
        
        book_system = {'137': {
            'identifier': '137',
            'headline': 'Beautiful 4-bedroom home on lakeside',
            'listed': '2024-07-17',
            'features': ['4 bedroom', '3 bath', 'Pool'],
            'location': ('New York', 'USA'),
            'description': 'This is a beautiful 4-bedroom, 3-bath detached'
            ' house\nwith an outdoor pool.'},
                       '001': {
                           'identifier': '001',
                           'headline': 'House',
                           'listed': None,
                           'features': ['clean'],
                           'location': ('New York', 'USA'),
                           'description': None},
                       '05': {
                           'identifier': '05',
                           'headline': 'Stunning lakeside cottage',
                           'listed': '2021-02-08',
                           'features': [],
                           'location': ('Oxford', 'UK'),
                           'description': 'This is lakeside!'}}
        book_sys_copy = deepcopy(book_system)
        expected = ['USA']
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_one_winner_example3(self):
        '''Test get_most_popular_countries with multiple listings, one winner'''
        
        book_system = {'137': {
            'identifier': '137',
            'headline': 'Beautiful 4-bedroom home on lakeside',
            'listed': '2024-07-17',
            'features': ['4 bedroom', '3 bath', 'Pool'],
            'location': ('Oxford', 'UK'),
            'description': 'This is a beautiful 4-bedroom, 3-bath detached'
            ' house\nwith an outdoor pool.'},
                       '001': {
                           'identifier': '001',
                           'headline': 'House',
                           'listed': None,
                           'features': ['clean'],
                           'location': ('Oxford', 'UK'),
                           'description': None},
                       '05': {
                           'identifier': '05',
                           'headline': 'Stunning lakeside cottage',
                           'listed': '2021-02-08',
                           'features': [],
                           'location': ('Oxford', 'UK'),
                           'description': 'This is lakeside!'}}
        book_sys_copy = deepcopy(book_system)
        expected = ['UK']
        actual = get_mpcs(book_system)
        msg = message(book_sys_copy, expected, actual)
        self.assertEqual(actual, expected, msg)


def message(test_case: dict, expected: list, actual: object) -> str:
    """Return an error message saying the function call
    get_most_popular_countries(test_case) resulted in the value
    actual, when the correct value is expected.

    """

    return ('When we called get_most_popular_countries(' + str(test_case)
            + ') we expected ' + str(expected)
            + ', but got ' + str(actual))


if __name__ == '__main__':
    unittest.main(exit=False)
