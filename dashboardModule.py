import customtkinter as ctk
import tkinter as tk
import threading
import time
import os

from PIL import Image

currentDir = os.getcwd()

easyScore = f"{currentDir}/dependencies/scoring.txt"
userScore = 0

elapsed = f"{currentDir}/dependencies/elapsedTime.txt"

totalLength = f"{currentDir}/dependencies/counted.txt"

diff = f"{currentDir}/dependencies/recentDifficulty.txt"
 
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
    
            with open(easyScore) as scoreFile:
                userScore = scoreFile.read()

            with open(totalLength) as total:
                length = total.readline()

            with open(diff) as currentDiff:
                difficulty = currentDiff.readline().strip()

            if difficulty != "":
                difficultyText.configure(text=f"{difficulty}")

            if userScore != "":
                if int(userScore) != int(length):
                    wrong = int(length) - int(userScore) 
                    counting.configure(text=f"{userScore}/{wrong}")
                else:
                    counting.configure(text=f"{userScore}/0")

                accuracyCalc = (int(userScore) / int(length)) * 100
                accuracy.configure(text=f"{int(accuracyCalc)}%")

                wpm = ((int(userScore) + int(wrong)) / 5) / currentTime
                wordsPerMinute.configure(text=f"{int(wpm)}")

                if int(wpm) >= 0 and int(wpm) < 10:
                    wpmLittle.place(x=55, y=190)
                elif int(wpm) > 10 and int(wpm) < 100:
                    wpmLittle.place(x=94, y=190)
                else:
                    wpmLittle.place(x=131, y=190)

            else:
                counting.configure(text="0/0")
                accuracy.configure(text=f"0%")
                wordsPerMinute.configure(text="0wpm")

                
    
    watchScore = threading.Thread(target=watchScoreFile, daemon=True)
    watchScore.start()

    geist12px = ctk.CTkFont(family="Geist Mono",
                            size=12,
                            slant="roman")
    
    geist16px = ctk.CTkFont(family="Geist Mono",
                            size=16,
                            slant="roman")
    
    geist65px = ctk.CTkFont(family="Geist Mono",
                            size=65,
                            slant="roman")


    widgetFont = ctk.CTkFont(family="Inter 24pt", 
                        size=16, 
                        slant="roman", # slant roman/italic
                        )
    
    widgetFont2 = ctk.CTkFont(family="Inter 24pt", 
                        size=65, 
                        slant="roman", # slant roman/italic
                        )

    # Dashboard Frame
    dashboard = ctk.CTkFrame(root, fg_color="#121212", width=1280, height=720)

    # Images
    missedImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/dangerous.png"), dark_image=Image.open(f"{currentDir}/elements/dangerous.png"), size=(23, 23))
    accuracyImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/accuracy.png"), dark_image=Image.open(f"{currentDir}/elements/accuracy.png"), size=(23, 23))
    wpmImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/keyboard.png"), dark_image=Image.open(f"{currentDir}/elements/keyboard.png"), size=(23, 23))
    commitImage = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/commit.png"), dark_image=Image.open(f"{currentDir}/elements/commit.png"), size=(23, 23))

    # Last Difficulty
    lastDiff = ctk.CTkLabel(root, text="Last Difficulty:", text_color="#535353", font=geist12px)
    difficultyText = ctk.CTkLabel(root, text="None", text_color="#FFFFFF", font=geist12px)

    # Apeparance // Frames
    widget1 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget2 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget3 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)
    widget4 = ctk.CTkFrame(dashboard, fg_color="#232323", width=224, height=224, corner_radius=12)

    # Widget1 Elements
    wrongText = ctk.CTkLabel(dashboard, text="Typing Mistakes", text_color="#535353", font=geist12px)
    wrongLabel = ctk.CTkLabel(dashboard, text="", image=missedImage)
    counting = ctk.CTkLabel(widget1, text="", text_color="#F2F2F2", font=geist65px)
    rL = ctk.CTkLabel(widget1, text="Right / Wrong", text_color="#535353", font=geist12px)

    # Widget2 Elements
    accuracyText = ctk.CTkLabel(dashboard, text="Accuracy", text_color="#535353", font=geist12px)
    accuracyLabel = ctk.CTkLabel(dashboard, text="", image=accuracyImage)
    accuracy = ctk.CTkLabel(widget2, text="", text_color="#F2F2F2", font=geist65px)
    acL = ctk.CTkLabel(widget2, text="of accurate code", text_color="#535353", font=geist12px)

    # Widget3 Elements
    wordsPerMinuteText = ctk.CTkLabel(dashboard, text="Words Per Minute", text_color="#535353", font=geist12px)
    wpmLabel = ctk.CTkLabel(dashboard, text="", image=wpmImage)
    wordsPerMinute = ctk.CTkLabel(widget3, text="", text_color="#F2F2F2", font=geist65px)
    wpmLittle = ctk.CTkLabel(widget3, text="wpm", text_color="#535353", font=geist12px)

    # Widget4 Elements
    versionText = ctk.CTkLabel(dashboard, text="Current Version", text_color="#535353", font=geist12px)
    versionLabel = ctk.CTkLabel(dashboard, text="", image=commitImage)
    versionNum = ctk.CTkLabel(widget4, text="1", text_color="#FFFFFF", font=geist65px)
    publicRelease = ctk.CTkLabel(widget4, text="Public Release", text_color="#535353", font=geist12px)

    # Positioning
    lastDiff.place(x=37, y=80)
    difficultyText.place(x=159, y=80)

    widget1.place(x=148, y=186)
    wrongText.place(x=176, y=156)
    wrongLabel.place(x=148, y=158)
    counting.place(x=7, y=143)
    rL.place(x=7, y=130)

    widget2.place(x=401, y=186)
    accuracyText.place(x=429, y=156)
    accuracyLabel.place(x=401, y=158)
    accuracy.place(x=7, y=143)
    acL.place(x=7, y=130)

    widget3.place(x=654, y=186)
    wordsPerMinuteText.place(x=682, y=156)
    wordsPerMinute.place(x=7, y=143)
    wpmLabel.place(x=654, y=158)

    widget4.place(x=907, y=186)
    versionText.place(x=935, y=156)
    versionLabel.place(x=907, y=158)
    versionNum.place(x=7, y=143)
    publicRelease.place(x=56, y=190)

    return dashboard