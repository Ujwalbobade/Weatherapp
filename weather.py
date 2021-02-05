from tkinter import *
from PIL import ImageTk,Image
import requests
import json
root=Tk()
root.title('Weather')
root.iconbitmap('D:/my_app/images/sky.ico')
root.geometry("250x50")

def clear():
    t.destroy()

def process():
    global e
    global t
    print(e.get())
    i=Label(root,text=e.get()).grid(row=2,sticky=W+S+E+N)
    t=Toplevel()
    t.title('Weather')
    t.iconbitmap('D:/my_app/images/sky.ico')
    
    try:
        #label1.pack_forget()
        api_re=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+e.get()+"&distance=10&API_KEY=962D3BBB-5CCB-4197-86B7-68478568A170")
        api= json.loads(api_re.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        Category=api[0]['Category']['Name']
        date=api[0]['DateObserved']

        if Category == 'Good':
            w_c="#0C0"
        elif  Category == 'Moderate':
            w_c="#FFFF00"
        elif  Category == 'Unhealthy for Sensitive Groups':
            w_c="#ff9900"
        elif  Category == 'Unhealthy':
            w_c="#FF0000"
        elif  Category == 'Very Unhealthy':
            w_c="#990066"
        elif  Category == 'Hazardous':
            w_c="#660000"
        #label1.delete(0,END)
        root.configure(background=w_c)
        label1=Label(t,text='Date :'+date+' City :'+city+'\nAir Quality :'+str(quality)+'   Condition :'+Category,font=('Helvetica',20),background=w_c).grid(row=0)
    except Exception as e:
        api='Error.....'
    



e=Entry(root,width=20)
e.insert(0,'Enter Zipcode')
e.grid(row=0,sticky=W+S+E+N)
button1=Button(root,text="sumbit",command=process).grid(row=0,column=1)
close=Button(root,text='close',command=clear).grid(row=0,column=2)



root.mainloop()