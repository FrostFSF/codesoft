from random import randint
randomChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','@','#','$','%','&']

def generatePassword(ofLength = 10) -> str:
    randomPassword = ''
    for i in range(0,ofLength):
        randomPassword += randomChar[randint(0,len(randomChar) - 1)]
    return randomPassword

length = int(input("Enter how long the password should be: "))

print(generatePassword(ofLength=length))
