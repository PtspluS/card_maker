import pdfkit
import pandas as pd
import json
import sys
from django.template import Template, Context

cards_csv = pd.read_csv("./cards.csv")

with open("./config.json") as js:
    config = json.load(js)

print(0)