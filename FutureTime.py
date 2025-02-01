#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour 
  currentMinute = now.minute

  print(f"Current Time: {currentHour:02}:{currentMinute:02}") #Display current time for checking

  #TODO:
  #Ask user for hours and mintues
  hours = int(input("Enter mintues to add: "))
  mins = int(input("Enter mintues to add:"))

  
   #Ask user for minutes
  Mins = int(input("Enter mintues to add:"))

  #Calculate the time after the user-supplied time has passed.
  totalMintues = currentMinute + mins
  futureHour = (currentHour + hours + (currentMinute + min) // 60) % 24
  futureMinute = (currentMinute + min) % 60

  #Do not use any if statements in calculating the time.
  

  #Output the future time in standard format "HH:MM"
print(f"Future Time: {:02}:{futureHour:02}:{futureMintues:02}")

if __name__ == '__main__':
  main()
