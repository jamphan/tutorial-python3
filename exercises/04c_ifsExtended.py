# ==================================================================================================
"""
Ex. 04b

Summary:
    - We determine what to call someone based on their age and gender

Explaination:
    - Line ##: This is an alternative way of "declaring" variables; languages often
      provide multiple ways of declaring variables.


"""
# ==================================================================================================

age, gender = 25, "M"

if (age > 30 and gender == 'F'):
    print("Ma'am")
elif (age > 30 and gender == 'M'):
    print("Sir")
elif (age > 19):
    print("Dude")
elif (age > 10 and gender == 'F'):
    print("Girl")
elif (age > 10 and gender == 'M'):
    print("Boy")
else:
    print("Child")