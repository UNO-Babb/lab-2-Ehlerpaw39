#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answer = ["yes", "yes-definetely", "No", "Very Doubtful", "Ask Again later", "cannot Predict Now", "It is certain",
            "Most likely", "I say no","outlook good", "outlook bad", "Not so sure",
            "it is certain", "it is not certain", "you may rely on it", "you may not like it"]
  #Answer question randomly with one of the options from your earlier list.
  question = input("Ask a question:")
  num = random. random()
  num = num * 1000
  num = int(num)
  num = num % 15
  print(answer[num])
  #print(answer[16])

  response = random. choice(answer)
  print(response)
  print(random. choice(answer))
  


if __name__ == '__main__':
  main()
