def isPhoneNumber(text):
   if len(text) !=12:
       return False
   for i in range(0,3):
       if not text[i].isdecimal():
           return False
       else:
           return True
   if text[3] !='-':
       return false
   for i in range(4,7):
       if text[i].isdecimal():
           return False
   if text[7] !='-':
        return False
   for i in range(8,12):
       if not text[i].isdecimal():
           return False
       else:
           return True


print('Is 470-278-0851 a phone number?')
print(isPhoneNumber('123456789'))
print(isPhoneNumber('eenie meenie mini mo'))
print('Is Moshi moshi a phone number')
print(isPhoneNumber('4151961'))


