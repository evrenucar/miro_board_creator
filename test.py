
### Username from Email Generator
# email_adress = "v94d6jm33t@xojxe.com"
# username = email_adress[:8]
# print (username) # AAAH8



# # email_adress = "v94d6jm33t@xojxe.com"
# # username = (email_adress[0:3])
# # print (username)



# import random  
# import string  
# def Upper_Lower_string(length): # define the function and pass the length as argument  
#     # Print the string in Lowercase  
#     result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length  
#     print(" Random string generated in Lowercase: ", result)  
  
#     # Print the string in Uppercase  
#     result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(length))) # run the loop until the define length  
#     print(" Random string generated in Uppercase: ", result1)  
  
# Upper_Lower_string(10) # define the length  


### Random Password Generator Code
import random   
import string  
import secrets  
num = 10 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
password = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
# Print the Secure string with the combination of ascii letters and digits  
print("Password:"+" "+password)  