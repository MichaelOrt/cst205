object_list = [
    {
    "key" : "laboratory",
    "type" : "room",
    "title" : "Scientist's Laboratory",
    "description" : "sdfsdfasdfdsa",
    "synonyms" : ["lab", "laboratory", "scientists"],
    "exits" : ["foyer", "basement"]
    },

]

class Room():
    def __init__(self, obj):
        self.title = obj["title"]

rooms_dict = {}

for obj in object_list:
    if (obj["type"] == "room"):
        rooms_dict[obj["key"]] = Room(obj)

print (rooms_dict["laboratory"].title)
