#GITHUB - iffysravioli 
#https://github.com/iffysravioli/unixgit
import sys 

string = input()
lst = []
cipher = int(input())
message = ""
num = 5 
count = 0
new_message = ""
string = str(string).upper()
for letter in range(0,len(string)):
  if 65 <= ord(string[letter]) <= 90:
    char = ord(string[letter]) + cipher
    if char > 90:
      char -= 26
    code = chr(char)
    message += code
for new_letter in range(0, len(message), num):
  lst.append(message[new_letter:new_letter + num])
for word in lst:
  new_message += word 
  new_message += " "
  count += 1
  if count == 10:
    new_message += "\n"
    count = 0 
print(new_message)
