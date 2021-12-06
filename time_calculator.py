def add_time(start, duration, day=''):
# to check if 'day' arg is passed 
 if len(day) > 0:
    day=day.title()
    week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    dayindex= week.index(day)  

    

# Split input into current/duration hour and minute
 cur_split=start.split()
 dur_split=duration.split()
 
 cur_meridiem=cur_split[1]

 cur_hour=int(cur_split[0].split(":")[0])
 cur_min =int(cur_split[0].split(":")[1])
 
 dur_hour= int(dur_split[0].split(":")[0])
 dur_min = int(dur_split[0].split(":")[1])
 
 new_meridiem = cur_meridiem
 days_passed = 0
 new_hour =  cur_hour + dur_hour
 new_min = cur_min + dur_min 

#time calculation
 while (new_hour >= 0):
     
     if new_hour >=24 :
        days_passed = new_hour//24
        new_hour = new_hour % 24
         
     #if 12 or more hours are added, PM changes to AM and vice versa but day count increases in the former
     elif new_hour < 24 and new_hour > 12 :
        new_hour = new_hour % 12
        if cur_meridiem == "PM":
           days_passed += 1
           new_meridiem = "AM" 

     else :
        # to add the minutes after hours have been calculated 
        new_min = cur_min + dur_min
       
        if new_min >= 60:
           new_min = new_min % 60
           new_hour += 1
          
           if cur_meridiem=="PM":
              days_passed += 1
              new_meridiem = "AM" 
             
           else : 
              new_meridiem = "PM" 
        break

# Formatting output
 min = str(new_min) if new_min >=10 else "0" + str(new_min)  
 hour = str(new_hour)

# Matching conditions as compared to the args passed
 if days_passed == 0  and len(day)>0:
    time_and_day = hour + ":" + min + ' ' + new_meridiem + ',' + " " + "Monday"
    return(time_and_day)

 elif days_passed == 0 :
    time_and_day = hour + ":" + min + ' ' + new_meridiem 
    return(time_and_day)

 elif days_passed == 1 and len(day)>0:
    time_and_day = hour + ":" + min + ' ' + new_meridiem + "," + " " + week[((days_passed + dayindex)%7)] + " " + "(next day)" 
    return(time_and_day)   

 elif days_passed == 1:
    time_and_day = hour + ":" + min + ' ' + new_meridiem + " " + "(next day)" 
    return(time_and_day)

 elif days_passed > 1 and len(day)>0: 
    time_and_day = hour + ":" + min + ' ' + new_meridiem + ',' + " " + week[((days_passed + dayindex)%7)] + " " + f"({days_passed} days later)"
    return(time_and_day)

 else :
    time_and_day = hour + ":" + min + ' ' + new_meridiem  + " " + f"({days_passed} days later)"
    return(time_and_day)