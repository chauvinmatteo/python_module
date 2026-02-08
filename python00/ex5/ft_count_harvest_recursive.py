def ft_count_harvest_recursive():
    harvest_day = int(input("Days until harvest: "))

    def days_passed(current_day, harvest_day):
        if current_day > harvest_day:
            return
        print("Day ", current_day)
        days_passed(current_day + 1, harvest_day)
    days_passed(1, harvest_day)
    print("Harvest time!")
