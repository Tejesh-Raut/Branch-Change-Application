from preprocessing import table_preprocessed
import sys, csv

table_sorted = list(table_preprocessed)
table_sorted.sort(key=lambda l:l[3], reverse=True)
