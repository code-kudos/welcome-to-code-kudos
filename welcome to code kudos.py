# Hi, I'm code kudos, this is simple welcome message using python & tkinter
## Hope you like it
### To see more like this Subscribe to 
#### Youtube: @codekudos
##### Instagram: @codekudos
###### Twitter: @code_kudos

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.tk_setPalette('#B6E2A1')

i = 0
msg=['|','C|','Co|','Cod|','Code|',
'Code |', 'Code K|','Code Ku|',
'Code Kud|', 'Code Kudo|','Code Kudos|']

welTxt = tk.Label(root, text='Welcome', font=('italic',50), fg='#497174')
welTxt.pack(pady=10)

welTxt = tk.Label(root, text='to', font=('italic',50), fg='#497')
welTxt.pack(pady=10)

txtAnimate = tk.Label(root, text='|', font=('italic',50), fg='#497174')
txtAnimate.pack(pady=20)

def animateText():
    global i
    if i<len(msg):
        txtAnimate.config(text=msg[i])
        i+=1
        root.after(600, animateText)
    else:
        i = 0
        txtAnimate.config(text='|')
        i+=1
        root.after(600,animateText)

root.after(1000,animateText)
root.mainloop()