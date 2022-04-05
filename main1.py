from pynput.mouse import Button, Controller
from resize import resize
import time
import pyautogui
import os
from pathlib import Path
path = Path('settings/my_screenshot.png')
class RouletteBot():
    def __init__(self):
        self.__mouse = Controller()    # Initializare controler

        # Initiazare variabile
        self.__screenshot = None
        self.__previous_colors = []
        self.jocuri_castigate = 0
        self.prev1=" "
        self.prev2=" "
        self.prev3=" "
        self.prev4=" "
        self.prev5=" "
        self.prev6=" "
        self.prev7=" "
        self.prev8=" "
        self.prev9=" "
        self.prev10=" "
        
        self.__red_color = "red"      
        self.__black_color = "black"     
        self.__green_color = "green"       
        self.__pos_result = 399,290        # Pozitia culorii rezultate
        self.__pos_rotire = 409,452        # Pozitia butonului de rotire
        self.__pos_stop = 391,453          # Pozitia butonului de stop
        self.__pos_betblack = 340,404      # Pozitia butonului pentru culoarea neagra
        self.__pos_betred = 277,403        # Pozitia butonului pentru culoarea rosie
        self.__pos_double_bet = 95,454    # Pozitia butonului pentru dublarea pariului anterior
        self.__pos_ok = 494,81             # Pozitia butonului de ok

    
    def screenshot(self):           # Se executa un screenshot, imaginea rezultata va fi stocata in path
        self.__screenshot = pyautogui.screenshot(path)
    def pariuriwins(self):
        return self.jocuri_castigate
    def go_on(self):
        #rotire,rotire,stop
        time.sleep(0.5)
        self.__mouse.position = (self.__pos_rotire)
        self.__mouse.click(Button.left, 1)
        time.sleep(0.5)
        self.__mouse.position = (self.__pos_rotire)
        self.__mouse.click(Button.left, 1)
        time.sleep(0.5)
        self.__mouse.position = (self.__pos_stop)
        self.__mouse.click(Button.left, 1)
        
    def get_info(self):
        # La fiecare ora, apare un pop-up box care ne avertizeaza ca jucam de X ore
        # Functia aceasta inchide acea avertizare
        pixel1 = self.__screenshot.getpixel((self.__pos_ok[0], self.__pos_ok[1]))
        
        if pixel1[0]>200 and pixel1[1]>200:
            self.__mouse.position = (self.__pos_ok)
            self.__mouse.click(Button.left, 1)
    def get_last_color(self):
        # Atribuim culori pentru rgb-ul din screenshot la pozitia culorii rezultate
        pixel = self.__screenshot.getpixel((self.__pos_result[0], self.__pos_result[1]))
        rgb = (pixel[0], pixel[1], pixel[2])
        if pixel[0] > 200 and pixel[1]>30:
            rgbcolor = "red"
        elif pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
            rgbcolor = "black"
        else:
            rgbcolor = "green"
        #print(rgb)
        
        
        if rgbcolor in self.__black_color:
            self.__previous_colors.append("black")
            print("black")
        elif rgbcolor in self.__red_color:
            self.__previous_colors.append("red")
            print("red")
        elif rgbcolor in self.__green_color:
            self.__previous_colors.append("green")
            print("green")

    # Functia pentru 2 culori consecutive.
    def gamemode_2(self):
        
        if len(self.__previous_colors) >= 2:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.jocuri_castigate+=1

            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.jocuri_castigate+=1
                
    def gamemode_3(self):
        
        if len(self.__previous_colors) >= 3:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.jocuri_castigate+=1        
    def gamemode_4(self):
        
        if len(self.__previous_colors) >= 4:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.jocuri_castigate+=1        

    def gamemode_5(self):
        
        if len(self.__previous_colors) >= 5:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.jocuri_castigate+=1
    def gamemode_6(self):
        
        if len(self.__previous_colors) >= 6:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black" and self.__previous_colors[-6]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                self.prev6="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red" and self.__previous_colors[-6]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                self.prev6="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.jocuri_castigate+=1
    def gamemode_7(self):
        
        if len(self.__previous_colors) >= 7:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black" and self.__previous_colors[-6]=="black" and self.__previous_colors[-7]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                self.prev6="black"
                self.prev7="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red" and self.__previous_colors[-6]=="red" and self.__previous_colors[-7]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                self.prev6="red"
                self.prev7="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.jocuri_castigate+=1

    def gamemode_8(self):
        
        if len(self.__previous_colors) >= 8:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black" and self.__previous_colors[-6]=="black" and self.__previous_colors[-7]=="black" and self.__previous_colors[-8]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                self.prev6="black"
                self.prev7="black"
                self.prev8="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red" and self.__previous_colors[-6]=="red" and self.__previous_colors[-7]=="red" and self.__previous_colors[-8]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                self.prev6="red"
                self.prev7="red"
                self.prev8="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.jocuri_castigate+=1
    def gamemode_9(self):
        
        if len(self.__previous_colors) >= 9:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black" and self.__previous_colors[-6]=="black" and self.__previous_colors[-7]=="black" and self.__previous_colors[-8]=="black" and self.__previous_colors[-9]=="black":
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                self.prev6="black"
                self.prev7="black"
                self.prev8="black"
                self.prev9="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red" and self.__previous_colors[-6]=="red" and self.__previous_colors[-7]=="red" and self.__previous_colors[-8]=="red" and self.__previous_colors[-9]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                self.prev6="red"
                self.prev7="red"
                self.prev8="red"
                self.prev9="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black"and self.prev9=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black" and self.prev9=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.prev9=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red" and self.prev9=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red" and self.prev9=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.prev9=" "
                self.jocuri_castigate+=1
    def gamemode_10(self):
        
        if len(self.__previous_colors) >= 10:
            if self.__previous_colors[-1]=="black" and self.__previous_colors[-2]=="black" and self.__previous_colors[-3]=="black" and self.__previous_colors[-4]=="black" and self.__previous_colors[-5]=="black" and self.__previous_colors[-6]=="black" and self.__previous_colors[-7]=="black" and self.__previous_colors[-8]=="black" and self.__previous_colors[-9]=="black" and self.__previous_colors[-10]=="black" :
                #click on joc dinou, red, rotire, stop , get color ball
                self.prev1="black"
                self.prev2="black"
                self.prev3="black"
                self.prev4="black"
                self.prev5="black"
                self.prev6="black"
                self.prev7="black"
                self.prev8="black"
                self.prev9="black"
                self.prev10="black"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betred)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
                

            if self.__previous_colors[-1]=="red" and self.__previous_colors[-2]=="red" and self.__previous_colors[-3]=="red" and self.__previous_colors[-4]=="red" and self.__previous_colors[-5]=="red" and self.__previous_colors[-6]=="red" and self.__previous_colors[-7]=="red" and self.__previous_colors[-8]=="red" and self.__previous_colors[-9]=="red" and self.__previous_colors[-10]=="red":
                #click on joc dinou, red, rotire, stop, get last color
                self.prev1="red"
                self.prev2="red"
                self.prev3="red"
                self.prev4="red"
                self.prev5="red"
                self.prev6="red"
                self.prev7="red"
                self.prev8="red"
                self.prev9="red"
                self.prev10="red"
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_betblack)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_rotire)
                self.__mouse.click(Button.left, 1)
                time.sleep(1)
                self.__mouse.position = (self.__pos_stop)
                self.__mouse.click(Button.left, 1)
                time.sleep(4)
                self.screenshot()
                self.get_last_color()
               
            
            if self.__previous_colors[-1]!="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black"and self.prev9=="black" and self.prev10=="black":
                #double 
                while self.__previous_colors[-1]!="red":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)

            if self.__previous_colors[-1]=="red" and self.prev1=="black" and self.prev2=="black" and self.prev3=="black" and self.prev4=="black" and self.prev5=="black" and self.prev6=="black" and self.prev7=="black" and self.prev8=="black" and self.prev9=="black" and self.prev10=="black":
                #win
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.prev9=" "
                self.prev10=" "
                self.jocuri_castigate+=1
            
            if self.__previous_colors[-1]!="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red" and self.prev9=="red" and self.prev10=="red":
                #double 
                
                while self.__previous_colors[-1]!="black":
                    self.__mouse.position = (self.__pos_double_bet)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(0.5)
                    self.__mouse.position = (self.__pos_stop)
                    self.__mouse.click(Button.left, 1)
                    time.sleep(2)
                    self.screenshot()
                    time.sleep(2)
                    self.get_last_color()
                    time.sleep(2)
                
            if self.__previous_colors[-1]=="black" and self.prev1=="red" and self.prev2=="red" and self.prev3=="red" and self.prev4=="red" and self.prev5=="red" and self.prev6=="red" and self.prev7=="red" and self.prev8=="red" and self.prev9=="red" and self.prev10=="red":
                #win 
                time.sleep(1)
                self.prev1=" "
                self.prev2=" "
                self.prev3=" "
                self.prev4=" "
                self.prev5=" "
                self.prev6=" "
                self.prev7=" "
                self.prev8=" "
                self.prev9=" "
                self.prev10=" "
                self.jocuri_castigate+=1
    
    
