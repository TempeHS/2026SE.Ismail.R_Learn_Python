def main():
    user_inputtime = input("What is the time? ")
    user_inputtime = convert(user_inputtime)
    if 7 <= user_inputtime <= 8:
        print("Breakfast Time")
    elif 12 <= user_inputtime <= 13:
        print("Lunch Time")
    elif 18 <= user_inputtime <= 19:
        print("Dinner Time")
    else:
        print("No meal")

def convert(time):
    hours, minutes = (time.split(":"))
    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)
    
if __name__ == "__main__":
    main()