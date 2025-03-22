def user_input():# Worked on it 2/27/25 6:50PM
    user = input("Has it rained recently? (Y/N): ")
    if user == "Y" or user == "y":
        return user
    else:
        print("Hopefully it rains soon")
        quit()

def rain_info_collect(user):
    total = 0
    days = 0

    while user == "Y" or user == "y":
        rain_info = int(input("How many inches did it rain?: "))
        total += rain_info
        days += 1
        user = input("Did it rain another day? (Y/N): ")
    else:
        return total, days

def rain_average(total, days):
    rainAvg = total / days
    return rainAvg

def rain_info(total, days, rainAvg):
    print(f"Total days rained is {days}")
    print(f"Total amount rained, in inches, is {total}")
    print(f"The average ammount of rain is {rainAvg}")

def main():
    user = user_input()
    total, days = rain_info_collect(user)
    rainAvg = rain_average(total, days)
    rain_info(total, days, rainAvg)

main()
