# import packages
import customtkinter as ctk
import tkinter as tk
import os

from PIL import Image

# Import Modules // Frames
from dashboardModule import dashboardFrame
from easyCode import easyFrame, easyPython
from mediumCode import mediumFrame, mediumPython

appearance = "light" # Default

user = "username.txt"
elapsed = "elapsedTime.txt"

username = "unknown"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  

def codeType():
    currentDir = os.getcwd()

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
    logoFont = ctk.CTkFont(family="Inter 24pt", 
                        size=40,
                        slant="roman", # slant roman/italic
                        )
        
    elementFont = ctk.CTkFont(family="Linefont", 
                        size=40,
                        weight="normal",
                        slant="roman", # slant roman/italic
                        )
        
    welcomeFont = ctk.CTkFont(family="Inter 24pt", 
                            size=24,
                            slant="roman", # slant roman/italic
                            )
        
    usernameFont = ctk.CTkFont(family="Nothing You Could Do", 
                            size=24,
                            slant="roman", # slant roman/italic
                            )
        
    welcomeSubHeading = ctk.CTkFont(family="Inter 24pt", 
                            size=16,
                            slant="roman", # slant roman/italic
                            )




    # Top Level Window // Finished
    with open(user) as usernameFile:
        username = usernameFile.read()
        if username == "":
            userWindow = ctk.CTkToplevel(root)
            userWindow.title("prism // welcome")
            userWindow.geometry(f"{rootWidth}x{rootHeight}+{int(centerX)}+{int(centerY)}")
            userWindow.configure(fg_color="#121212")
                
            
            def closeWindow():
                usernameInput = userInput.get()
                if usernameInput == "":
                    emptyUserInput.place(x=28, y=111)
                    userWindow.after(3000, lambda: emptyUserInput.place(y=721))
                else:
                    username = usernameInput
                    with open(user, "w") as writtenUsername:
                        writtenUsername.write(usernameInput)
                    root.destroy()
            
            # Elements 
            welcomeFrame = ctk.CTkFrame(userWindow, fg_color="#121212", border_width=1, border_color="#636363", width=394, height=328, corner_radius=23)

            logoWelcome = ctk.CTkLabel(welcomeFrame, text="prism", font=logoFont, text_color="#F2F2F2")

            authorWelcome = ctk.CTkLabel(welcomeFrame, text="university", font=elementFont, text_color="#F2F2F2")

            userInput = ctk.CTkEntry(welcomeFrame, placeholder_text="Enter your username", text_color="#F2F2F2", fg_color="#121212", border_width=1, border_color="#636363", width=268, height=43, corner_radius=29)

            submitButton = ctk.CTkButton(welcomeFrame, text="Submit", font=("Inter 24pt", 24), text_color="#F2F2F2", fg_color="#121212", hover_color="#1F1F1F", border_width=1, border_color="#636363", width=164, height=43, corner_radius=29, command=closeWindow)

            emptyUserInput = ctk.CTkLabel(welcomeFrame, text="!", font=logoFont, text_color="#FE5F55")

            # Placing them
            welcomeFrame.place(x=443, y=196)
            logoWelcome.place(x=142, y=34)
            authorWelcome.place(x=177, y=244)
            userInput.place(x=65, y=114)
            submitButton.place(x=115, y=185)
    



    # Frames // Imported from different modules
    easyPython() # Int -> length of chars in easy python coding
    mediumPython()
    dashboard = dashboardFrame(root) # Frame -> root (mainApp)
    easy = easyFrame(root) # Frame -> root (mainApp)
    medium = mediumFrame(root) # Frame -> root (mainApp)




    # Create Icons for menu buttons // CustomTkinter Image Utility with Pillow Package
    dashboardIcon = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/Mask.png"), dark_image=Image.open(f"{currentDir}/elements/Mask.png"), size=(20, 20))
    easyIcon = ctk.CTkImage(light_image=Image.open(f"{currentDir}/elements/Pixel.png"), dark_image=Image.open(f"{currentDir}/elements/Pixel.png"), size=(20, 20))




    def dashboardMenu():
        # Place new frame
        dashboard.place(y=0)

        # Get rid of current frame
        easy.place(y=721)
        medium.place(y=721)
    
    def easyMenu():
        # Place new frame
        easy.place(y=0)

        # Get rid of current frame
        dashboard.place(y=721)
        medium.place(y=721)

    def mediumMenu():
        # Place new frame
        medium.place(y=0)

        # Get rid of current frame
        dashboard.place(y=721)
        easy.place(y=721)


    # Text Labels
    logo = ctk.CTkLabel(root, text="prism", font=logoFont, text_color="#F2F2F2")

    plusElement = ctk.CTkLabel(root, text="+", font=logoFont, text_color="#F2F2F2")

    universityLabel = ctk.CTkLabel(root, text="university", font=elementFont, text_color="#F2F2F2")




    # Menu & Buttons // Placeholder
    menuFrame = ctk.CTkFrame(root, fg_color="#121212", width=355, height=65, border_color="#636363", border_width=1, corner_radius=20)

    dashboardButton = ctk.CTkButton(menuFrame, text="", image=dashboardIcon, fg_color="#121212", hover_color="#121212", width=42, height=42, border_width=1, border_color="#636363", corner_radius=10, command=dashboardMenu)

    easyButton = ctk.CTkButton(menuFrame, text="", image=easyIcon, fg_color="#121212", hover_color="#121212", width=42, height=42, border_width=1, border_color="#636363", corner_radius=10, command=easyMenu)

    mediumButton = ctk.CTkButton(menuFrame, text="", image=easyIcon, fg_color="#121212", hover_color="#121212", width=42, height=42, border_width=1, border_color="#636363", corner_radius=10, command=mediumMenu)

    hardButton = ctk.CTkButton(menuFrame, text="", image=easyIcon, fg_color="#121212", hover_color="#121212", width=42, height=42, border_width=1, border_color="#636363", corner_radius=10, command=None)

    creditsButton = ctk.CTkButton(menuFrame, text="", image=easyIcon, fg_color="#121212", hover_color="#121212", width=42, height=42, border_width=1, border_color="#636363", corner_radius=10, command=None)




    # Welcome Message inside dashboard
    bluebar = ctk.CTkFrame(dashboard, fg_color="#6B8CE6", width=6, height=59)
    welcomeMessage = ctk.CTkLabel(dashboard, text=f"Welcome,", font=welcomeFont, text_color="#F2F2F2")
    usernameText = ctk.CTkLabel(dashboard, text=f"{username}!", font=usernameFont)
    subHeading = ctk.CTkLabel(dashboard, text="Here's your performance", font=welcomeSubHeading, text_color="#484848")




    # positioning - menu
    menuFrame.place(x=462, y=623)
    dashboardButton.place(x=25 , y=11)
    easyButton.place(x=91, y=11)
    mediumButton.place(x=157, y=11)
    hardButton.place(x=223, y=11)
    creditsButton.place(x=289, y=11)

    # positioning dashboard - main & extra elements
    dashboard.place(x=0, y=0)
    bluebar.place(x=53, y=82)
    welcomeMessage.place(x=67, y=88)
    usernameText.place(x=192, y=88)
    subHeading.place(x=69, y=114)

    # positioning - labels
    logo.place(x=37, y=20)
    plusElement.place(x=1214, y=22)
    universityLabel.place(x=44, y=632)


    easy.place(x=0, y=721)
    medium.place(x=0, y=721)

    root.mainloop()

def currentDirectory():
    try:
        currentDir = os.getcwd() # Get current directory
        os.chdir(currentDir) # Use currentDir
    except Exception as e:
        print("There has been an error with the currentDir variable.")

def main():
    currentDirectory()
    codeType()
main()



# Spalsh Screen
'''
    emptyFrame = ctk.CTkFrame(root, fg_color="#121212", width=1280, height=720)
    codinglogo = ctk.CTkLabel(emptyFrame, text="coding* |", text_color="#F2F2F2", font=logoFont)
    universitytext = ctk.CTkLabel(emptyFrame, text="university", text_color="#F2F2F2", font=elementFont)

    emptyFrame.place(x=0, y=0)
    codinglogo.place(x=524, y=336)
    universitytext.place(x=715, y=327)

    root.after(2000, lambda: emptyFrame.destroy())
'''
