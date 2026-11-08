def main():
    text = input("input any text: ")
    print(convert(text))

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text

main()
