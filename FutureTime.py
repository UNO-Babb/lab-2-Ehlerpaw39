#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 16
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours:")
  hours = int(hours) #change from text to number 

  futurehour = currentHour + hours
  futurehour = futurehour % 24
  print(futurehour)

  

   #Ask user for minutes
  Mins = input ("Enter mintues")

  #Calculate the time after the user-supplied time has passed.
  futureHour = (currentHour + hours + (currentMinute + min) // 60) % 24
  futureMinute = (currentMinute + min) % 60

  #Do not use any if statements in calculating the time.
  

  #Output the future time in standard format "HH:MM"
print(f"future Time: {futureHour:02} {futureMintues + min}")

if __name__ == '__main__':
  main()
