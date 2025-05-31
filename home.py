import csv
import datetime
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from PIL import ImageTk
from skimage.io import imread
import numpy as np
import matplotlib.pylab as plt
from tkinter.ttk import Treeview
import time
import cv2
from tkinter import Tk, messagebox, ttk
from tkinter import *

from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import numpy as np
import tkinter.simpledialog
from sample_data import student


class ar_crop_recommendation():
    image=''
    path=''
    gray=''
    fname=''
    feature_value=0
    username=''
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Crop Recommendation'
        self.titlec = 'CROP RECOMMENDATION'
        self.backround_color = '#c4732b'
        self.text_color = '#FFF'
        self.backround_image = r'images/background_hd.jpg'
        self.account_no=''
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def get_account_no(self):
        return self.account_no
    def set_account_no(self,acc):
        self.account_no=acc
    def home_window(self):
        home_window_root=Tk()
        w = 950
        h = 600
        ws = home_window_root.winfo_screenwidth()
        hs = home_window_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        home_window_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        home_window_root.title(self.title)
        home_window_root.resizable(False, False)
        bg1 = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(home_window_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg1, anchor=NW)
        canvas.create_text(470, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def clickHandler(event):
            tt = ar_crop_recommendation
            tt.select_dataset(event)
        image1 = Image.open('images/crop.png')
        img1 = image1.resize((200, 200))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(470, 270, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler)
        ###
        admin_id = canvas.create_text(480, 400, text="START ANALYSIS", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        ###
        home_window_root.mainloop()

    def select_dataset(self):
        select_dataset_root = Toplevel()
        select_dataset_root.attributes('-topmost', 'true')
        get_data = ar_crop_recommendation()
        w = 950
        h = 600
        ws = select_dataset_root.winfo_screenwidth()
        hs = select_dataset_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        select_dataset_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        select_dataset_root.title(get_data.get_title())
        select_dataset_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(select_dataset_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="CROP RECOMMENDATION", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 200, text="PATH", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 325, text="FILE", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        e1 = Entry(select_dataset_root, font=('times', 15, ' bold '), width=40)
        canvas.create_window(480, 200, window=e1)
        e2 = Entry(select_dataset_root, font=('times', 15, ' bold '), width=40)
        canvas.create_window(480, 325, window=e2)

        def select_image():
            dir = r'data'
            if not os.path.exists(dir):
                os.mkdir(dir)
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            if not os.path.exists(dir):
                os.makedirs(dir)
            csv_file_path = askopenfilename(parent=select_dataset_root)
            fpath = os.path.dirname(os.path.abspath(csv_file_path))
            fname = (os.path.basename(csv_file_path))
            fsize = os.path.getsize(csv_file_path)
            e1.delete(0, END)
            e1.insert(0, fpath)
            e2.insert(0, fname)
            get_data.path = os.path.abspath(csv_file_path)
            destination = os.path.join("data", "input.csv")
            print(destination)
            shutil.copy(os.path.abspath(csv_file_path), destination)

        def next_image():
            select_dataset_root.destroy()
            tt = ar_crop_recommendation()
            tt.read_dataset()

        b1 = Button(select_dataset_root, text='Select Dataset', command=select_image, font=('times', 15, ' bold '),
                    width=20)
        canvas.create_window(300, 425, window=b1)
        b2 = Button(select_dataset_root, text='Next', command=next_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 425, window=b2)
        select_dataset_root.mainloop()

    def read_dataset(self):
        read_dataset_root = Toplevel()
        get_data = ar_crop_recommendation()
        read_dataset_root.attributes('-topmost', 'true')
        w = 950
        h = 600
        ws = read_dataset_root.winfo_screenwidth()
        hs = read_dataset_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        read_dataset_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        read_dataset_root.title(get_data.get_title())
        read_dataset_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(read_dataset_root, width=200, height=450)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(410, 70, text="READ DATASET", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        def read_data():
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=(
            "N", "P", "K", "temperature", "humidity", "ph", "rainfall", "NuContAvailable", "AvMoisture%", "AvN%(dry)",
            "AvP%(dry)", "AvK%(dry)","soil Type"), yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)

            tree.heading('N', text="N", anchor=W)
            tree.heading('P', text="P", anchor=W)
            tree.heading('K', text="K", anchor=W)
            tree.heading('temperature', text="temperature", anchor=W)
            tree.heading('humidity', text="humidity", anchor=W)
            tree.heading('ph', text="ph", anchor=W)
            tree.heading('rainfall', text="rainfall", anchor=W)
            tree.heading('NuContAvailable', text="NuContAvailable", anchor=W)
            tree.heading('AvMoisture%', text="AvMoisture%", anchor=W)
            tree.heading('AvN%(dry)', text="AvN%(dry)", anchor=W)
            tree.heading('AvP%(dry)', text="AvP%(dry)", anchor=W)
            tree.heading('AvK%(dry)', text="AvK%(dry)", anchor=W)
            tree.heading('soil Type', text="soil Type", anchor=W)

            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)
            tree.column('#4', width=100)
            tree.column('#5', width=100)
            tree.column('#6', width=100)
            tree.column('#7', width=100)
            tree.column('#8', width=100)
            tree.column('#9', width=100)
            tree.column('#10', width=100)
            tree.column('#11', width=100)
            tree.column('#12', width=100)
            tree.pack()
            file = 'data/input.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['N']
                    t2 = row['P']
                    t3 = row['K']
                    t4 = row['temperature']
                    t5 = row['humidity']
                    t6 = row['ph']
                    t7 = row['rainfall']

                    t8 = row['NuContAvailable']
                    t9 = row['AvMoisture%']
                    t10 = row['AvN%(dry)']
                    t11 = row['AvP%(dry)']
                    t12 = row['AvK%(dry)']
                    t13 = row['soil Type']

                    tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13))
        b1 = Button(read_dataset_root, text='Read Dataset', command=read_data, font=('times', 15, ' bold '), width=20)
        canvas.create_window(300, 475, window=b1)
        def next_page():
            read_dataset_root.destroy()
            tt = ar_crop_recommendation()
            tt.missing_values()
        b2 = Button(read_dataset_root, text='Next', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 475, window=b2)
        read_dataset_root.mainloop()
    def missing_values(self):
        missing_values_root = Toplevel()
        get_data = ar_crop_recommendation()
        missing_values_root.attributes('-topmost', 'true')
        w = 950
        h = 600
        ws = missing_values_root.winfo_screenwidth()
        hs = missing_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        missing_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        missing_values_root.title(get_data.get_title())
        missing_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(missing_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(410, 70, text="Missing Values", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        def read_data():
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=(
                "N", "P", "K", "temperature", "humidity", "ph", "rainfall", "NuContAvailable", "AvMoisture%",
                "AvN%(dry)",
                "AvP%(dry)", "AvK%(dry)","soil Type"), yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)

            tree.heading('N', text="N", anchor=W)
            tree.heading('P', text="P", anchor=W)
            tree.heading('K', text="K", anchor=W)
            tree.heading('temperature', text="temperature", anchor=W)
            tree.heading('humidity', text="humidity", anchor=W)
            tree.heading('ph', text="ph", anchor=W)
            tree.heading('rainfall', text="rainfall", anchor=W)
            tree.heading('NuContAvailable', text="NuContAvailable", anchor=W)
            tree.heading('AvMoisture%', text="AvMoisture%", anchor=W)
            tree.heading('AvN%(dry)', text="AvN%(dry)", anchor=W)
            tree.heading('AvP%(dry)', text="AvP%(dry)", anchor=W)
            tree.heading('AvK%(dry)', text="AvK%(dry)", anchor=W)
            tree.heading('soil Type', text="soil Type", anchor=W)
            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)
            tree.column('#4', width=100)
            tree.column('#5', width=100)
            tree.column('#6', width=100)
            tree.column('#7', width=100)
            tree.column('#8', width=100)
            tree.column('#9', width=100)
            tree.column('#10', width=100)
            tree.column('#11', width=100)
            tree.column('#12', width=100)
            tree.pack()
            file = 'data/input.csv'
            with open(file) as f, open('data/missing.csv', 'w', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'NuContAvailable', 'AvMoisture%',
                'AvN%(dry)',
                'AvP%(dry)', 'AvK%(dry)','soil Type'])
                for row in reader:
                    # print row
                    t1 = row['N']
                    t2 = row['P']
                    t3 = row['K']
                    t4 = row['temperature']
                    t5 = row['humidity']
                    t6 = row['ph']
                    t7 = row['rainfall']
                    t8 = row['NuContAvailable']
                    t9 = row['AvMoisture%']
                    t10 = row['AvN%(dry)']
                    t11 = row['AvP%(dry)']
                    t12 = row['AvK%(dry)']
                    t13 = row['soil Type']
                    if ((t1 == "") or (t2 == "") or (t3 == "") or (t4 == "") or (t5 == "") or (t6 == "") or (
                            t7 == "") or (t8 == "") or (t9 == "") or (t10 == "") or (t11 == "") or (t12 == "")or (t13 == "")):
                        print("yes")
                    else:
                        tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13))
                        filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13])
        b1 = Button(missing_values_root, text='Missing Values', command=read_data, font=('times', 15, ' bold '),
                    width=20)
        canvas.create_window(300, 475, window=b1)
        def next_page():
            missing_values_root.destroy()
            tt = ar_crop_recommendation()
            tt.irrelevant_values()
        b2 = Button(missing_values_root, text='Next', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 475, window=b2)
        missing_values_root.mainloop()

    def irrelevant_values(self):
        irrelevant_values_root = Toplevel()
        get_data = ar_crop_recommendation()
        irrelevant_values_root.attributes('-topmost', 'true')
        w = 950
        h = 600
        ws = irrelevant_values_root.winfo_screenwidth()
        hs = irrelevant_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        irrelevant_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        irrelevant_values_root.title(get_data.get_title())
        irrelevant_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(irrelevant_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(410, 70, text="Irrelevant Values", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())

        def read_data():
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=(
                "N", "P", "K", "temperature", "humidity", "ph", "rainfall", "NuContAvailable", "AvMoisture%",
                "AvN%(dry)",
                "AvP%(dry)", "AvK%(dry)","soil Type"), yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            tree.heading('N', text="N", anchor=W)
            tree.heading('P', text="P", anchor=W)
            tree.heading('K', text="K", anchor=W)
            tree.heading('temperature', text="temperature", anchor=W)
            tree.heading('humidity', text="humidity", anchor=W)
            tree.heading('ph', text="ph", anchor=W)
            tree.heading('rainfall', text="rainfall", anchor=W)
            tree.heading('NuContAvailable', text="NuContAvailable", anchor=W)
            tree.heading('AvMoisture%', text="AvMoisture%", anchor=W)
            tree.heading('AvN%(dry)', text="AvN%(dry)", anchor=W)
            tree.heading('AvP%(dry)', text="AvP%(dry)", anchor=W)
            tree.heading('AvK%(dry)', text="AvK%(dry)", anchor=W)
            tree.heading('soil Type', text="soil Type", anchor=W)
            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)
            tree.column('#4', width=100)
            tree.column('#5', width=100)
            tree.column('#6', width=100)
            tree.column('#7', width=100)
            tree.column('#8', width=100)
            tree.column('#9', width=100)
            tree.column('#10', width=100)
            tree.column('#11', width=100)
            tree.column('#12', width=100)
            tree.pack()
            file = 'data/missing.csv'
            with open(file) as f, open('data/irrelevant.csv', 'w', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'NuContAvailable', 'AvMoisture%',
                     'AvN%(dry)',
                     'AvP%(dry)', 'AvK%(dry)','soil Type'])
                for row in reader:
                    # print row
                    t1 = row['N']
                    t2 = row['P']
                    t3 = row['K']
                    t4 = row['temperature']
                    t5 = row['humidity']
                    t6 = row['ph']
                    t7 = row['rainfall']
                    t8 = row['NuContAvailable']
                    t9 = row['AvMoisture%']
                    t10 = row['AvN%(dry)']
                    t11 = row['AvP%(dry)']
                    t12 = row['AvK%(dry)']
                    t13 = row['soil Type']

                    if ((t1.isdigit() == False) or (t2.isdigit() == False) or (t3.isdigit() == False)):
                        dd = 0
                    else:
                        tree.insert("", 0, values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13))
                        filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12,t13])

        b1 = Button(irrelevant_values_root, text='Irrelevant Values', command=read_data, font=('times', 15, ' bold '),
                    width=20)
        canvas.create_window(300, 475, window=b1)

        def next_page():
            irrelevant_values_root.destroy()
            tt = ar_crop_recommendation()
            tt.attribut_extraction()

        b2 = Button(irrelevant_values_root, text='Next', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 475, window=b2)
        irrelevant_values_root.mainloop()


    def attribut_extraction(self):
        attribut_extraction_root = Toplevel()
        get_data = ar_crop_recommendation()
        attribut_extraction_root.attributes('-topmost', 'true')
        w = 950
        h = 600
        ws = attribut_extraction_root.winfo_screenwidth()
        hs = attribut_extraction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        attribut_extraction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        attribut_extraction_root.title(get_data.get_title())
        attribut_extraction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(attribut_extraction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(410, 70, text="Attribute Extraction", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        def read_data():
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=( "temperature", "humidity", "ph", "rainfall","soil Type"), yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)

            tree.heading('temperature', text="temperature", anchor=W)
            tree.heading('humidity', text="humidity", anchor=W)
            tree.heading('ph', text="ph", anchor=W)
            tree.heading('rainfall', text="rainfall", anchor=W)
            tree.heading('soil Type', text="soil Type", anchor=W)

            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)
            tree.column('#4', width=100)

            tree.pack()
            file = 'data/irrelevant.csv'
            with open(file) as f, open('data/attributes.csv', 'w', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow( ['temperature', 'humidity', 'ph', 'rainfall','soil Type'])
                for row in reader:
                    t4 = row['temperature']
                    t5 = row['humidity']
                    t6 = row['ph']
                    t7 = row['rainfall']
                    t8 = row['soil Type']
                    tree.insert("", 0, values=(t4, t5, t6, t7,t8))
                    filewriter.writerow([t4, t5, t6, t7,t8])
        b1 = Button(attribut_extraction_root, text='Attributes Extraction', command=read_data, font=('times', 15, ' bold '), width=20)
        canvas.create_window(300, 475, window=b1)
        def next_page():
            attribut_extraction_root.destroy()
            tt = ar_crop_recommendation()
            tt.random_forest()


        b2 = Button(attribut_extraction_root, text='Next', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 475, window=b2)
        attribut_extraction_root.mainloop()

    def random_forest(self):
        random_forest_root = Toplevel()
        get_data = ar_crop_recommendation()
        random_forest_root.attributes('-topmost', 'true')
        w = 950
        h = 600
        ws = random_forest_root.winfo_screenwidth()
        hs = random_forest_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        random_forest_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        random_forest_root.title(get_data.get_title())
        random_forest_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        random_forest_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        canvas = Canvas(random_forest_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(410, 70, text="Classification", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        obj = student

        def prediction():
            o1 = student
            left = range(o1.acid.__len__())
            height = o1.acid
            tick_label = o1.acid1
            plt1.bar(left, height, tick_label=tick_label,width=0.8, color=['red', 'red'])
            plt1.xlabel('x - axis')
            plt1.ylabel('y - axis')
            plt1.title('Acid')
            plt1.show()

        def graph2():
            o1 = student
            left1 = range(o1.neutral.__len__())
            height1 = o1.neutral
            tick_label1 = o1.neutral1
            plt2.bar(left1, height1, tick_label=tick_label1,
                     width=0.8, color=['green', 'green'])
            plt2.xlabel('x - axis')
            plt2.ylabel('y - axis')
            plt2.title('Neutral')
            plt2.show()
            ###

        def graph1():
            o1 = student
            left2 = range(o1.base.__len__())
            height2 = o1.base
            tick_label2 = o1.base1
            plt3.bar(left2, height2, tick_label=tick_label2, width=0.8, color=['red', 'red'])
            plt3.xlabel('x - axis')
            plt3.ylabel('y - axis')
            plt3.title('Base')
            plt3.show()

        def read_data():
            test_dict = {'lime soil': 0,  'Red Soil': 0, 'sandy': 0, 'silt': 0, 'Clay': 0, 'Loam': 0, 'Alluvial': 0, 'clay': 0, 'black': 0, 'chalk': 0}
            test_dict1 = {'lime soil': 0, 'Red Soil': 0, 'sandy': 0, 'silt': 0, 'Clay': 0, 'Loam': 0, 'Alluvial': 0, 'clay': 0, 'black': 0, 'chalk': 0}


            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=("soil Type","ph"),yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)

            tree.heading('soil Type', text="soil Type", anchor=W)
            tree.heading('ph', text="ph", anchor=W)
            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.pack()
            file = 'data/irrelevant.csv'
            with open(file) as f, open('data/random_forest.csv', 'w', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['temperature', 'humidity', 'ph', 'rainfall', 'soil Type'])
                for row in reader:
                    t2 = row['ph']
                    t1 = row['soil Type']
                    test_dict[t1]=test_dict[t1]+float(t2)
                    test_dict1[t1]=test_dict1[t1]+1
                    c = float(t2)
                    tree.insert("", 0, values=(t1, t2))
                    filewriter.writerow([t1, t2])

            # print(test_dict)
            # print(test_dict1)
            for x in test_dict:
                dd=test_dict[x]/test_dict1[x]
                test_dict[x]=dd
            print(test_dict)
            for x in test_dict:

                c=test_dict[x]
                t1=x
                print(x,c)

                if (c < 6):
                    obj.acid.append(c)
                    obj.acid1.append(t1)
                elif (c < 8):
                    obj.neutral.append(c)
                    obj.neutral1.append(t1)
                else:
                    obj.base.append(c)
                    obj.base1.append(t1)


            data = pd.read_csv('data/random_forest.csv')
            # print(data)
            x = data.iloc[:, 1:2].values
            # print(x)
            y = data.iloc[:, 1].values
            regressor = RandomForestRegressor(n_estimators=100, random_state=0)
            regressor.fit(x, y)
            X_grid = np.arange(min(x).item(), max(x).item(), 0.01)
            X_grid = X_grid.reshape((len(X_grid), 1))
            plt.scatter(x, y, color='blue')
            plt.plot(X_grid, regressor.predict(X_grid), color='green')
            plt.title('Random Forest')
            plt.xlabel('Position level')
            plt.ylabel('Values')
            plt.show()

        def recommented_crops():
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=850, height=300)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=("Soil type", "Crop","fertilizer", "harvest time"), yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)

            tree.heading('Soil type', text="Soil type", anchor=W)
            tree.heading('Crop', text="Crop", anchor=W)
            tree.heading('fertilizer', text="fertilizer", anchor=W)
            tree.heading('harvest time', text="harvest time", anchor=W)

            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=360)
            tree.pack()
            file = 'crop_details.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Soil type']
                    t2 = row['Crop']
                    t3 = row['fertilizer']
                    t4 = row['harvest time']
                    tree.insert("", 0, values=(t1, t2,t3,t4))


        compare_dataset = Button(random_forest_root, text="Prediction", width=15, command=read_data,
                                 height=1, fg="#FFF", bg="#004080", activebackground="#ff8000",
                                 activeforeground="white", font=('times', 15, ' bold '))
        compare_dataset.place(x=150, y=400)

        resust_dataset = Button(random_forest_root, command=prediction, text=" Prediction( Acid )", width=15,
                                height=1, fg="#FFF", bg="#004080", activebackground="#ff8000", activeforeground="white",
                                font=('times', 15, ' bold '))
        resust_dataset.place(x=450, y=400)

        resust_dataset = Button(random_forest_root, command=graph1, text="Prediction( Base )", width=15, height=1,
                                fg="#FFF", bg="#004080", activebackground="#ff8000", activeforeground="white",
                                font=('times', 15, ' bold '))
        resust_dataset.place(x=150, y=450)

        resust_dataset = Button(random_forest_root, command=graph2, text="Prediction( Neutral )", width=15,
                                height=1, fg="#FFF", bg="#004080", activebackground="#ff8000", activeforeground="white",
                                font=('times', 15, ' bold '))
        resust_dataset.place(x=450, y=450)

        resust_dataset = Button(random_forest_root, command=recommented_crops, text="Recommended Crops", width=15,
                                height=1, fg="#FFF", bg="#004080", activebackground="#ff8000", activeforeground="white",
                                font=('times', 15, ' bold '))
        resust_dataset.place(x=450, y=500)



        random_forest_root.mainloop()




ar=ar_crop_recommendation()
root=ar.home_window()