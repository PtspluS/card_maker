import pdfkit
import pandas as pd
import json
import os
from django.template import Template, Context

cards = pd.read_csv("./cards.csv", sep=";")

with open("./config.json") as js:
    config = json.load(js)

qd_cards = sum(cards["quantity"])
print("Quantity of cards = %i" % qd_cards)
print("Number of sheets generated = %i" % (qd_cards % 9 + qd_cards // 9))
try:
    print("Creating directory %s" % config["name"])
    os.mkdir("./" + config["name"])
except:
    exit("Error ! Impossible to create directory")




print(0)
