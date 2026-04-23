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
 
def dashboardFrame(root):

    def watchScoreFile():
        global userScore

        while True:
            time.sleep(0.1)
            with open(elapsed) as timeTaken:
                try:
                    currentTime = int(timeTaken.readline().strip()) / 60
                except:
                    currentTime = 0
            print("Threading works")
            with open(easyScore) as scoreFile:
                userScore = scoreFile.read()

            with open(totalLength) as total:
                length = total.readline()

            if userScore != "":
                if int(userScore) != int(length):
                    wrong = int(length) - int(userScore) 
                    counting.configure(text=f"{userScore}/{wrong}")
                else:
                    counting.configure(text=f"{userScore}/0")

                accuracyCalc = (int(userScore) / int(length)) * 100
                accuracy.configure(text=f"{int(accuracyCalc)}%")

                wpm = ((int(userScore) + int(wrong)) / 5) / currentTime
                wordsPerMinute.configure(text=f"{int(wpm)}wpm")

            else:
                counting.configure(text="0/0")
                accuracy.configure(text=f"0%")
                wordsPerMinute.configure(text="0wpm")

                
    
    watchScore = threading.Thread(target=watchScoreFile, daemon=True)
    watchScore.start()


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

    # Apeparance // Frames
    widget1 = ctk.CTkFrame(dashboard, fg_color="#121212", border_width=1, border_color="#636363", width=308, height=177, corner_radius=29)
    widget2 = ctk.CTkFrame(dashboard, fg_color="#121212", border_width=1, border_color="#636363", width=308, height=177, corner_radius=29)
    widget3 = ctk.CTkFrame(dashboard, fg_color="#121212", border_width=1, border_color="#636363", width=308, height=177, corner_radius=29)
    leaderboardwidget = ctk.CTkFrame(dashboard, fg_color="#121212", border_width=1, border_color="#636363", width=308, height=177, corner_radius=29)

    # Widget1 Elements
    wrongText = ctk.CTkLabel(widget1, text="Missed Characters", text_color="#F2F2F2", font=widgetFont)
    wrongDesc = ctk.CTkLabel(widget1, text="R/W", text_color="#F2F2F2", font=widgetFont)
    counting = ctk.CTkLabel(widget1, text="", text_color="#F2F2F2", font=widgetFont2)
    wrongLabel = ctk.CTkLabel(widget1, text="", image=missedImage)

    # Widget2 Elements
    accuracyText = ctk.CTkLabel(widget2, text="Accuracy", text_color="#F2F2F2", font=widgetFont)
    accuracy = ctk.CTkLabel(widget2, text="", text_color="#F2F2F2", font=widgetFont2)
    accuracyLabel = ctk.CTkLabel(widget2, text="", image=accuracyImage)

    # Widget3 Elements
    wordsPerMinuteText = ctk.CTkLabel(widget3, text="Words Per Minute", text_color="#F2F2F2", font=widgetFont)
    wordsPerMinute = ctk.CTkLabel(widget3, text="", text_color="#F2F2F2", font=widgetFont2)
    wpmLabel = ctk.CTkLabel(widget3, text="", image=wpmImage)


    # Widget Positioning
    widget1.place(x=106, y=168)
    wrongText.place(x=143, y=11)
    wrongDesc.place(x=255, y=36)
    counting.place(x=13, y=88)
    wrongLabel.place(x=16, y=13)

    widget2.place(x=488, y=168)
    accuracyText.place(x=213, y=11)
    accuracy.place(x=12, y=88)
    accuracyLabel.place(x=16, y=13)

    widget3.place(x=870, y=168)
    wordsPerMinuteText.place(x=159, y=11)
    wordsPerMinute.place(x=14, y=88)
    wpmLabel.place(x=16, y=13)

    return dashboard