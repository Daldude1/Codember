import requests 

# Get text words
url = "https://codember.dev/data/message_01.txt"

req = requests.get(url)
words = req.text.lower().split()

repeated_words = {}

for word in words:
    if word in repeated_words:
        repeated_words[word] += 1
    else:
        repeated_words[word] = 1

# Generate the text format as "murcielago15leon15"
text = ""
for word, quantity in repeated_words.items():
    text += f"{word}{quantity}"

print(text)