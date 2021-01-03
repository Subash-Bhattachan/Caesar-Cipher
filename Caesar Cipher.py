# Project 1
# Subash Bhattachan
# Program that figures out encoding and decoding
# October 11, 2016




while True:
  print("Press 'e' to encode, 'd' to decode, or 'q' to quit this program.")
  
  answer = input()
  if answer.isalpha():
    answer= str(answer.lower())
    break
  else:
      print("Invalid Entry. Try again.")

      
      
########################################################################

while answer !="q":
  if answer == "e":
    while True:
      print("So write a word or a sentence you like to encode?")
      text = input()
      if text.isalpha():
        text= str(text.lower())
        break
      else:
          print("Invalid Entry. Try again.")

    while True:
      print("Choose from 1 through 25 for the rotation number:")
      rotation = input()
      if rotation.isdigit():
        rotation = int(rotation)
        break
   
      else:
         print("That is not an option! Try again.")
           
  
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
  
    cipher = " "

    for c in text:
      if c in alphabet:
        cipher = cipher + alphabet[(alphabet.index(c) + rotation) % 26] 

    print("Okay, your encoded text is" + cipher + "." )  
    print("\n")
    
    print("Press 'e' to encode, 'd' to decode, or 'q' to quit this program.")
    answer = input()
        
    
########################################################################   
       
  if answer == "d":
    
      print("So write a word or a sentence you like to decode?")
      text = input()

      print("What plaintext word is in the code?")
      pltext = str(input())

      alphabet = "abcdefghijklmnopqrstuvwxyz"

      cipher = " "

      for i in range(1, 27):
  
        while(i):
           for c in text:
             if c in alphabet:
                cipher +=  alphabet[(alphabet.index(c) - i) % 26]         
  
           print("Shift of " + str(i) + ":",  cipher)
           break
    
        if (pltext in cipher):
          print("    Voila! the shift is at " + str(i) + ".")
          break
        else:
          print("    Too bad, no shift exists here!")
    
          cipher = " "
  
  print("\n")
  print("Press 'e' to encode, 'd' to decode, or 'q' to quit this program.")
  answer = input()
 
  
  

else:
  print("Thank you!! GO AWAY!")
    
    
