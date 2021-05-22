import json


class Card:

    def __init__(self, name, type, cost, places, subtype, text, path_img, config):
        """

        :param name: Name of the card
        :param type: Type of the card
        :param cost: Cost of the card
        :param places: Places inside the room
        :param subtype: Subtype of the room
        :param text: Effect of the room or the card
        :param path_img: Path to the image to display in the card
        :param config: JSON config file
        """
        self.name = name
        self.type = type
        self.cost = cost
        self.places = places
        self.subtype = subtype
        self.text = text
        self.path_img = path_img
        self.config = config

        for t in config["type"]:
            if type == t:
                self.template = t
