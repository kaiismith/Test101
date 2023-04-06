import tkinter as tk
from FitnessProject.Control.logic import *
from FitnessProject.View.SignInPage import SignInPage
from PIL import ImageTk, Image
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import scrolledtext


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create background for Home Page
        self.frame_photo_4 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Home page (noti off).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_4)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)

        # Message Button
        self.message_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Message (off).png')
        message_button = tk.Button(self, image=self.message_image, bd=0, bg='#212121', activebackground='#212121', command=lambda: [Logic.delete_info_widgets(self), controller.show_frame('ChatPage')])
        message_button.place(x=29, y=339)

        # Stats Button
        self.stats_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Statistics.png')
        stats_button = tk.Button(self, image=self.stats_image, border=0, bg='#212121', activebackground='#212121', command=lambda: Logic.check_stats(self))
        stats_button.place(x=29, y=435.1)

        # Personal Settings Button
        self.user_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\User.png')
        user_button = tk.Button(self, image=self.user_image, border=0, bg='#212121', activebackground='#212121',
                                command=lambda: [Logic.delete_info_widgets(self), controller.show_frame('UpdateHealthInfoPage')])
        user_button.place(x=29, y=530.1)

        # Notification Button
        self.noti_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Notification (off).png')
        noti_button = tk.Button(self, image=self.noti_image, border=0, bg='#212121', activebackground='#212121')
        noti_button.place(x=29, y=625)

        # Log Out Button
        self.log_out_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Log out.png')
        log_out_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121', command=lambda: [Logic.delete_info_widgets(self), controller.show_frame('SignInPage')])
        log_out_button.place(x=32, y=1012)

        self.pt_image_1 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Giga Chad.png')
        pt_label_1 = tk.Label(self, bd=0, bg='#212121', image=self.pt_image_1)
        pt_label_1.place(x=222, y=589)

        self.pt_image_2 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\The Rock.png')
        pt_label_2 = tk.Label(self, bd=0, bg='#212121', image=self.pt_image_2)
        pt_label_2.place(x=476, y=589)

        self.course_image_1 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Course 1.png')
        course_label_1 = tk.Button(self, image=self.course_image_1, bd=0, bg='#212121', activebackground='#212121')
        course_label_1.place(x=688, y=265)

        self.course_image_2 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Course 2.png')
        course_label_2 = tk.Button(self, image=self.course_image_2, bd=0, bg='#212121', activebackground='#212121')
        course_label_2.place(x=688, y=355)

        self.course_image_3 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Course 3.png')
        course_label_3 = tk.Button(self, image=self.course_image_3, bd=0, bg='#212121', activebackground='#212121')
        course_label_3.place(x=688, y=445)

        self.course_image_4 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Course 4.png')
        course_label_4 = tk.Button(self, image=self.course_image_4, bd=0, bg='#212121', activebackground='#212121')
        course_label_4.place(x=688, y=535)

        self.food_image_1 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Food 1.png')
        food_label_1 = tk.Button(self, image=self.food_image_1, bd=0, bg='#212121', activebackground='#212121')
        food_label_1.place(x=688, y=822)

        self.food_image_2 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Food 2.png')
        food_label_2 = tk.Button(self, image=self.food_image_2, bd=0, bg='#212121', activebackground='#212121')
        food_label_2.place(x=1086, y=822)

        self.food_image_3 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Food 3.png')
        food_label_3 = tk.Button(self, image=self.food_image_3, bd=0, bg='#212121', activebackground='#212121')
        food_label_3.place(x=1478, y=822)

        # Calendar
        now = datetime.now()
        month = now.strftime("%B")
        year = now.strftime("%Y")

        time_now = tk.Label(self, text=f"{month} {year}", font=('iCiel Gotham Medium', 12), bg='#212121', fg="#E3E3E3")
        time_now.place(x=1525, y=292)

        cal = Calendar(self, font="Arial 14", selectmode="day", year=2023, month=4, day=1)
        cal.place(x=1390, y=330)

