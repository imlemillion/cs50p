def main():
    time = input("What time is it? ")
    hour = convert(time)
    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    new_time = time.split(":")
    hours = float(new_time[0])
    minutes = float(new_time[1])
    return hours + minutes / 60

if __name__ == "__main__":
    main()
