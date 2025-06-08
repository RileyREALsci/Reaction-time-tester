import json
import base64
import time


class Calls():


    def Encrypt():
        with open("click_data.txt", "r") as file: ## opening encrypted file.
            byte = file.read()
        de_b = str.encode(byte)
        de_b = base64.standard_b64encode(de_b)
        de_b = bytes.decode(de_b)
        file = open("click_data.txt", "w") # storing data
        file.write(de_b)
        file.close()

    def CallData(dataFile):
        f = open(dataFile, "r")
        data = f.read()
        data = str.encode(data)
        data = base64.standard_b64decode(data)
        data = bytes.decode(data)

        data = list(map(float, data.split()))
        
        return data
    
    def WriteData(dataFile,dataList): # Not tested
        """Updates user data when given a file and path refrence."""
        data = ' '.join(map(str, dataList))
        data = str(data) # converting it to a string.
        data = str.encode(data)
        data = base64.standard_b64encode(data)
        data = bytes.decode(data)        
        f = open(dataFile, "w")
        f.write(data)
    
        

#Calls.Encrypt()