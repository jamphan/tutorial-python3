# Nested If-statements
if (age > 30):
    if (gender == 'F'):
        print("Ma'am")
    else:
        print("Sir")

elif (age > 19):
    print("Dude")

elif (age > 10):
    if (gender == 'F'):
        print("Girl")
    else:
        print("Boy")

else:
    print("Child")