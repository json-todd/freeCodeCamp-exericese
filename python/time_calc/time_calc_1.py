def add_time(start_time, duration, start_day = False):
    
    # data structures
    new_time = []
    
    start_time_format = start_time.split(" ") # [time, AM/PM]
    
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

    # Logic for conversion of minute to hour
    if new_time[1] >= 60:
        new_time[0] += 1
        new_time[1] -= 60
        
    return ":".join(new_time)
