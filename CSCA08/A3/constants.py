"""CSCA08 Assignment 3

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bilal Syed.

"""

ID = 'identifier'
HEADLINE = 'headline'
LISTED = 'listed'
FEATURES = 'features'
LOC = 'location'
DESC = 'description'
END = 'ENDOFLISTING'
SEP = ';'

# We store locations as tuples of two strs: (city, country).
LocType = tuple[str, str]

# ListingValueType is the type for valid values in the ListingType dict.
# All values are None or str, except for the value associated with key LOC,
# which is LocType, or key FEATURES, which is list[str].
ListingValueType = None | str | LocType | list[str]

# ListingType is a dict that maps keys ID, HEADLINE, LISTED, FEATURES,
# LOC, and DESC to their values (of type ListingValueType).
ListingType = dict[str, ListingValueType]

# BookSysType is a dict that maps listing identifiers to listings,
# i.e. to values of type ListingType.
BookSysType = dict[str, ListingType]
