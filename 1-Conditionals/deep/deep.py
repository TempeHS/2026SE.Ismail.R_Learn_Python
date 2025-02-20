ans = input("What is the answer to Great Question of Life, the universe and everything? ")
    
match ans.casefold():
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _: 
        print("No")

