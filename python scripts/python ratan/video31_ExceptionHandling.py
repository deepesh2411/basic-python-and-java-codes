try:
    print("deepesh")
    print(10/0)
    print("ranjan")

except ZeroDivisionError as e:
    print("rest of the app")

#ex-2

try:
    print("deepesh")
    print(10/0)
    print("ranjan")

except TypeError as e:   #for the except block is not matched then error occured
    print("rest of the app")

#ex-3
try:
    print("deepesh")
    print("ranjan")

except ZeroDivisionError as e:   #except blocks are not checked as no exception
    print("rest of the app")

print("rest of the app new")
    

#ex-4 only try blocks are not allowed

#ex-5 invalid, inbetwwen try and except statement other decleration are not allowed

#ex-6 whenever exception raised in try block the rest of the app in try will not execute

