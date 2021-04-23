# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:42:08 2020

@author: uhalisdemir
"""

import pandas as pd
import numpy as np

# part1 import
df = pd.read_csv(
    "Data/inputd2.txt", header=None, names=["policy", "letter", "input"], sep=" "
)
df["letter"] = df["letter"].map(lambda x: x.rstrip(":"))
df[["min", "max"]] = df.policy.str.split(
    "-",
    expand=True,
)

print(type(df["min"][0]))

df["part1"] = 0
df["part2"] = 0
count = 0

for i in range(0, len(df.index)):
    # part 1
    if (df["input"][i].count(df["letter"][i]) >= int(df["min"][i])) and (
        df["input"][i].count(df["letter"][i]) <= int(df["max"][i])
    ):
        df["part1"][i] = 1
    # part 2
    if (df["input"][i][int(df["max"][i]) - 1] == df["letter"][i]) or (
        df["input"][i][int(df["min"][i]) - 1] == df["letter"][i]
    ):
        if (
            df["input"][i][int(df["max"][i]) - 1]
            != df["input"][i][int(df["min"][i]) - 1]
        ):
            # print("Good input {}; length {}, letter {}; positions {} and {}".format(df["input"][i],len(df["input"][i]),df["letter"][i],int(df["max"][i]), int(df["min"][i])))
            df["part2"][i] = 1
            # print(df["input"][i][int(df["max"][i])-1])
            # print(df["input"][i][int(df["min"][i])-1])
            # print(df["letter"][i])


print(df["part1"].value_counts())
print(df["part2"].value_counts())
