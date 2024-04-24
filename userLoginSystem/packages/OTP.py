import random, os, re

def generateOTP():
    otp = ""
    for i in range(5):
        otp += str(random.randint(0,9))
    return otp

def generateOTPFile(otp):
    filePath = 'userLoginSystem\OTP'

    for filename in os.listdir(filePath):
        if(re.match(r'otp-\d+\.txt', filename)):
            currentOTPNumber = re.search(r'\d+',filename).group()

            newOTPFileName = filename.replace(currentOTPNumber, otp)
            
            sourcePath = os.path.join(filePath,filename)
            dstPath = os.path.join(filePath,newOTPFileName)

            try:
                os.rename(sourcePath,dstPath)
                file = open(dstPath,'w')
                file.write(f"Your One Time OTP is: {otp}\n\nThanks for using OTP-Xpress!!")
                file.close()
                return

            except OSError as e:
                print(e)

    file = open(f"{filePath}\otp-{otp}.txt","w")
    file.write(f"Your One Time OTP is: {otp}\n\nThanks for using OTP-Xpress!!")
    file.close()

def removeOTPFile():
    filePath = 'userLoginSystem\OTP'

    for filename in os.listdir(filePath):
        if(re.match(r"otp-\d+\.txt", filename)):
            deletingFilePath = os.path.join(filePath,filename)
            try:
                os.remove(deletingFilePath)
            except OSError as e:
                print(e)
