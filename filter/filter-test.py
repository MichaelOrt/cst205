import pprint

# the function
def r_name(something):
    if something.find('r') == -1:
        return 0
    if something.find('r') != -1:
        return 1

pprint.pprint(filter(r_name, ["Mark", "Betty", "Matthew","Jenny"]))