# Python function to check whether a passed string is a palindrome or not

def palindrome(s1):
    if s1[0:] == s1[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

s = input("Enter a string : ")
palindrome(s)
