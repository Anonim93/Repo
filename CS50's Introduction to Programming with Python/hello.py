# Ask user for their name
name = input("What is your name?").strip().title()  # = sign means assignment in python 
#.strip() removes white spaces from left and right of the str.
#.title() capitalize the first letter of the str

#Split user's name into first and last name
first , last  = name.split()


#Say hello to user
print (f"Hello, {first} {last}" ) # f before ""  means a special format string





