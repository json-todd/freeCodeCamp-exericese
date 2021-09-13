def add_time(start_time, duration, start_day = False):
    # Ver 2: Include logic for min-to-hour conversion, 12-h format conversion
    
    # data structures
    new_time = [] # [HH,MM]
    start_time_format = start_time.split(" ") # [time, AM/PM]
    new_time_day_night = start_time_format[1] # AM/PM
    
    def getTimeAndHour(time):
        """ Receive input as time format HH:MM
        return the hour and minute
        """
        time_arr = time.split(":")
        return time_arr[0], time_arr[1]
 
    start_hour_min = [int(t) for t in getTimeAndHour(start_time_format[0])]
    duration_hour_min = [int(t) for t in getTimeAndHour(duration)]

    for i in range(2):
        new_time.append(start_hour_min[i] + duration_hour_min[i])

    

    # Logic for 60-minute to hour conversion
    if new_time[1] > 60:
        new_time[1] -= 60
        new_time[0] += 1

    # Logic for AM/PM conversion
    def changeDayNight():
        if new_time_day_night == "AM": return "PM"
        elif new_time_day_night == "PM": return "AM"
  
    # Logic for hour conversion to 12-h format
    if new_time[0]  < 12: pass
    elif new_time[0] == 12: pass
    elif new_time[0] > 12: 
        
        twelve_h_period = new_time[0] / 12
        if (new_time[0] % 12 == 0): new_time[0] = 12
        else: new_time[0] = new_time[0] % 12

    new_time = [ str(x) for x in new_time ] # alt. map(lambda x: str(x), return_time)
    if len(new_time[1]) < 2: new_time[1] = "0" + new_time[1]

    new_time_output =  ":".join(new_time) + " " + new_time_day_night

    return new_time_output
