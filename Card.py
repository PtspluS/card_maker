class Card:

    def __init__(self, name, type, cost, places, subtype, text, path_img, config):
        """
        Create the Card object.
        str:param name: Name of the card
        str:param type: Type of the card
        str:param cost: Cost of the card
        str:param places: Places inside the room
        str:param subtype: Subtype of the room
        str:param text: Effect of the room or the card
        str:param path_img: Path to the image to display in the card
        str:param config: JSON config file
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
        """
        Open the template link with the type of the card et replace the elements inside with the value of the card.
        str:return: return a string for the html template
        """

        template = open(self.template, 'r').read()
        str = template.format(
            name=self.name,
            type=self.type,
            cost=self.cost,
            places=self.places,
            subtype=self.subtype,
            text=self.text,
            path_img=self.path_img
        )
        template.close()

        return str
