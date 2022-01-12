import sys
password = input('Enter the password: ')
specialchars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digit = 0
smallalpha = 0
capitalalpha = 0
specialchar = 0
if(len(password) >= 6 and len(password) <= 16):
 for x in password:
  if(x.isdigit()):
   digit = digit+1
  if(x.islower()):
   smallalpha = smallalpha + 1
  if(x.isupper()):
   capitalalpha = capitalalpha + 1
  if(x in specialchars):
   specialchar = specialchar + 1
else:
 print('Password does not qualify.')
 sys.exit()
if(digit > 0 and smallalpha > 0 and capitalalpha > 0 and specialchar > 0):
 print('Password accepted.')
else:
 print('Password does not qualify.')