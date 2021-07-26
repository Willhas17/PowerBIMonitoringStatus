import tkinter as tk
import time
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Command for transform in an exe
#pyinstaller --noconfirm --onefile --noconsole "'directory'/PowerBI.py"

root = tk.Tk()
root.title('POWER BI - STATUS')
window_width = 400
window_height = 405

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# define the dimension
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(True, True)

## Using a alternative theme
# Import the tcl file
root.tk.call("source", "azure-dark.tcl")
style = ttk.Style(root)
style.theme_use("azure-dark")
##


canvas = []
canvascolor = []

def Atualizar_Rela():
    # The main url for login
    url = r"https://app.powerbi.com/?tenant=&UPN="
    option = Options()
    option.add_argument("--incognito")
    option.headless = True

    driver = webdriver.Chrome(options=option)


    try:
        driver.get(url)
        time.sleep(3)
        elem = driver.find_element_by_name("loginfmt")
        elem.clear()
        # Input your power BI email here
        elem.send_keys("email@powerBI.com.br")
        elem.send_keys(Keys.ENTER)
        time.sleep(1)
        elem = driver.find_element_by_name("passwd")
        # Input your passaword here
        elem.send_keys("Passawordhere")
        elem.send_keys(Keys.ENTER)
        time.sleep(3)
        elem = driver.find_element_by_id("idSIButton9")
        elem.click()
        time.sleep(3)
        
        # Finding all the workspaces to collect informations
        work = driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/button')
        time.sleep(1)
        work.click()
        time.sleep(1)

        work = driver.find_element_by_class_name('workspacesPaneExpander.switcher')
        work.click()

        workcount = driver.find_elements_by_class_name("groupContextMenuButton")
        time.sleep(1)
    

        cont = 0
        cont2 = 0
        lb = []
        lb2 = []
        global canvas
        global canvascolor

        canvas = []
        canvascolor = []

        # "workcount" count the workspaces quantity
        for p in range(int(len(workcount))):
            pathtemp = '//*[@id="cdk-overlay-2"]/nav/nav-pane-workspaces/div[3]/virtual-scroll/div[2]/ul/li['+ str(p + 1) +']/workspace-button'  
            tempclick = driver.find_element_by_xpath(pathtemp)
            tempclick.click()
            work = driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/button')
            work.click()
            time.sleep(3)    
            grid = driver.find_elements_by_class_name('row.ng-star-inserted')
            colunas = []  

            for y in range(3):
                if y == 0:
                    k = 2 # Use for collect the name of the report in workspace
                elif y == 1:
                    k = 5 # Use for collect the actual refresh hour of the report in workspace
                elif y == 2:
                    k = 6 # Use for collect the next refresh hour of the report in workspace
                
                #print(k)  
                linhas = []
                
                # Loop for all reports in the workspace
                for x in range(int((len(grid)/2))):
                    
                    xpath = "//*[@id='artifactContentList']/div[1]/div["+ str((x * 2)+2) +"]/div[" + str(k) + "]/span"  
                    linhas.append(driver.find_element_by_xpath(xpath))                 

                    lb.append("-")
                    canvas.append("-")
                    lb2.append("-")
                    lb[cont] = tk.Label(root, text="-")
                    lb[cont].grid(column=3, row=cont)
                    lb2[cont] = tk.Label(root, text="-")
                    lb2[cont].grid(column=4, row=cont)
                    canvas[cont] = tk.Canvas(root, width=15, height=15,highlightbackground="black", borderwidth=1, highlightthickness=5, bg="white")
                    canvas[cont].grid(row=cont)

                    # Set colors for actual status of the reports
                    if k == 6:
                        lb2[cont2].configure(text=linhas[x].text)
                        canvascolor.append("yellow")
                        if linhas[x].text == "N/D":
                            canvascolor[cont2] = "red"
                        else:    
                            canvascolor[cont2] = "green"
                        cont2+= 1   
                       
                        

                    if k == 2:
                       
                        lb[cont].configure(text=linhas[x].text)
                        cont+= 1

                       
   

                colunas.append(linhas)  
    except:
        print('Something went wrong')
        

    #

    driver.close()

Atualizar_Rela() # Calling the first loop

def task():   
    now = time.strftime("%M")
    now2 = time.strftime("%S")

    # Calling the function for each 5 minutes and 31 seconds
    if int(now) % 5 == 0 and int(now2) % 30 == 1:
        Atualizar_Rela()

    if int(now2) % 2 == 0:
        for x in range(len(canvascolor)):
            canvas[x].configure(bg=canvascolor[x])
    else:
        for x in range(len(canvascolor)):
            canvas[x].configure(bg="yellow")


    root.after(1000, task)  # reschedule event in 2 seconds


root.after(0, task)
root.mainloop()
