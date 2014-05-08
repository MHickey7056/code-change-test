import time
global b
def bottles():
    b=10
    for x in range(10):
        print(b, "green bottles, hanging on the wall.")
        print(b, "green bottles, hanging on the wall.")
        print("And if 1 green bottle should acidentally fall,")
        b=b-1
        print("There will be" ,b, "green bottles hanging on the wall.")
        time.sleep(2)
