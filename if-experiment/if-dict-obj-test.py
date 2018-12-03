object_list = [
    {
    "key" : "laboratory",
    "type" : "room",
    "title" : "Scientist's Laboratory",
    "description" : "sdfsdfasdfdsa",
    "synonyms" : ["lab", "laboratory", "scientists"],
    "exits" : ["foyer", "basement"]
    },
    "key", "vomit",
    "title", "Dragon's Vomit",
    "type", "item",
    "takable" : False,
    "description" : "sfdsaf",
    "effect" : {
        "inspect": ["examine vomit", "move endgame"]
    },
    {
    "key" : "broken_furniture",
    "type" : "item",
    "effect" : {
        "inspect": [("add_to_inventory", "bullet"),
                    ("describe", 
                    """You found abullet!""") ]
        }
    }


]

class Room():
    def __init__(self, obj):
        self.title = obj["title"]

rooms_dict = {}

for obj in object_list:
    if (obj["type"] == "room"):
        rooms_dict[obj["key"]] = Room(obj)

print (rooms_dict["laboratory"].title)
