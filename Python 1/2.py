print(" *** Wind classification ***")
wind = float(input("Enter wind speed (km/h) : "))
print("Wind classification is ", end="")
if(wind >= 0 and wind < 52):
    print("Breeze.")
elif(wind >= 52 and wind < 56):
    print("Depression.")
elif(wind >= 56 and wind < 102):
    print("Tropical Storm.")
elif(wind >= 102 and wind < 209):
    print("Typhoon.")
else:
    print("Super Typhoon.")