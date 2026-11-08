# ask user for their name
#name = input("whats your name? ").strip().title()

# split user's name into first and last name
#first, last = name.split(" ")

# say hello to user
#print(f"Hello {first}, how you doing?")

def main():
    name = input("what's your name? ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()