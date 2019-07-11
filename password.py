# intro 
print("This is a program to help you generate a secure passcode.")

email = input("What is your email address?")

petname = input("What is your pet?")

team = input("What your favorite sports team?")

birthyear = input("What year were you born in?")

age = input("How old are you?")

food = input("What is your favorite food?")

street = input("What street did you grow up on?")

firstname = input("What is you first name?")

lastname = input("What is your last name?")

#slice out username 
user = email[email.index(""):email.index("@")]

#slice out domain

domain = email[email.index("@")+1::1]

#format message

#format message
message = """Username:{}
Domain:{}"""
passwordmessage = """Possible passwords:
pass1 - {}{}
pass2 - {}{}
pass3 - {}{}
pass4 - {}{}
Pass5 - {}{}"""

#display message output

output = message.format(user,domain)
print(output)
passwordoutput = passwordmessage.format(petname,birthyear,team,age,lastname,firstname,team,petname,food,street)
print(passwordoutput)
