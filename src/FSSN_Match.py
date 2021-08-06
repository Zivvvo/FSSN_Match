import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument("Datapath", type=str)
argparser.add_argument("--Timeslots", default = 8, type = int)
argparser.add_argument("--Outputpath", default = ".", type=str)
argparser.add_argument("--Outputname", default = "results.csv", type =str)

args = argparser.parse_args()

import sys
sys.path.append(".")

import utils.excel_parser as parser

df = parser.load_csv(args.Datapath)

pref_list = parser.generate_pref_list(df)
profs = parser.generate_profs(df, args.Timeslots)

students = parser.generate_students(df, pref_list, profs)

import utils.match as match

match = match.match(students, profs)
match.fit()

df = match.generate_table()

print(df)

import os

df.to_csv(os.path.join(args.Outputpath, args.Outputname))



