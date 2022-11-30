def add_time(start_time, duration, start_day = None):
    # Ver 4: Final version; added day of the week after time calculation.
    
    # data structures
    new_time = []
    start_time_split = start_time.split(" ") # [time, AM/PM]
    week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    # new_time_day_night = start_time_format[1]

    def getTimeAndHour(time):
        """ Receive input as time format HH:MM
        return the hour and minute
        """
        time_arr = time.split(":")
        return time_arr[0], time_arr[1]
 
    start_hour_min = [int(t) for t in getTimeAndHour(start_time_split[0])]
    duration_hour_min = [int(t) for t in getTimeAndHour(duration)]

    # Convert start_time to 24-h format
    if start_time_split[1] == 'PM':  start_hour_min[0] += 12
    elif start_time_split[1] == 'AM' and start_hour_min[0] == 12: start_hour_min[0] = 0
    
    #  Add start_time with duration, assign results into new_time array
    for i in range(2):
        new_time.append(start_hour_min[i] + duration_hour_min[i])

    # Convert 60-minute into hour
    if new_time[1] >= 60:
        new_time[1] -= 60
        new_time[0] += 1

    # Convert new_time to 24-h format
    days = new_time[0] // 24
    new_time[0] %= 24
    
    # Deduce the AM/PM state
    if new_time[0] // 12 == 0:
        new_time_day_night = 'AM'
    else:
        new_time_day_night = 'PM'

    # Convert new_time to 12-h format
    new_time[0] %= 12
    if new_time[0] == 0: new_time[0] = 12

    # Return new_time output
    new_time = [ str(x) for x in new_time ] # alt. map(lambda x: str(x), return_time)
    if len(new_time[1]) < 2: new_time[1] = "0" + new_time[1]

    new_time_output =  ":".join(new_time) + " " + new_time_day_night 

    # if start_day argument, return the day of the week in output 
    if start_day:
        def convertDayFormat(day):
            day_out = ''
            day = day.lower()
            day_out = day[0].upper() + day[1:]    
            return day_out

        start_day = convertDayFormat(start_day)
        start_day_indx = week.index(start_day)
        end_day_indx = (start_day_indx + days ) % 7
        end_day = week[end_day_indx]

        new_time_output += f', {end_day}'

    if days == 1: 
        new_time_output += f" (next day)" 
    elif days > 1:
        new_time_output += f" ({days} days later)" 

    return new_time_output
