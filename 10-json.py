## Json
# Note: in json True/False is set to true/false , None. to null https://www.w3schools.com/js/js_json_datatypes.asp
import json

person =   {
    "name": "Aamir Solangi",
    "language": "Sindhi",
    "id": "IAKPO3R4761JDRVG",
    "bio": "Vestibulum pharetra libero et velit gravida euismod. Quisque mauris ligula, efficitur porttitor sodales ac, lacinia non ex. Fusce eu ultrices elit, vel posuere neque.",
    "version": 7.27,
    "titles": ["engineer", "programmer"]
  },
# convert to list
personJSON = json.dumps(person, indent=4, sort_keys=True) # indent, sort_keys, seperator this are optional parameter
print(personJSON)
#write to file
with open('file.json', 'w') as file:
    json.dump(person, file, indent=4)

# convert from json to dict
person = json.load(personJSON)

#
