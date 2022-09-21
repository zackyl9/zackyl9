#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#get the string of word randomly
password = []
for ran_word in range(1,nr_letters+1):
  ran_word = random.choice(letters)
  password.append(ran_word) #run the loop add in the random word in the pass list


#get the string of symbol randomly
for ran_sym in range(1,nr_symbols+1):
  ran_sym = random.choice(symbols)
  password.append(ran_sym ) #run the loop add in the random symbol in the list


#get the string of number randomly
for ran_int in range(1, nr_numbers+1):
  ran_int = random.choice(numbers)
  password.append(ran_int) #run the loop add in the random number in the list

#shuffle the list
#final_pass_List = random.sample(password, len(password)) #reorder the list by sample function
final_passList = random.shuffle(password)

#join the list becoming a long string
#print(''.join(final_pass)) #join the list to string by join function

#Method 2 to join list to string
final_pass = ""
for char in password:
    final_pass += char

print(f"Your password is {final_pass}")