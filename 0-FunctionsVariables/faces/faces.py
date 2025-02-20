def convert(text: str):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    
def main():
    something = input("text: ")
    print(convert(something))

main()