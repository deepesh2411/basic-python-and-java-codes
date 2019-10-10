def isPalindrome(s):
    rev=s[::-1]
    if(s==rev):
        return True
    else:
        return False
    
s=input("input a string: ")
ans=isPalindrome(s)
if(ans==1):
    print("yes")
else:
    print("No")
    
