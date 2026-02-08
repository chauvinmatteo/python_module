def ft_water_reminder():
    day_water = int(input("Days since last watering: "))
    if day_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
