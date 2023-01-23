def main():
    time = input('What time is it? (24-hour format) ')
    converted_time = convert(time)
    if converted_time >= 7 and converted_time < 12:
        print("It's breakfast time.")
    elif converted_time >= 12 and converted_time < 18:
        print("It's lunch time.")
    elif converted_time >= 18 and converted_time < 24:
        print("It's dinner time.")



def convert(time):
    hours , minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes) 
    if minutes <= .15:
        minutes = .25
    elif minutes <= .30:
        minutes = .5
    elif minutes <= .45:
        minutes = .75
    elif minutes <= .60:
        minutes = 0
        hours += 1
    
    return hours + (minutes / float(60))


if __name__ == "__main__":
    main()

