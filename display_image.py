"""
Copyright (c) 2024 Tomi Bilcu.

This work is licensed under the terms of the MIT license.  
For a copy, see LICENSE.txt.


Credit for Experience_In_AI from StackOverflow for the Tkinter code for sohwing live feed.
Rest of the code is made by myself.
https://stackoverflow.com/questions/66956444/live-video-feed-from-camera-to-tkinter-window-with-opencv/67161773#67161773
"""

import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import cv2

from detect_barcodes import read_barcode


ikkuna=tkinter.Tk()
ikkuna.title("Barcode reader")

frame=np.random.randint(0,255,[100,100,3],dtype='uint8')
img = ImageTk.PhotoImage(Image.fromarray(frame))

paneeli_image=tkinter.Label(ikkuna) #,image=img)
paneeli_image.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

message="Be ready to insert the barcode to the camera. \n When ready, press the start button"
paneeli_text=tkinter.Label(ikkuna,text=message)
paneeli_text.grid(row=1,column=1,pady=1,padx=10)

cam = cv2.VideoCapture(0)

def otakuva():
    global frame
    global cam
    #cam = cv2.VideoCapture(0)
    while (cam.isOpened()):
        ret, frame = cam.read()

        #Update the image to tkinter...
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        frame, check_for_barcodes = read_barcode(frame)

        if check_for_barcodes:
            on_closing()
            break
        

        img_update = ImageTk.PhotoImage(Image.fromarray(frame))
        paneeli_image.configure(image=img_update)
        paneeli_image.image=img_update
        paneeli_image.update()

        if not ret:
            print("failed to grab frame")
            break

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")

            cam.release()
            cv2.destroyAllWindows()
            break



def on_closing():
    global cam
    cam.release()
    cv2.destroyAllWindows()
    ikkuna.destroy()
    print("Stopped!")



painike_korkeus=10
painike_1=tkinter.Button(ikkuna,text="Start",command=otakuva,height=5,width=20)
painike_1.grid(row=1,column=0,pady=10,padx=10)
painike_1.config(height=1*painike_korkeus,width=20)

painike_korkeus=10
painike_1=tkinter.Button(ikkuna,text="Stop",command=on_closing,height=5,width=20)
painike_1.grid(row=1,column=2,pady=10,padx=10)
painike_1.config(height=1*painike_korkeus,width=20)


ikkuna.protocol("WM_DELETE_WINDOW", on_closing)

ikkuna.mainloop()