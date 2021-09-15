def add_time(start_time, duration, start_day = False):
    """ Ver 3: Add logic to convert new_time to  12-h format with AM/PM state
    """
    # Data structures
    new_time = []
    start_time_split = start_time.split(" ") # [time, AM/PM]
    
    def getTimeAndHour(time):
        """ Receive input as time format HH:MM
        return the hour and minute
        """
        time_arr = time.split(":")
        return time_arr[0], time_arr[1]
 
    start_hour_min = [int(t) for t in getTimeAndHour(start_time_split[0])]
    duration_hour_min = [int(t) for t in getTimeAndHour(duration)]

    # Convert to 24-h format
    if start_time_split[1] == 'PM':  start_hour_min[0] += 12
    elif start_time_split[1] == 'AM' and start_hour_min[0] == 12: start_hour_min[0] = 0

    # Add start_time with duration, assign results into new_time array
    for i in range(2):
        new_time.append(start_hour_min[i] + duration_hour_min[i])
    
    # Convert 60-min to hour
    if new_time[1] >= 60:
        new_time[1] -= 60
        new_time[0] += 1
    
    # Convert new_time to 24-h format
    days = new_time[0] // 24
    new_time[0] %= 24
    
    # Deduce the day or night state
    if new_time[0] // 12 == 0:
        new_time_day_night = 'AM'
    else:
        new_time_day_night = 'PM'

    # Convert new_time to 12-h format
    new_time[0] %= 12
    if new_time[0] == 0: new_time[0] = 12

    # Return new_time as output
    new_time = [ str(x) for x in new_time ] # alt. map(lambda x: str(x), return_time)
    if len(new_time[1]) < 2: new_time[1] = "0" + new_time[1]

    new_time_output =  ":".join(new_time) + " " + new_time_day_night 
    if days == 1: 
        new_time_output += f" (next day)" 
    elif days > 1:
        new_time_output += f" ({days} days later)" 

    return new_time_output
