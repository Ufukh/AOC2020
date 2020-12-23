# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:31:58 2020

@author: uhalisdemir
"""

import pandas as pd

# Passport on single line
# with open("Data/a.txt", "r") as r:
#     with open("Data/inputd4new.txt", "w") as w:
#         w.write(r.read().replace('\n\n', '\nFakeline\n').replace('\n', ' ').replace(' Fakeline ', '\n'))

# create regex pattern to look for
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
pattern = ""
for el in keys:
    pattern += "(?=.*{})".format(el)


# Load cleaned file
df = pd.read_csv('Data/inputd4new.txt', header=None,names=['PassID'])
print(df['PassID'].str.contains(pattern).sum())
