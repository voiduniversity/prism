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
        userFrame.configure(state="disabled")
        submitButton.configure(state="disabled")
        startButton.configure(state="normmal")


        userCode = userFrame.get(0.0, "end")
        splitNewLine = userCode.split("\n")
        joinedCode = "".join(splitNewLine)
        splitSpace = joinedCode.split()
        final = "".join(splitSpace)


        # Track right & wrong with the help of claude
        i = 0
        j = 0
        rightChars = 0
        userInput = list(final)
        codingExample = list(pythonExample)
        # loop through if i is less than the length of user input and if j is less than the coding example
        while i < len(userInput) and j < len(codingExample):
            # if both are the same
            if userInput[i] == codingExample[j]:
                rightChars += 1
                i += 1
                j += 1
                continue
            else:
                # Inserion // if i+1 is not the last char and i+1 is the same as j's current index
                if i + 1 < len(userInput) and userInput[i + 1] == codingExample[j]:
                    i += 1
                    continue
                # Deletion // if j+1 is not the last char and j+1 is the same as i's current index
                elif j + 1 < len(codingExample) and userInput[i] == codingExample[j + 1]:
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
        userFrame.configure(state="normal")
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
        global timer
        timer = 61
        elapsed = 0
        timerFunc()
            


    # Placeholder Frame
    backgroundFrame = ctk.CTkFrame(root, fg_color="#121212", width=1280, height=720)
    windowFrame = ctk.CTkFrame(backgroundFrame, fg_color="#121212", width=1126, height=479, border_width=1, border_color="#636363", corner_radius=14)
    codeFrame = ctk.CTkFrame(windowFrame, fg_color="#121212", width=527, height=400, border_width=1, border_color="#636363", corner_radius=0)
    userFrame = ctk.CTkTextbox(windowFrame, fg_color="#121212", width=525, height=400, font=codingFont, wrap="word", border_width=1, border_color="#636363", corner_radius=0, state="disabled")
    ideFrameOne = ctk.CTkFrame(windowFrame, fg_color="#121212", width=38, height=400, border_width=1, border_color="#636363", corner_radius=0)
    ideFrameTwo = ctk.CTkFrame(windowFrame, fg_color="#121212", width=39, height=400, border_width=1, border_color="#636363", corner_radius=0)
    numsOne = ctk.CTkLabel(ideFrameOne, text=IDEnums, font=codingFont, text_color="#636363")
    numsTwo = ctk.CTkLabel(ideFrameTwo, text=IDEnums, font=codingFont, text_color="#636363")

    # Window Frame Elements
    circleOne = ctk.CTkFrame(windowFrame, fg_color="#323232", width=13, height=13, corner_radius=18)
    circleTwo = ctk.CTkFrame(windowFrame, fg_color="#424242", width=13, height=13, corner_radius=18)
    circleThree = ctk.CTkFrame(windowFrame, fg_color="#595959", width=13, height=13, corner_radius=18)
    timerLabel = ctk.CTkLabel(windowFrame, text="60", text_color="#636363", font=("Geist Mono", 16))
    timerImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/timer.png"), dark_image=Image.open(f"{currentDir}/elements/timer.png"), size=(17, 17))
    timerLogo = ctk.CTkLabel(windowFrame, text="", image=timerImage)


    languageType = ctk.CTkLabel(windowFrame, text="python", text_color="#636363", font=("Geist Mono", 16))
    startImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/start.png"), dark_image=Image.open(f"{currentDir}/elements/start.png"), size=(15, 15))
    startButton = ctk.CTkButton(windowFrame, text="", image=startImage, text_color="#F2F2F2", text_color_disabled="#636363", fg_color="#121212", hover_color="#121212", width=82, height=22, border_width=1, border_color="#636363", corner_radius=29, command=resetTimer)
    submitImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/submit.png"), dark_image=Image.open(f"{currentDir}/elements/submit.png"), size=(15, 15))
    submitButton = ctk.CTkButton(windowFrame, text="", image=submitImage, text_color="#F2F2F2", text_color_disabled="#636363", fg_color="#121212", hover_color="#121212", width=82, height=22, border_width=1, border_color="#636363", corner_radius=29, state="disabled", command=submitCode)

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


    # Positioning - Window Frame
    windowFrame.place(x=77, y=100)
    circleOne.place(x=20, y=18)
    circleTwo.place(x=37, y=18)
    circleThree.place(x=54, y=18)
    languageType.place(x=77, y=7)
    startButton.place(x=947, y=451)
    submitButton.place(x=1038, y=451)
    timerLabel.place(x=1092, y=9)
    timerLogo.place(x=1071, y=10)

    # Code Frame
    codeFrame.place(x=37, y=46)
    ideFrameOne.place(x=0, y=46)
    numsOne.place(x=9, y=7)
    lineOne.place(x=9, y=3)
    lineTwo.place(x=9, y=25)
    lineThree.place(x=25, y=45)
    lineFour.place(x=25, y=67)
    lineFive.place(x=25, y=87)
    lineSix.place(x=25, y=129)
    lineSeven.place(x=41, y=149)
    lineEight.place(x=58, y=172)
    lineNine.place(x=41, y=192)
    lineTen.place(x=58, y=212)
    lineEleven.place(x=58, y=232)
    lineTwelve.place(x=25, y=276)
    lineThirteen.place(x=41, y=296)
    lineFourteen.place(x=25, y=338)

    # User Code
    userFrame.place(x=601, y=46)
    ideFrameTwo.place(x=563, y=46)
    numsTwo.place(x=10, y=7)


    return backgroundFrame
