# import packages
import customtkinter as ctk
import tkinter as tk
import os

from PIL import Image

# Import Modules // Frames
from dashboardModule import dashboardFrame
from easyCode import easyFrame, easyPython
from mediumCode import mediumFrame, mediumPython
from hardCode import hardFrame, hardPython

# Get the directory that the folder is in
currentDir = os.path.dirname(__file__)

# Get information from dependencies
user = f"{currentDir}/dependencies/username.txt"
elapsed = f"{currentDir}/dependencies/elapsedTime.txt"

# User's username
username = "unknown"

# Default App Settings
appearance = "light"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  

# Main App
def codeType(): 

    root = ctk.CTk()
    root.title("prism // @voiduniversity")

    # codeType width x height
    rootWidth = 1280
    rootHeight = 720

    # Grabs the users screen width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # Center Mathematic
    centerX = (screenWidth / 2) - (rootWidth / 2)
    centerY = (screenHeight / 2) - (rootHeight / 2)

    # codeType geometry // apps resolution + center mechanic
    root.geometry(f"{rootWidth}x{rootHeight}+{int(centerX)}+{int(centerY)}")

    root.configure(fg_color="#121212")
    root.resizable(width = False, height = False) # Disable user scaling

    # Fonts // Same font, different sizes
    logoFont = ctk.CTkFont(family="Instrument Serif", 
                        size=40,
                        weight="normal",
                        slant="roman", # slant roman/italic
                        )
        
    usernameFont = ctk.CTkFont(family="Instrument Serif", 
                            size=24,
                            weight="normal",
                            slant="roman", # slant roman/italic
                            )
    
    geist16px = ctk.CTkFont(family="Geist Mono",
                            size=16,
                            slant="roman")

    # Top Level Window // remake unfinished
    with open(user) as usernameFile:
        username = usernameFile.read().strip("/n")
        if username == "":
            userWindow = ctk.CTkToplevel(root)
            userWindow.title("prism // welcome")
            userWindow.geometry(f"{rootWidth}x{rootHeight}+{int(centerX)}+{int(centerY)}")
            userWindow.configure(fg_color="#121212")
                
            # Triggered whenever the user presses the "Submit" button
            def closeWindow():
                usernameInput = userInput.get()
                if usernameInput == "" or len(usernameInput) == 0:
                    emptyUserInput.place(x=855, y=309)
                    userWindow.after(3000, lambda: emptyUserInput.place(y=721))
                else:
                    with open(user, "w") as writtenUsername:
                        writtenUsername.write(usernameInput)
                    root.destroy()
            
            # Elements 
            logoWelcome = ctk.CTkLabel(userWindow, text="prism", font=logoFont, text_color="#F2F2F2")
            userInput = ctk.CTkEntry(userWindow, placeholder_text="Enter your username", text_color="#F2F2F2", fg_color="#121212", border_width=1, border_color="#636363", width=268, height=43, corner_radius=29)
            submitButton = ctk.CTkButton(userWindow, text="Submit", font=("Geist Mono", 18), text_color="#000000", fg_color="#F2F2F2", hover_color="#DCDCDC", width=164, height=43, corner_radius=29, command=closeWindow)
            emptyUserInput = ctk.CTkLabel(userWindow, text="!", font=logoFont, text_color="#FE5F55")
            universitylogo = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/6niversitylogo.png"), dark_image=Image.open(f"{currentDir}/elements/6niversitylogo.png"), size=(100, 100))
            logoLabel = ctk.CTkLabel(userWindow, text="", image=universitylogo, width=100, height=100)

            # Placing them
            logoWelcome.place(x=411, y=309)
            logoLabel.place(x=0, y=620)
            userInput.place(x=411, y=369)
            submitButton.place(x=704, y=369)

    # Call functions to load coding examples.
    easyPython()
    mediumPython()
    hardPython()

    # Frames // Imported from different modules
    dashboard = dashboardFrame(root) # Frame -> root (mainApp)
    easy = easyFrame(root) # Frame -> arg: root (mainApp)
    medium = mediumFrame(root) # Frame -> arg: root (mainApp)
    hard = hardFrame(root) # Frame -> arg: root (mainApp)

    # dashboardMenu, easyMenu & mediumMenu -> functions to show current frames
    def dashboardMenu():
        # Place new frame
        dashboard.place(y=0)
        diffFrame.place(y=480)

        # Get rid of current frame
        easy.place(y=721)
        medium.place(y=721)
        hard.place(y=721)
        returnFrame.place(y=721)
    
    def easyMenu():
        # Place new frame
        easy.place(y=0)
        returnFrame.place(y=655)

        # Get rid of current frame
        dashboard.place(y=721)
        diffFrame.place(y=721)

    def mediumMenu():
        # Place new frame
        medium.place(y=0)
        returnFrame.place(y=655)

        # Get rid of current frame
        dashboard.place(y=721)
        diffFrame.place(y=721)
    
    def hardMenu():
        # Place new frame
        hard.place(y=0)
        returnFrame.place(y=655)

        # place dashboard & diffFrame out of frame
        dashboard.place(y=721)
        diffFrame.place(y=721)

    # Text Labels
    logo = ctk.CTkLabel(root, text="prism", font=logoFont, text_color="#F2F2F2")
    
    # Welcome Message inside dashboard
    usernameText = ctk.CTkLabel(root, text=f"@{username}", font=usernameFont, text_color="#FFFFFF")

    # Pick difficulty
    diffFrame = ctk.CTkFrame(root, fg_color="#121212", width=450, height=141)
    pickLabel = ctk.CTkLabel(diffFrame, text="Pick a Mode:", text_color="#535353", font=geist16px)
    easyButton = ctk.CTkButton(diffFrame, width=116, height=31, text="Easy", text_color="#000000", fg_color="#FFFFFF", bg_color="#000000", hover_color="#DCDCDC", corner_radius=50, font=geist16px, command=easyMenu)
    mediumButton = ctk.CTkButton(diffFrame, width=116, height=31, text="Medium", text_color="#000000", fg_color="#FFFFFF", bg_color="#000000", hover_color="#DCDCDC", corner_radius=50, font=geist16px, command=mediumMenu)
    hardButton = ctk.CTkButton(diffFrame, width=116, height=31, text="Hard", text_color="#000000", fg_color="#FFFFFF", bg_color="#000000", hover_color="#DCDCDC", corner_radius=50, font=geist16px, command=hardMenu)

    # Return to dashboard
    returnFrame = ctk.CTkFrame(root, fg_color="#121212", width=178, height=50)
    returnButton = ctk.CTkButton(returnFrame, width=116, height=31, text="Return", text_color="#000000", fg_color="#FFFFFF", bg_color="#000000", hover_color="#DCDCDC", corner_radius=50, font=geist16px, command=dashboardMenu)

    # positioning dashboard - main & extra elements
    dashboard.place(x=0, y=0)
    usernameText.place(x=132, y=30)

    # difficulty positioning
    diffFrame.place(x=415, y=480)
    pickLabel.place(x=167, y=33)
    easyButton.place(x=40, y=66)
    mediumButton.place(x=167, y=66)
    hardButton.place(x=294, y=66)

    returnFrame.place(x=1089, y=721)
    returnButton.place(x=31, y=10)

    # positioning - labels
    logo.place(x=37, y=20)

    # positioning frames - difficulty frames
    easy.place(x=0, y=721)
    medium.place(x=0, y=721)
    hard.place(x=0, y=721)

    root.mainloop()

# currentDirectory -> use the current directory
def currentDirectory():
    try:
        os.chdir(currentDir) # Use currentDir
    except Exception as e:
        print("There has been an error with the currentDir variable.")

# Run the project
def main():
    currentDirectory()
    codeType()
main()