from html2image import Html2Image
import pandas as pd
import json
import os
from django.template import Template, Context

from Card import Card


def create_page_img(html, path,  id=0):
    hti = Html2Image(output_path=path+"/img")
    hti.screenshot(html_file=html, css_file="./template/template.css", save_as="page_"+str(id)+".png")


def create_page(list_cards, path):
    for c in list_cards:
        str = c.create()


def main():
    cards = pd.read_csv("./cards.csv", sep=";")

    with open("./config.json") as js:
        config = json.load(js)

    # print data to know how many cards will be displayed
    qd_cards = sum(cards["quantity"])
    print("Quantity of cards = %i" % qd_cards)
    print("Number of sheets generated = %i" % (qd_cards % 9 + qd_cards // 9))
    # try to create a directory based on the name of the deck in the config to save pages to print inside
    try:
        print("Creating directory %s" % config["name"])
        os.mkdir("./" + config["name"])
    except:
        print("Impossible to create directory")

    # deck of cards to print
    deck = []

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
            deck.append(Card(
                name=name,
                type=type,
                cost=cost,
                places=places,
                subtype=subtype,
                text=text,
                path_img=path_img,
                config=config
            ))
    # list temp for deck creation
    tmp_list = []
    for i in range(len(deck)):
        tmp_list.append(deck[i])
        if i % 9 == 0:
            create_page(list_cards=tmp_list, path="./"+config["name"])
            tmp_list.clear()


if __name__ == '__main__':
    main()
