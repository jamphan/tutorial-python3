age = int(input("How old are you?"))

if (age > 25):
    print("You're probably having a mid-life crisis right now")
elif (age > 19):
    print("You're a young adult")
if (age > 10):
    print("You're a teenager")
else:
    print("You're getting old")

# ==================================================================================================

if (10 < age <= 19):
    print("You're a teenager")
elif (age > 19 and age <= 25): #Short for "else if"
    print("You're a young adult")
elif (age > 25) :
    print("You're probably having a mid-life crisis right now")
else:
    print("You're pretty young")