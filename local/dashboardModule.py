import customtkinter as ctk
import tkinter as tk
import threading
import time
import os

from PIL import Image

currentDir = os.path.dirname(__file__)


scores = f"{currentDir}/dependencies/scoring.txt"
userScore = 0

elapsed = f"{currentDir}/dependencies/elapsedTime.txt"

totalLength = f"{currentDir}/dependencies/counted.txt"

diff = f"{currentDir}/dependencies/recentDifficulty.txt"

usernameFile = f"{currentDir}/dependencies/username.txt"
 
def dashboardFrame(root):

    def watchScoreFile():
        global userScore

        while True:
            time.sleep(0.1)

            print("Threading works")

            with open(elapsed) as timeTaken:
                try:
                    currentTime = int(timeTaken.readline().strip()) / 60
                except:
                    currentTime = 0
    
            with open(scores) as scoreFile:
                userScore = scoreFile.read()

            with open(totalLength) as total:
                length = total.readline()

            with open(diff) as currentDiff:
                difficulty = currentDiff.readline().strip()

            if difficulty != "":
                difficultyText.configure(text=f"{difficulty}")

            if userScore != "":
                wrong = int(length) - int(userScore) 
                if int(userScore) != int(length):
                    counting.configure(text=f"{userScore}/{wrong}")
                else:
                    counting.configure(text=f"{userScore}/0")

                accuracyCalc = (int(userScore) / int(length)) * 100
                accuracy.configure(text=f"{int(accuracyCalc)}%")

                wpm = ((int(userScore) + int(wrong)) / 5) / currentTime
                if wpm > 1000:
                    wpm = 0

                wordsPerMinute.configure(text=f"{int(wpm)}")

                if int(wpm) >= 0 and int(wpm) < 10:
                    wpmLittle.place(x=42, y=190)
                elif int(wpm) > 10 and int(wpm) < 100:
                    wpmLittle.place(x=74, y=190)
                else:
                    wpmLittle.place(x=104, y=190)

            else:
                # ignore else for now
                pass

    watchScore = threading.Thread(target=watchScoreFile, daemon=True)
    watchScore.start()

    geist12px = ctk.CTkFont(family="Geist Mono",
                            size=12,
                            slant="roman")
    
    geist16px = ctk.CTkFont(family="Geist Mono",
                            size=16,
                            slant="roman")
    
    geist52px = ctk.CTkFont(family="Geist Mono",
                            size=52,
                            slant="roman")


    widgetFont = ctk.CTkFont(family="Inter 24pt", 
                        size=16, 
                        slant="roman", # slant roman/italic
                        )
    
    widgetFont2 = ctk.CTkFont(family="Inter 24pt", 
                        size=65, 
                        slant="roman", # slant roman/italic
                        )
    
    # Change username Top Level
    def changeUsernameFunc():
        changeWindow = ctk.CTkToplevel(root)
        changeWindow.title("prism // change your username")
        # changeWindow width x height
        changeWidth = 1280
        changeHeight = 720

        # Grabs the users screen width and height
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        # Center Mathematic
        centerX = (screenWidth / 2) - (changeWidth / 2)
        centerY = (screenHeight / 2) - (changeHeight / 2)

        # prism geometry // apps resolution + center mechanic
        changeWindow.geometry(f"{changeWidth}x{changeHeight}+{int(centerX)}+{int(centerY)}")

        changeWindow.configure(fg_color="#121212")

        # Fonts
        logoFont = ctk.CTkFont(family="Instrument Serif", 
                        size=40,
                        weight="normal",
                        slant="roman", # slant roman/italic
                        )
        
        geist18px = ctk.CTkFont(family="Geist Mono",
                            size=18,
                            weight="normal",
                            slant="roman")

        def closeWindow():
            user = userInput.get()
            if user == "" or len(user) == 0:
                emptyUserInput.place(x=855, y=309)
                changeWindow.after(3000, lambda: emptyUserInput.place(y=721))
            else:
                with open(usernameFile, "w") as userFile:
                    userFile.write(user)
                with open(elapsed, "w") as elapsedTime:
                    elapsedTime.write("")
                with open(scores, "w") as currentScore:
                    currentScore.write("")
                with open(totalLength, "w") as typedRight:
                    typedRight.write("")
                with open(diff, "w") as difficultyFile:
                    difficultyFile.write("")

                changeWindow.destroy()
                root.destroy()
                
        # Elements 
        logoWelcome = ctk.CTkLabel(changeWindow, text="prism", font=logoFont, text_color="#F2F2F2")
        userInput = ctk.CTkEntry(changeWindow, placeholder_text="Enter your new username", text_color="#F2F2F2", fg_color="#121212", border_width=1, border_color="#636363", width=268, height=43, corner_radius=29)
        submitButton = ctk.CTkButton(changeWindow, text="Submit", font=geist18px, text_color="#000000", fg_color="#F2F2F2", hover_color="#DCDCDC", width=164, height=43, corner_radius=29, command=closeWindow)
        emptyUserInput = ctk.CTkLabel(changeWindow, text="!", font=logoFont, text_color="#FE5F55")
        universitylogo = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/6niversitylogo.png"), dark_image=Image.open(f"{currentDir}/elements/6niversitylogo.png"), size=(100, 100))
        logoLabel = ctk.CTkLabel(changeWindow, text="", image=universitylogo, width=100, height=100)
        warningLabel = ctk.CTkLabel(changeWindow, text="WARNING: ALL PROGRESS WILL BE DELETED", font=geist12px, text_color="#535353", width=267, height=16)

        # Placing them
        logoWelcome.place(x=411, y=309)
        logoLabel.place(x=0, y=620)
        userInput.place(x=411, y=369)
        submitButton.place(x=704, y=369)
        warningLabel.place(x=506, y=438)

    # Dashboard Frame
    dashboard = ctk.CTkFrame(root, fg_color="#121212", width=1280, height=720)

    # Images
    missedImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/dangerous.png"), dark_image=Image.open(f"{currentDir}/elements/dangerous.png"), size=(23, 23))
    accuracyImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/accuracy.png"), dark_image=Image.open(f"{currentDir}/elements/accuracy.png"), size=(23, 23))
    wpmImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/keyboard.png"), dark_image=Image.open(f"{currentDir}/elements/keyboard.png"), size=(23, 23))
    commitImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/commit.png"), dark_image=Image.open(f"{currentDir}/elements/commit.png"), size=(23, 23))

    # Last Difficulty
    lastDiff = ctk.CTkLabel(dashboard, text="Last Difficulty:", text_color="#535353", font=geist12px)
    difficultyText = ctk.CTkLabel(dashboard, text="None", text_color="#FFFFFF", font=geist12px)

    # Apeparance // Frames
    widget1 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget2 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget3 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget4 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)

    # Widget1 Elements
    wrongText = ctk.CTkLabel(dashboard, text="Typing Mistakes", text_color="#535353", font=geist12px)
    wrongLabel = ctk.CTkLabel(dashboard, text="", image=missedImage)
    counting = ctk.CTkLabel(widget1, text="0", text_color="#F2F2F2", font=geist52px)
    rL = ctk.CTkLabel(widget1, text="Right / Wrong", text_color="#535353", font=geist12px)

    # Widget2 Elements
    accuracyText = ctk.CTkLabel(dashboard, text="Accuracy", text_color="#535353", font=geist12px)
    accuracyLabel = ctk.CTkLabel(dashboard, text="", image=accuracyImage)
    accuracy = ctk.CTkLabel(widget2, text="0", text_color="#F2F2F2", font=geist52px)
    acL = ctk.CTkLabel(widget2, text="of accurate code", text_color="#535353", font=geist12px)

    # Widget3 Elements
    wordsPerMinuteText = ctk.CTkLabel(dashboard, text="Words Per Minute", text_color="#535353", font=geist12px)
    wpmLabel = ctk.CTkLabel(dashboard, text="", image=wpmImage)
    wordsPerMinute = ctk.CTkLabel(widget3, text="0", text_color="#F2F2F2", font=geist52px)
    wpmLittle = ctk.CTkLabel(widget3, text="wpm", text_color="#535353", font=geist12px)

    # Widget4 Elements
    versionText = ctk.CTkLabel(dashboard, text="Current Version", text_color="#535353", font=geist12px)
    versionLabel = ctk.CTkLabel(dashboard, text="", image=commitImage)
    versionNum = ctk.CTkLabel(widget4, text="1", text_color="#FFFFFF", font=geist52px)
    publicRelease = ctk.CTkLabel(widget4, text="Public Release", text_color="#535353", font=geist12px)

    # Change username
    changeUsernameButton = ctk.CTkButton(dashboard, text="Change Username", fg_color="#FFFFFF", text_color="#000000", hover_color="#DCDCDC", font=geist16px, corner_radius=50, width=171, height=31, command=changeUsernameFunc)

    # Positioning
    lastDiff.place(x=37, y=80)
    difficultyText.place(x=159, y=80)
    changeUsernameButton.place(x=1076, y=31)

    widget1.place(x=148, y=186)
    wrongText.place(x=176, y=156)
    wrongLabel.place(x=148, y=158)
    counting.place(x=7, y=158)
    rL.place(x=12, y=143)

    widget2.place(x=401, y=186)
    accuracyText.place(x=429, y=156)
    accuracyLabel.place(x=401, y=158)
    accuracy.place(x=7, y=158)
    acL.place(x=12, y=143)

    widget3.place(x=654, y=186)
    wordsPerMinuteText.place(x=682, y=156)
    wordsPerMinute.place(x=7, y=158)
    wpmLabel.place(x=654, y=158)
    wpmLittle.place(x=42, y=190)

    widget4.place(x=907, y=186)
    versionText.place(x=935, y=156)
    versionLabel.place(x=907, y=158)
    versionNum.place(x=7, y=158)
    publicRelease.place(x=43, y=190)

    return dashboard