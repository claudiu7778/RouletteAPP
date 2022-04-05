
import tkinter as tk
from tkinter import ttk
from main1 import RouletteBot
from resize import resize
from tkinter.messagebox import showinfo
import time
import MySQLdb
import sshtunnel
from threading import *
from parolesecrete import SSH_PASS, SSH_USER, SSH_ADDRESS, MYSQL_DB, MYSQL_USER, MYSQL_PASS
import sys
import atexit

sshtunnel.SSH_TIMEOUT = 500
sshtunnel.TUNNEL_TIMEOUT = 500
conectat=0

jocuri_castigate=0
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('RouletteBot')

var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
var10 = tk.IntVar()

style = ttk.Style()
style.theme_use('clam')
stopper=False
username = tk.StringVar()
password = tk.StringVar()
 # Sign in 
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
user_label = ttk.Label(signin, text="Nume de utilizator:")
user_label.pack(fill='x', expand=True)

user_entry = ttk.Entry(signin, textvariable=username)
user_entry.pack(fill='x', expand=True)
user_entry.focus()

# password
password_label = ttk.Label(signin, text="Parola:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)
# login button
def my_exit_func():
    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username=SSH_USER, ssh_password=SSH_PASS,
        remote_bind_address=(SSH_ADDRESS, 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user=MYSQL_USER,
            passwd=MYSQL_PASS,
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=MYSQL_DB,
        )
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM accs WHERE username = %s AND passwd = %s', (username.get(), password.get(),))
        cursor.execute(
        'UPDATE accs SET conectat = 0 WHERE username = %s AND passwd = %s', (username.get(), password.get(),)) 
        cursor.close()
        connection.commit()
atexit.register(my_exit_func)

def login_clicked():
    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username=SSH_USER, ssh_password=SSH_PASS,
        remote_bind_address=(SSH_ADDRESS, 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user=MYSQL_USER,
            passwd=MYSQL_PASS,
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=MYSQL_DB,
        )
        cursor = connection.cursor()
        
        checkLogin = cursor.execute('SELECT * FROM accs WHERE username = %s AND passwd = %s', (username.get(), password.get(),))
        cursor.execute(
        'SELECT conectat FROM accs WHERE username = %s AND passwd = %s', (username.get(), password.get(),)) 
        
        checkConectat = cursor.fetchone()       
        
        # Daca username-ul si parola sunt valide, iar jucatorul nu este conectat
        if checkLogin == 1 and 0 in checkConectat:
            
            cursor.execute('UPDATE accs SET conectat = 1 WHERE username = %(username)s', { 'username' : username.get() })
            global conectat
            conectat= 1
            # jucatorul va avea starea de 'conectat'
            cursor.close()
            connection.commit()
    # inchidem conexiunea cu baza de date 
    # Daca username-ul si parola sunt valide, iar jucatorul are starea de 'conectat' atunci se 'construieste' GUI-ul, am creat 2 thread-uri deoarece programul se bloca la un moment dat
    if checkLogin == 1 and conectat == 1:
        def threading():
            
            t1=Thread(target=start)
            t1.daemon=True
            t1.start()
            if stopper == True:
                t1.join()
        def threading1():
            t2=Thread(target=stop)
            t2.daemon=True
            t2.start()
        showinfo(
            title="RouletteBot",
            message="Te-ai logat cu succes!"
        )
        # Cream interfata grafica
        password_label.after(1000, password_label.destroy())
        password_entry.after(1000, password_entry.destroy())
        user_label.after(1000, user_label.destroy())
        user_entry.after(1000, user_entry.destroy())
        login_button.after(1000, login_button.destroy())
        signin.after(1000, signin.destroy())
        ttk.Checkbutton(root,
                text='2 culori consecutive',
                variable=var2,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='3 culori consecutive',
                
                variable=var3,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='4 culori consecutive',
                
                variable=var4,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='5 culori consecutive',
                
                variable=var5,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='6 culori consecutive',
                
                variable=var6,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='7 culori consecutive',
                
                variable=var7,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='8 culori consecutive',
                
                variable=var8,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='9 culori consecutive',
                
                variable=var9,
                onvalue=1,
                offvalue=0).pack()
        ttk.Checkbutton(root,
                text='10 culori consecutive',
                
                variable=var10,
                onvalue=1,
                offvalue=0).pack()
        # Cand apasam pe butonul de exit, 'conectat' devine 0, si se trece in baza de date nr de pariuri castigate in aceasta sesiune, dupa care se iese din program

        def stop():
            if conectat == 1:
                global stopper
                stopper=True
                
                with sshtunnel.SSHTunnelForwarder(
                        ('ssh.pythonanywhere.com'),
                        ssh_username=SSH_USER, ssh_password=SSH_PASS,
                        remote_bind_address=(SSH_ADDRESS, 3306)
                    ) as tunnel:
                        connection = MySQLdb.connect(
                            user=MYSQL_USER,
                            passwd=MYSQL_PASS,
                            host='127.0.0.1', port=tunnel.local_bind_port,
                            db=MYSQL_DB,
                        )
                        cursor = connection.cursor()
                        cursor.execute('UPDATE accs SET conectat = 0 WHERE username = %(username)s', { 'username' : username.get() })
                        cursor.execute('UPDATE accs SET pariuri_castigate = pariuri_castigate + %s WHERE username = %s', (jocuri_castigate,username.get(),))
                        cursor.close()
                        connection.commit()
                root.destroy()
                        
           
            
        def start():
            # Am pus acel stopper de multe ori deoarece doream ca, atunci cand apas pe EXIT, primul thread sa se opreasca din functiune mult mai rapid
            resize()
            bot = RouletteBot()
            global jocuri_castigate
            while True:
                if stopper:
                    break
                if var2.get() == 1:

                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break                        
                        time.sleep(4)
                        bot.gamemode_2()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                    
                if var3.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_3()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var4.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_4()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var5.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_5()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var6.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_6()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var7.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_7()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var8.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_8()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var9.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_9()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                if var10.get() == 1:
                    
                        time.sleep(3)
                        bot.screenshot()
                        bot.get_last_color()
                        if stopper:
                            break
                        time.sleep(4)
                        bot.gamemode_10()
                        if stopper:
                            break
                        time.sleep(3)
                        bot.go_on()
                        bot.get_info()
                        jocuri_castigate = bot.pariuriwins()
                
        startbtn = ttk.Button(root, text ="START", command = threading)
        startbtn.place(x=220,y=80)

        stopbtn = ttk.Button(root, text ="EXIT", command = threading1)
        stopbtn.place(x=220,y=140)
                
    elif checkLogin == 1 and 1 in checkConectat:
        showinfo(
            title="RouletteBot",
            message="Esti deja conectat."
        )
    else:
        showinfo(
            title="RouletteBot",
            message="Nume sau parola incorecta."
        )
        
    
login_button = ttk.Button(signin, text="Logare", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)    


root.mainloop()


    



