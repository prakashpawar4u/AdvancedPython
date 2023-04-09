# def checkPal(st):
#     l = len(st)

#     if l<2:
#         return True
    
#     elif st[0]==st[l-1]:
#         return checkPal(st[1: 1-1])
    
#     else:
#         return False
# Inp = "abbfuckbba"
# print(checkPal(Inp))



def isPalindrome(s):
  
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
  
    # if length is less than 2
    if l < 2:
        return True
  
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
  
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
  
    else:
        return False
  
# Driver Code
s = "MalaYuckaLam"
ans = isPalindrome(s)
  
if ans:
    print("Yes")
  
else:
    print("No")