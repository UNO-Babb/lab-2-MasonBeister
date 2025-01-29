#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = (now.minute - 15) % 60

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours)

  futureHour = currentHour + hours 
  futureHour = futureHour % 24
  print(futureHour)
  #Ask user for minutes
  minutes = input("Enter minutes: ")
  minutes = int(minutes)

  #Output the future time in standard format "HH:MM"

  futureMinute = currentMinute + minutes
  furtureMinute = futureMinute % 60
  strHour = str(futureHour)
  strMinute = str(futureMinute)

  if futureMinute < 10:
    strMinute = "0" + strMinute
  print(strHour + ":" + strMinute)
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculatin
if __name__ == '__main__':
  main()
