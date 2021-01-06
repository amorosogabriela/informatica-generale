print("parole polindrome")
stri = input("scrivi una parola e scopri se è polindroma:\n")
stri2 = stri[::-1]
if stri == stri2:
    print("questa parola è polindroma")
else:
    print("questa parola non è polindroma")
