# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:31:58 2020

@author: uhalisdemir
"""

with open("Data/inputd4.txt", "r") as r:
    with open("Data/inputd4new.txt", "w") as w:
        w.write(r.read().replace('\n\n', ','))

import pandas as pd

# df = pd.read_csv('Data/inputd4.txt', header=None, sep=" ", names=["input"])
# dfn = pd.read_csv('Data/inputd4new.txt', header=None, sep=" ", names=["input"])