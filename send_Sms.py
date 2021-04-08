import requests
import json
from tkinter import *
from tkinter.messagebox import showerror,showinfo

def send_sms(number,msg):
    url=" https://www.fast2sms.com/dev/bulkV2"
    params={
        'authorization': 'H0Cisj2I6NdlZAqzgWUDbT9PYyGt7kR8nvoEJe4MFxchQOXLufMyvDch28frZCAT4FozmeSuBGbnN15O',
        'route' : 'q',
        'sender_id': 'CHKSMS',
        'message': msg,
        'language': 'English',
        'numbers': number,
    }
    response=requests.get(url,params=params)
    dic = response.json()
    print(dic)
    return dic.get("return")

# send_sms('9021883355',"Hello I am Test SMS")

def btn_click():
    num=textnumber.get()
    msg=textmsg.get("1.0",END)
    r=send_sms(num, msg)
    if r:
        showinfo("Success","Message Send Successfully")
    else:
        showerror("Error","Something Went Wrong")




#Creating GUI
root=Tk()
root.title=("Message")
root.geometry("400x500")
font=("Helvetica",20,"bold")

Reciver = Label(root,text = "TO").place(x = 20)  
textnumber=Entry(root,font=font),padx=20)

Recivermsg = Label(root,text = "Message").place(x = 20,y=55)  
textmsg=Text(root)
textmsg.pack(fill=X,padx=20)

sendbtn=Button(root,text="Send SMS",command=btn_click)
sendbtn.pack()

root.mainloop()
