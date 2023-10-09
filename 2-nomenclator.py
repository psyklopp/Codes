# read the supporting JSON file and load it to a dictionary
# the setup file named 2-nomenclator-setup.json is in the same dir as the program
import json
with open("2-nomenclator-setup.json") as file:
    data = json.load(file)

# read the plaintext
text = data["plaintext"]
print("Plaintext: ", text)

print('There are', len(data['special']), 'special substitutions being used..')

if len(data['special']) > 5:
    print("No more than 5 special substitutions allowed")
    exit(0)

# special substitution first
for plain in data["special"]:
    text = text.replace(plain, data["special"][plain])

print("After special substitution: ", text)

# normal substitution second
for plain in data["letters"]:
    text = text.replace(plain, data["letters"][plain])

print("Final ciphertext: ", text)