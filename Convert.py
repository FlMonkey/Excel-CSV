from tkinter import filedialog
import pandas as pd
import xlrd
import csv


filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a File",
                                              filetypes=(("Excel", "*.xlsx"), ("all files", "*.*")))

read_file = pd.read_excel(filename)

# Write the dataframe object
# into csv file
read_file.to_csv("Pandas.csv",index=None,sep=',')

# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Pandas.csv"))

# show the dataframe
df

