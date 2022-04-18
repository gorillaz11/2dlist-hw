from calendar import day_abbr


april_temps=[
[None, None, None, None, 4.0, 3.0, 2.0],
[8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0],
[2.0, 7.0, 6.0, 2.0, 4.0, 2.0, 3.0],
[8.0, 2.0, 6.0, 5.0, 10.0, 3.0, 2.0],
[8.0, 7.0, 6.0, 2.0, 3.0, 3.0, 2.0],


]
start_week =input("start time(week): ")
start_time_week = int( start_week[0:2])


day=0


print(f"today temperature{april_temps[start_time_week][day]:7.2}C")
print("forecast for the entire week:")
for day_index in range(7):
    print(f"t{april_temps[start_time_week][day_index]:7.2}C")