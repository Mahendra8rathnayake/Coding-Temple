print("Hello World!")
print("hello world")
print("Hello python interpreter!")
print("Hello World!")
print("Hello Python World!")
print("Hello_World.py")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "\nSay to audiance , and they will repeat back to you:"
prompt += "\nEnter 'quit' to end the program. "
while message != 'quit':
    input(prompt)
    print(message)

    if message != 'quit':
        print(message)

prompt = "\ntell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active: 
    message = input(prompt)

    if message == 'quit':
        ctive = False
    
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited."
prompt += "n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else: 
        print("I'd love to go to " + city.title() + "!")