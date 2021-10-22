weight = input("what is your weight?\n")
lbs_or_kg = input("k for kg, L for lbs\n")
lbs_or_kg = lbs_or_kg.lower()
weight = float(weight)
if lbs_or_kg == "k" or lbs_or_kg == "kg":
    print("{} lbs".format(weight/0.45))

elif lbs_or_kg == "l" or lbs_or_kg == "lbs":
    print("{} kg".format(weight*0.45))

else:
    print("that is wrong please enter l or k")
