#Create a program that takes in a string input and returns “Trick” if the input has the word “trick” in it or returns “Treat”. View the attached image for more information on sample test cases.

#user input
userInput = input("Enter your message: ")

#testing for character length with len and if else statments
inputCharacters = len(userInput)

if (inputCharacters < 1):
  print("Too short! The message must be in between 1 and 20 characters")
  userInput = input("Re-enter your message: ")
  
elif (inputCharacters > 20):
  print("Too long! The message must be in between 1 and 20 characters")
  userInput = input("Re-enter your message: ")

#testing to find if trick is in the word and prints corresponding output
if userInput.find("trick") != -1:
  print("Trick")
  
elif userInput.find("trick") == -1:
  print("Treat")

