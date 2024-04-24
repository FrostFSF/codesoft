import getpass, os
from packages import OTP as otp

def validateLogin(user):
    userName = input("Enter a username: ")
    passWord = getpass.getpass()
    err = ""

    if(userName != user["username"] and passWord != user["password"] or userName != user["username"] or passWord != user["password"]):
        if(userName != user["username"] and passWord != user["password"]):
            err = "username and password wrong!"
        elif(userName != user["username"]):
            err = "username wrong!"
        else:
            err = "password wrong!"
        return {"msg": False, "err": err}


    return {"msg": True}

def askPassword(user):
    askPass = getpass.getpass(prompt="Please enter password")
    confirmPass = getpass.getpass(prompt="Please confirm password")
    if(askPass == confirmPass):
        user["password"] = confirmPass
        print("****************************************")
        print("Password successfully reset!")
    else:
        while(askPass != confirmPass):
            print("")
            askPass = getpass.getpass(prompt="Please enter password")
            confirmPass = getpass.getpass(prompt="Please confirm password")
                
        user["password"] = confirmPass
        print("****************************************")
        print("Password successfully reset!")


def askForUserReset(user):
    userChoice = input("Do you want to reset the password? (y,n): ")
    if(userChoice == 'y'):
        generatedOtp = otp.generateOTP()
        otp.generateOTPFile(generatedOtp)

        print("****************************************")
        askOtp = input("Please enter your otp: ")

        if(askOtp == generatedOtp):
            otp.removeOTPFile()
            print("****************************************")
            askPassword(user)
        else:
            while(askOtp != generatedOtp):
                print("****************************************")
                print("Entered OTP is wrong!\n")
                askOtp = input("Please enter your otp: ")
            
            otp.removeOTPFile()
            print("")

            print("****************************************")
            askPassword(user)
    else:
        print("Thank you for your experience!")



def login_attempt(user):
    acknowledgement = validateLogin(user)
    attempt = 1
    
    while(not acknowledgement["msg"]):
        if(attempt > 3):
           print("Maximum attempt reached!")
           askForUserReset(user)
           return
        
        acknowledgement = validateLogin(user)
        attempt += 1
    
    print("\nLogin successful!")