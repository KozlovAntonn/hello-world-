import time


def function_one():
    list = ["one", "two", "three", "four", "five"]
    for x in list:
        print(x + "_number")
        time.sleep(1)

function_one()

