import discord, os
import time
import pathlib
from datetime import datetime




print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("                                                                         █")
                                                                     

print("   ▄█    █▄       ▄████████ ███▄▄▄▄       ███     ▄██   ▄      ▄████████ █")
print("  ███    ███     ███    ███ ███▀▀▀██▄ ▀█████████▄ ███   ██▄   ███    ███ █")
print("  ███    ███     ███    █▀  ███   ███    ▀███▀▀██ ███▄▄▄███   ███    █▀  █")
print(" ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███   ███     ███   ▀ ▀▀▀▀▀▀███  ▄███▄▄▄     █")
print("▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███   ███     ███     ▄██   ███ ▀▀███▀▀▀     █")
print("  ███    ███     ███    █▄  ███   ███     ███     ███   ███   ███    █▄  █")
print("  ███    ███     ███    ███ ███   ███     ███     ███   ███   ███    ███ █")
print("  ███    █▀      ██████████  ▀█   █▀     ▄████▀    ▀█████▀    ██████████ █") 
                                                                               

                                                                                                                                       
print("                                                                         █")
print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
print("█")

newToken = False

if newToken == False:
    config = open("token.txt","r")
    token = (config.read())
    config.close()
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")    
    print("  " + token + " █")
    print("                                           ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("  Would you like to change this token? Y/N █")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("█")
    tokenChange = input("█ ")
    if tokenChange == "N" or tokenChange == "n" or tokenChange == "no" or tokenChange == "No":
        pass
    elif tokenChange == "Y" or tokenChange == "y" or tokenChange == "yes" or tokenChange == "Yes":
        newToken = True
    
if newToken == True:
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("  What is your bot token? █")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("█")
    token = input("█ ")
    if len(token) == 59:
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("    Bot token accepted!   █")
        print("                          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("  " + token + " █")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("█")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("  Would you like to save this token? Y/N █")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("█")
        saveTokenChoice = input("█ ")
        if saveTokenChoice == "N" or saveTokenChoice == "n" or saveTokenChoice == "no" or saveTokenChoice == "No":
            pass
        elif saveTokenChoice == "Y" or saveTokenChoice == "y" or saveTokenChoice == "yes" or saveTokenChoice == "Yes":
            f = open("token.txt", "w")
            f.write(token)
            f.close()
    else:
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("  Bot token denied. Quitting █")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        time.sleep(2)
        quit()




client = discord.Client()
fileList = os.listdir('images/')
totalFiles = len(fileList)
totalSize = 0

#print(totalFiles)

############

def clearScreen():
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█")
    print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("                                                                         █")
    print("   ▄█    █▄       ▄████████ ███▄▄▄▄       ███     ▄██   ▄      ▄████████ █")
    print("  ███    ███     ███    ███ ███▀▀▀██▄ ▀█████████▄ ███   ██▄   ███    ███ █")
    print("  ███    ███     ███    █▀  ███   ███    ▀███▀▀██ ███▄▄▄███   ███    █▀  █")
    print(" ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███   ███     ███   ▀ ▀▀▀▀▀▀███  ▄███▄▄▄     █")
    print("▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███   ███     ███     ▄██   ███ ▀▀███▀▀▀     █")
    print("  ███    ███     ███    █▄  ███   ███     ███     ███   ███   ███    █▄  █")
    print("  ███    ███     ███    ███ ███   ███     ███     ███   ███   ███    ███ █")
    print("  ███    █▀      ██████████  ▀█   █▀     ▄████▀    ▀█████▀    ██████████ █")                                                                                                                                
    print("                                                                         █")
    print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("█")
############

#clearScreen()

#print(fileList)
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("  Would you like to prune the files? █")
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print("█")
prune = input("█ ")
if prune == "Y" or prune == "y" or prune == "yes" or prune == "Yes":
    print("█")
    for i in range(0,totalFiles):
        if os.path.getsize('images/' + fileList[i]) > 8000000 or os.path.getsize('images/' + fileList[i]) == 0:
            print("█ Found: " + fileList[i])
            os.remove('images/' + fileList[i])
else:
    pass

fileList = os.listdir('images/')
totalFiles = len(fileList)

#fileList = os.listdir('images/')
#totalFiles = len(fileList)

for i in range(0, totalFiles):
    totalSize += os.path.getsize('images/' + fileList[i])

if totalSize >= 1000000000:
    totalSize = str(str(totalSize/1000000000) + "GB")
elif totalSize >= 1000000 and totalSize < 1000000000:
    totalSize = str(str(totalSize/1000000) + "MB")
elif totalSize < 1000000:
    totalSize = str(str(totalSize/1000) + "KB")

if len(str(totalFiles) + " Files") > len(str(totalSize)):
    tempSizeVar = len(totalFiles)
else:
    tempSizeVar = len(str(totalSize))

print("█ ")
print("█▀" + tempSizeVar * "-" + "▀")
print("█ " + str(totalFiles) + " Files" )
print("█ " + totalSize )
print("█▄" + tempSizeVar * "-" + "▄")


print("█")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("  Would you like to rename the files? █")
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print("█")
rename = input("█ ")
if rename == "Y" or rename == "y" or rename == "yes" or rename == "Yes":
    for i in range(0,totalFiles):
        fileExtension = pathlib.Path('images/' + fileList[i]).suffix
        #print("File Extension: ", file_extension)
        source = 'images/' + fileList[i]
        j = i + 1
        numOfDigits = len(str(j))
        numOfZeros = 5 - numOfDigits
        os.rename('images/' + fileList[i], 'images/' + (numOfZeros * '0') + str(j) + fileExtension)
else:
    pass

fileList = os.listdir('images/')
totalFiles = len(fileList)

totalSize = 0

for i in range(0, totalFiles):
    totalSize += os.path.getsize('images/' + fileList[i])

if totalSize >= 1000000000:
    totalSize = str(str(totalSize/1000000000) + "GB")
elif totalSize >= 1000000 and totalSize < 1000000000:
    totalSize = str(str(totalSize/1000000) + "MB")
elif totalSize < 1000000:
    totalSize = str(str(totalSize/1000) + "KB")

print("█")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("  Ready to upload ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("  Please type \"give img\" in the channel you'd like to upload to.   █")
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print("█")









#tempTotalSize = 0






startTime = time.time()
def tic():
    global startTime
    startTime = time.time()

def toc():
    tSec = round(time.time() - startTime)
    (tMin, tSec) = divmod(tSec,60)
    (tHour, tMin) = divmod(tMin,60)
    print('█ ')
    print("█▀-------------------------------▀")
    print('█ Time passed: {}hours:{}min:{}sec'.format(tHour,tMin,tSec))
    print("█▄-------------------------------▄")

toc2var = ""

#def toc2(toc2var):

#    return toc2var

@client.event
async def on_ready():
    print('█ logged in as {0.user}'.format(client))

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('2hello'):
#        print("hello found")
#        await message.channel.send('Hello!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('give img'):
        tic()
        toc()
        print("█ Sending " + str(totalFiles) + " images.")
        for i in range (0,len(fileList)):
            await message.channel.send(file=discord.File('images/' + fileList[i]))
            print("█ " + str(i + 1) + " / " + str(totalFiles) + " | " + str(((i + 1) / totalFiles)*100) + "%")
        toc()
        tSec2 = round(time.time() - startTime)
        (tMin2, tSec2) = divmod(tSec2,60)
        (tHour2, tMin2) = divmod(tMin2,60)
        toc2var = ('Took: {}hours:{}min:{}sec'.format(tHour2,tMin2,tSec2))

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y at %H:%M:%S")

        
        logSave = open("log.txt", "a")  # append mode
        logSave.write("Uploaded " + str(totalFiles) + " files. \n")
        logSave.write("Which is " + totalSize + "\n")
        logSave.write(toc2var + "\n")
        logSave.write("Upload finished on "  + dt_string + "\n")
        logSave.write("----------\n")
        logSave.close()

        print("█")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("  Would you like to delete the files? █")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("█")
        delete = input("█ ")
        if delete == "Y" or delete == "y" or delete == "yes" or delete == "Yes":
            for i in range (0,len(fileList)):
                os.remove('images/' + fileList[i])



client.run(token)






























