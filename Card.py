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
            if type in t:
                self.template = t.get(type)


    def create(self):
        context = {
            'name': self.name,
            'path_img': self.path_img,
            'text': self.text
        }

        template = open(self.template, 'r')
        str = template.read().format()
        template.close()

        return str