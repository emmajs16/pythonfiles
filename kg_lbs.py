# Emma Stoverink
# October 5, 2018

LBS_TO_KG = 2.2
print("Kilograms\t\t\tPounds")
kg = 1
while kg <= 199:
    pounds = kg * LBS_TO_KG
    print("{}\t\t\t{:.1f}".format(kg,pounds))
    kg+=2