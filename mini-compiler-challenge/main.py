import requests

def mini_compiler(code):
    value = 0

    for symbol in code:
        if symbol == "#":
            value += 1
        elif symbol == "@":
            value -= 1
        elif symbol == "*":
            value *= value
        elif symbol == "&":
            print(value, end="")

# Get the message from the file
url = "https://codember.dev/data/message_02.txt"
req = requests.get(url)
message = req.text

# Execute the program
mini_compiler(message)
