"""
 Create a python file named KgToPounds, write a program that can convert kg to pounds
            Hints: 1 kg = 2.2 pounds

            Ex:
                Given data:
                    kg = 100

                output:
                    100 kg is equal to 220 pounds
"""
kg = 100
pounds = kg * 2.2

print(str(kg) + ' kg is equal to ' + str(pounds) + ' pounds')
print(f"{kg} kg is equal to {pounds:.2f} pounds")