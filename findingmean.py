import csv 
import pandas as pd 
import plotly.express as pl 
import statistics

with open('data.csv', newline='') as f:
    reader = csv.reader()
    file_data = file_data = list(reader)
mean = statistics.mean(reader)
stdev = statistics.stdev(reader)