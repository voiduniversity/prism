import customtkinter as ctk
import tkinter as tk
from PIL import Image
import os

currentDir = os.getcwd()

python = f"{currentDir}/dependencies/pythonMediumFile.txt"
score = f"{currentDir}/dependencies/scoring.txt"
pythonCodeLines = []
pyhtonExample = ""
timer = 61
elapsed = 0
elapsedTime = f"{currentDir}/dependencies/elapsedTime.txt"
codecount = f"{currentDir}/dependencies/counted.txt"
diff = f"{currentDir}/dependencies/recentDifficulty.txt"

# Load Python Code Lines & Return the string
def mediumPython():
    global pythonExample

    with open(python) as pythonFile:
        for line in pythonFile:
            # Append each line to a list & join them together
            pythonCodeLines.append(line.strip())
            exampleJoined = "".join(pythonCodeLines)
            
            # Get rid of additional whitespaces between words
            splitExample = exampleJoined.split(" ")
            example = "".join(splitExample)

            pythonExample = example
    

def mediumFrame(root):
    
    codingFont = ctk.CTkFont(family="JetBrains Mono NL", 
                    size=16, 
                    weight="normal", # weight bold/normal
                    slant="roman", # slant roman/italic
                    )

    # Loop - > codeNums will have 15 numbers individually that will be used to
    # output the numbers on new lines to represent an IDE look
    codeNums = []
    for num in range(18):
        codeNums.append(str(num + 1))

    IDEnums = "\n".join(codeNums)

    # Submit the code -> Saves the users coåde with no whitelines or spaces
    # then gets saved locally within rightandwrong.txt
    def submitCode():
        global timer
        timer = 0
        timerLabel.configure(text=60)
        userInput.configure(state="disabled")
        submitButton.configure(state="disabled")
        startButton.configure(state="normmal")


        userCode = userInput.get(0.0, "end")
        splitNewLine = userCode.split("\n")
        joinedCode = "".join(splitNewLine)
        splitSpace = joinedCode.split()
        final = "".join(splitSpace)


        # Track right & wrong with the help of claude
        i = 0
        j = 0
        rightChars = 0
        currentCode = list(final)
        codingExample = list(pythonExample)
        # loop through if i is less than the length of user input and if j is less than the coding example
        while i < len(currentCode) and j < len(codingExample):
            # if both are the same
            if currentCode[i] == codingExample[j]:
                rightChars += 1
                i += 1
                j += 1
                continue
            else:
                # Inserion // if i+1 is not the last char and i+1 is the same as j's current index
                if i + 1 < len(currentCode) and currentCode[i + 1] == codingExample[j]:
                    i += 1
                    continue
                # Deletion // if j+1 is not the last char and j+1 is the same as i's current index
                elif j + 1 < len(codingExample) and currentCode[i] == codingExample[j + 1]:
                    j += 1
                    continue
                # Subtitution // if user missed a character
                else:
                    i += 1
                    j += 1
                    continue
                
                
        
        with open(score, "w") as scoreFile:
            print("Debugging: Executed")
            scoreFile.write(f"{rightChars}")

        with open(elapsedTime, "w") as timeTaken:
            print("Debugging: Executed")
            timeTaken.write(str(elapsed))
        
        with open(diff, "w") as diffiulty:
            diffiulty.write("Medium")

        with open(codecount, "w") as counting:
            counting.write(str(len(pythonExample)))

    def timerFunc():
        global timer, elapsed
        userInput.configure(state="normal")
        startButton.configure(state="disabled")
        submitButton.configure(state="normal")

        if timer != 0:
            elapsed += 1
            timer -=1
            timerLabel.configure(text=timer)
            root.after(1000, timerFunc)
        else:
            submitCode()

    def resetTimer():
        global timer, elapsed
        timer = 61
        elapsed = 0
        timerFunc()
            


    # Frames
    backgroundFrame = ctk.CTkFrame(root, fg_color="#121212", width=1280, height=720)
    codeFrame = ctk.CTkFrame(backgroundFrame, fg_color="#232323", width=527, height=400, corner_radius=15)
    userFrame = ctk.CTkFrame(backgroundFrame, fg_color="#232323", width=527, height=400, corner_radius=15)

    # codeFrame
    ideFrameOne = ctk.CTkFrame(codeFrame, fg_color="#232323", width=38, height=400, corner_radius=0)
    separator1 = ctk.CTkFrame(codeFrame, fg_color="#353535", width=1, height=373)

    # Hard coded label output
    lineOne = ctk.CTkLabel(codeFrame, text=pythonCodeLines[0], font=codingFont, text_color="#636363")
    lineTwo = ctk.CTkLabel(codeFrame, text=pythonCodeLines[1], font=codingFont, text_color="#636363")
    lineThree = ctk.CTkLabel(codeFrame, text=pythonCodeLines[2], font=codingFont, text_color="#636363")
    lineFour = ctk.CTkLabel(codeFrame, text=pythonCodeLines[3], font=codingFont, text_color="#636363")
    lineFive = ctk.CTkLabel(codeFrame, text=pythonCodeLines[4], font=codingFont, text_color="#636363")
    lineSix = ctk.CTkLabel(codeFrame, text=pythonCodeLines[5], font=codingFont, text_color="#636363")
    lineSeven = ctk.CTkLabel(codeFrame, text=pythonCodeLines[6], font=codingFont, text_color="#636363")
    lineEight = ctk.CTkLabel(codeFrame, text=pythonCodeLines[7], font=codingFont, text_color="#636363")
    lineNine = ctk.CTkLabel(codeFrame, text=pythonCodeLines[8], font=codingFont, text_color="#636363")
    lineTen = ctk.CTkLabel(codeFrame, text=pythonCodeLines[9], font=codingFont, text_color="#636363")
    lineEleven = ctk.CTkLabel(codeFrame, text=pythonCodeLines[10], font=codingFont, text_color="#636363")
    lineTwelve = ctk.CTkLabel(codeFrame, text=pythonCodeLines[11], font=codingFont, text_color="#636363")
    lineThirteen = ctk.CTkLabel(codeFrame, text=pythonCodeLines[12], font=codingFont, text_color="#636363")
    lineFourteen = ctk.CTkLabel(codeFrame, text=pythonCodeLines[13], font=codingFont, text_color="#636363")

    # userFrame
    ideFrameTwo = ctk.CTkFrame(userFrame, fg_color="#232323", width=38, height=400, corner_radius=0)
    separator2 = ctk.CTkFrame(userFrame, fg_color="#353535", width=1, height=373)
    userInput = ctk.CTkTextbox(userFrame, fg_color="#232323", width=454, height=383, font=codingFont, text_color="#FFFFFF", wrap="word", state="disabled")

    # Timer
    timerLabel = ctk.CTkLabel(backgroundFrame, text="60", text_color="#F2F2F2", font=("Geist Mono", 16))
    timerImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/timer.png"), dark_image=Image.open(f"{currentDir}/elements/timer.png"), size=(17, 17))
    timerLogo = ctk.CTkLabel(backgroundFrame, text="", image=timerImage)

    # Language Type
    languageType = ctk.CTkLabel(backgroundFrame, text="PYTHON", text_color="#535353", font=("Geist Mono", 12))

    # Start & Submit Buttons
    startImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/startDark.png"), dark_image=Image.open(f"{currentDir}/elements/startDark.png"), size=(15, 15))
    startButton = ctk.CTkButton(backgroundFrame, text="", image=startImage, fg_color="#F2F2F2", hover_color="#DCDCDC", width=82, height=22, corner_radius=29, command=resetTimer)
    submitImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/submitDark.png"), dark_image=Image.open(f"{currentDir}/elements/submitDark.png"), size=(15, 15))
    submitButton = ctk.CTkButton(backgroundFrame, text="", image=submitImage, fg_color="#F2F2F2", hover_color="#DCDCDC", width=82, height=22, border_width=1, border_color="#F2F2F2", corner_radius=29, state="disabled", command=submitCode)

    # IDE Nums
    numsOne = ctk.CTkLabel(ideFrameOne, text=IDEnums, font=codingFont, text_color="#F2F2F2")
    numsTwo = ctk.CTkLabel(ideFrameTwo, text=IDEnums, font=codingFont, text_color="#F2F2F2") 

    # Code Frame
    codeFrame.place(x=114, y=146)
    ideFrameOne.place(x=9, y=4)
    separator1.place(x=47, y=12)
    numsOne.place(x=9, y=7)
    lineOne.place(x=59, y=6)
    lineTwo.place(x=75, y=26)
    lineThree.place(x=95, y=48)
    lineFour.place(x=95, y=70)
    lineFive.place(x=95, y=90)
    lineSix.place(x=95, y=129)
    lineSeven.place(x=115, y=149)
    lineEight.place(x=130, y=172)
    lineNine.place(x=115, y=195)
    lineTen.place(x=130, y=215)
    lineEleven.place(x=130, y=235)
    lineTwelve.place(x=95, y=276)
    lineThirteen.place(x=115, y=296)
    lineFourteen.place(x=95, y=338)

    # User Code
    userFrame.place(x=662, y=148)
    ideFrameTwo.place(x=9, y=4)
    separator2.place(x=47, y=12)
    numsTwo.place(x=9, y=7)
    userInput.place(x=59, y=7)

    # Positioning - Window Frame
    languageType.place(x=117, y=118)
    startButton.place(x=1016, y=559)
    submitButton.place(x=1107, y=559)
    timerLabel.place(x=1165, y=118)
    timerLogo.place(x=1144, y=118)


    return backgroundFrame
