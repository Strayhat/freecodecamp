def add_time(start, duration, day_of_week=None):
    # Maintaining Days in a week
    day_map = {
      "Saturday": 0,
      "Sunday": 1,
      "Monday": 2,
      "Tuesday": 3,
      "Wednesday": 4,
      "Thursday": 5,
      "Friday": 6
    }
    #split the start time with hours minutes and AM/PM
    starter= start.split(" ")
    if len(starter) != 2:
      return "Invalid start time format"
    alpha_hours, alpha_minutes = map(int, starter[0].split(':'))
    alpha_am_pm= starter[1]

    #military time
    if alpha_am_pm == "PM":
      alpha_hours += 12

    #split duration into hours and minutes
    bravo_hours, bravo_minutes = map(int, duration.split(':'))
    
    #start and duration hours combined 
    op_minutes = alpha_minutes + bravo_minutes
    op_hours = alpha_hours + bravo_hours

    #remainder of 60 min 
    if op_minutes > 60:
        op_minutes %= 60
        op_hours += 1
    #Timezone indicator
    alpha_am_pm = "AM"

    #make my day
    day = op_hours // 24
    if op_hours > 24:
        op_hours %= 24

    # AM<-->PM switch
    if op_hours > 12:
        op_hours %= 12
        alpha_am_pm = "PM"

    if op_hours == 12:
        alpha_am_pm = "PM"

    if op_hours == 0:
        op_hours = 12
        alpha_am_pm = "AM"

    #return the time 
    if day_of_week is None:
      if day == 0:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm}"
      elif day == 1:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm} (next day)"
      else:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm} ({day} days later)"
    else:
      #weekday calculator
      index = (day_map[day_of_week.lower().capitalize()] + day) % 7
      for weekday, number_days in day_map.items():
        if number_days == index:
          index = weekday
         
          break
      if day == 0:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm}, {index}"
      elif day == 1:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm}, {index} (next day)"
      else:
        return f"{op_hours}:{op_minutes:02d} {alpha_am_pm}, {index} ({day} days later)"



print(add_time("3:30 PM", "2:12", "Thursday"))  # Output: "5:42 PM, Thursday"
print(add_time("11:55 AM", "3:12"))  # Output: "3:07 PM"
print(add_time("9:15 PM", "5:30"))  # Output: "2:45 AM (next day)"
print(add_time("11:40 AM", "0:25"))  # Output: "12:05 PM""
print(add_time("2:59 AM", "24:05", "Monday"))  # Output: "2:59 AM (next day)"
print(add_time("5:01 PM", "0:00"))  # Output: "5:01 AM"
print(add_time("3:30 PM", "2:12", "Monday"))  # Output: "5:42 PM, Monday""
print(add_time("2:59 AM", "24:00"))  # Output: "2:59 AM, Sunday (next day)"
print(add_time("11:59 PM", "24:05", "Monday"))  # Output: "12:04 AM, Wednesday (2 days later)"
print(add_time("8:16 PM", "466:02")) # Output: "6:18 AM, (20 days later)"

