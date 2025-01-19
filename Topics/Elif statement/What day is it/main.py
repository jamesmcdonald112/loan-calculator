num = int(input())


def time(num):
    if (num > 13):
        print("Wednesday")
    elif (num < -10):
        print("Monday")
    else:
        print("Tuesday")

time(num)