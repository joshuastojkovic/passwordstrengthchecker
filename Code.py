import string

password = input("what is your password?: ")


upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
length = len(password)
score = 0

if length > 8:
   score += 1
if length > 11:
   score += 1
if length > 15:
   score += 1
if length > 25:
   score += 1

if sum(characters) > 1:
   score += 1
if sum(characters) > 3:
   score += 1
if sum(characters) > 5:
   score += 1
if sum(characters) > 10:
   score += 1


print("your password is ranked at a level " + str(score))

if score <= 3:
   print("this is a weak password try adding some more special characters or uppercase characters")
if score >= 5:
   print("this is a very strong password congrats! adding even more special characters would make it impenetrable")
