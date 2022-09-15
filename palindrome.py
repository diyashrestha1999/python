list=123

def palindrome(val):
    
   
    if str(val)!=str(val)[::-1]:
        print("its is not palindrome number")
    else:
        print("it is palindrome")

palindrome(list)
