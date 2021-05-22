import img2pdf
from html2image import Html2Image
from PIL import Image
import pandas as pd
import json
import os
import glob
from django.template import Template, Context

from Card import Card

def create_page_img(html, path,  id=0):
    hti = Html2Image(output_path=path+"/img")
    hti.screenshot(html_file=html, css_file="./template/template.css", save_as="page_"+str(id)+".png")


def main():
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
        print("Impossible to create directory")

    lst_cards = []

    for index, row in cards.iterrows():
        # list param for each card in the csv
        name = row["name"]
        quantity = row["quantity"]
        type = row["type"]
        cost = row["cost"]
        places = row["places"]
        subtype = row["subtype"]
        text = row["text"]
        path_img = row["path_img"]

        for quant in range(quantity):
            lst_cards.append(Card(
                name=name,
                type=type,
                cost=cost,
                places=places,
                subtype=subtype,
                text=text,
                path_img=path_img,
                config=config
            ))

    lst_cards.append(None)

    # create_page_img("./template/template_sheet.html", "./"+config["name"])


if __name__ == '__main__':
    main()
