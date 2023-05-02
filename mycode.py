#GITHUB - iffysravioli 
#https://github.com/iffysravioli/unixgit

import sys 

string = sys.stdin
lst = []
cipher = sys.stdin
message = ""
num = 5 
count = 0
new_message = ""
string = string.upper()
for letter in range(0,len(string)):
  if 65 <= ord(string(letter)) <= 90:
    char = ord(string(letter)) + cipher
    if char > 90:
      char -= 26
      code = chr(char)
      message += code
for new_letter in range(0, len(message), num):
  lst.append(message[new_letter + num ])
for word in lst:
  new_message += word 
  new_message += " "
  count += 1
  if count == 10:
    new_letter += "\n"
    count = 0 
  print(new_message)
