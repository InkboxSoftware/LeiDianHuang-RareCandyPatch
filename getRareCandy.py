inputFilePath = 'game.sav'
outputFilePath = 'game2.sav'

def readModifyBinFile(inputFilePath, outputFilePath):
    try:
        with open(inputFilePath, 'rb') as inputFile:
            data = bytearray(inputFile.read())
        
        #increase rare candy
        data[0x0CE1] = 255  #number of rare candies


        #calculate checksum
        checksum = 0
        c = 0   #carry bit
        for i in range(0x0C00, 0x1600):
            checksum = checksum + data[i] + c
            c = 0
            if (checksum > 255):
                checksum = checksum & 255
                c = 1
        for i in range(0x1C00, 0x1C10):
            checksum = checksum + data[i]
            c = 0
            if (checksum > 255):
                checksum = checksum & 255
                c = 1
        checksum = checksum & 255
        oldchecksum = data[0x1C20]
        data[0x1C20] = checksum

        with open(outputFilePath, 'wb') as outputFile:
            outputFile.write(data)

        print(f"File saved as {outputFilePath}")
    except IOError as e:
        print(f"Error occurred: {e}")

readModifyBinFile(inputFilePath, outputFilePath)
