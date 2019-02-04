
def tester():
    print("it is: ", global_var)
    global_var += 10


global_var = 5

tester()

print("It is now: ", global_var)