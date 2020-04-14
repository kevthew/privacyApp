from guizero import *
import random

#PASSWORD CREATOR
def passwords():
    
    app.hide()
    
    window1.show()
   
    app.display()
   
def get_passwords():
    
    chars2 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,.<>/?;:\"\'|\\[{]}=+-_)(*&^%$#@!`~"
    chars1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars= ""
    
    num = int(input_box.value)

    length = int(input_box2.value)
    
    passwords = []
    
    if chars_box.value == 1:
        chars = chars2
    elif chars_box.value == 0:
        chars = chars1

    for p in range(num):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)
        password= str(password)
        passwords.append(password)
        
        printpass = TextBox(window1, text="\n".join(passwords), width=20, height=8, grid=[0,7], multiline=True, enabled=False, scrollbar=True)

#CEASER CYPHER
def ceaser():
    
    app.hide()
    
    window2.show()
    
    app.display()
   

def code():
    
    window2.hide()
    
    window3.show()
    
    app.display()
    
def code_message():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums='0123456789'
    key=numkey1.value
    key=(int(key))
    
    newMessage = ''
  
    message = uc_message.value
  
    for character in message:
        if character in alphabet:
            position=alphabet.find(character)
            newPosition=(position+key) %26
            newCharacter=alphabet[newPosition]
            newMessage += newCharacter
        elif character in alphabet2:
            position=alphabet2.find(character)
            newPosition=(position+key) %26
            newCharacter2=alphabet2[newPosition]
            newMessage += newCharacter2
        elif character in nums:
            position=nums.find(character)
            newPosition=(position+key) %10
            newCharacter3=nums[newPosition]
            newMessage += newCharacter3  
        else: 
            newMessage += character
      
    print(newMessage) 
    c_message = TextBox(window3, text=newMessage, align="right", width=20, height=10, grid=[0,2], multiline=True, enabled=False, scrollbar=True)

def decode():
    
    window2.hide()
    
    window4.show()
    
    app.display()

def decode_message():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums='0123456789'
    key= numkey.value
    key=(-int(key))
    
    newMessage = ''

    message = coded_message.value
    
    for character in message:
        if character in alphabet:
            position=alphabet.find(character)
            newPosition=(position+key) %26
            newCharacter=alphabet[newPosition]
            newMessage += newCharacter
        elif character in alphabet2:
            position=alphabet2.find(character)
            newPosition=(position+key) %26
            newCharacter2=alphabet2[newPosition]
            newMessage += newCharacter2  
        elif character in nums:
            position=nums.find(character)
            newPosition=(position+key) %10
            newCharacter3=nums[newPosition]
            newMessage += newCharacter3   
        else: 
            newMessage += character
    
    print(newMessage)
    dc_message = TextBox(window4, align="right", text=newMessage, width=20, height=10, grid=[0,2], multiline=True, enabled=False, scrollbar=True)

#GO BACK BUTTONS
def go_back():
    window1.hide()
    app.show()
    app.display()

def go_back2():
    window2.hide()
    app.show()
    app.display()
    
def go_back3():
    window3.hide()
    window2.show()
    app.display()
    
def go_back4():
    window4.hide()
    window2.show()
    app.display()
    
#MAIN GUI DISPLAY
app = App(title="Privacy App", width=400, height=400, layout="grid")
welcome_message = Text(app, text="PRIVACY APP!!!", grid=[0,0], align="top", size=40, font="Times New Roman", color="blue")
button1 = PushButton(app, command=passwords, text="Password Creator", grid=[0,1])
button2 = PushButton(app, command=ceaser, text="Simple Coder", grid=[0,3])

#PASSWORD MAIN WINDOW
window1 = Window(app, title="Privacy App", width=400, height=400, layout="grid")
welcome_message = Text(window1, text="Password Creator!", grid=[0,0], align="top", size=40, font="Times New Roman", color="blue")
instruction1 = Text(window1, text="How many passwords?", grid=[0,1], align="top", size=16, font="Times New Roman", color="blue")
input_box = TextBox(window1, grid=[0,2])
instruction2 = Text(window1, text="How many characters?", grid=[0,3], align="top", size=16, font="Times New Roman", color="blue")
input_box2 = TextBox(window1, grid=[0,4])
chars_box = CheckBox(window1, text="Special Characters?(e.g !@&*)", grid=[0,5])
button5 = PushButton(window1, command=get_passwords, text="GET", grid=[0,6])
back_button = PushButton(window1, command=go_back, text="GO BACK", grid=[0,8])
window1.hide()

#CEASER MAIN WINDOW
window2 = Window(app, title="Privacy App", width=400, height=400, layout="grid")
welcome_message = Text(window2, text="Code! or Decode!", grid=[0,0], align="top", size=40, font="Times New Roman", color="blue")
button3 = PushButton(window2, command=code, text="Code", grid=[0,1])
button4 = PushButton(window2, command=decode, text="Decoder", grid=[0,3])
back_button2 = PushButton(window2, command=go_back2, text="GO BACK", grid=[0,4])
window2.hide()

#CODER WINDOW
window3 = Window(app, title="Privacy App", width=400, height=400, layout="grid")
welcome_message = Text(window3, text="Message Coder!", grid=[0,0], align="top", size=40, font="Times New Roman", color="blue")
title_uc = Text(window3, text="Message", grid=[0,1], align="left", size=20, font="Times New Roman", color="blue")
title_c = Text(window3, text="Coded Message", grid=[0,1], align="right", size=20, font="Times New Roman", color="blue")
uc_message = TextBox(window3, align="left", width=20, height=10, grid=[0,2], multiline=True, scrollbar=True)
numkey_title = Text(window3, text="Secret Number", grid=[0,5], size=20, font="Times New Roman", color="blue")
numkey1 = TextBox(window3, grid=[0,6])
button6 = PushButton(window3, command=code_message, text="CODE", grid=[0,7])
back_button3 = PushButton(window3, command=go_back3, text="GO BACK", grid=[0,8])
window3.hide()

#DECODER WINDOW
window4 = Window(app, title="Privacy App", width=400, height=400, layout="grid")
welcome_message = Text(window4, text="Message Decoder!", grid=[0,0], align="top", size=36, font="Times New Roman", color="blue")
title_coded = Text(window4, text="Coded Message", grid=[0,1], align="left", size=20, font="Times New Roman", color="blue")
title_uncoded = Text(window4, text="Message", grid=[0,1], align="right", size=20, font="Times New Roman", color="blue")
coded_message = TextBox(window4, align="left", width=20, height=10, grid=[0,2], multiline=True, scrollbar=True)
numkey_title = Text(window4, text="Secret Number", grid=[0,5], size=20, font="Times New Roman", color="blue")
numkey = TextBox(window4, grid=[0,6])
button7 = PushButton(window4, command=decode_message, text="DECODE", grid=[0,7])
back_button4 = PushButton(window4, command=go_back4, text="GO BACK", grid=[0,8])
window4.hide()

app.display()