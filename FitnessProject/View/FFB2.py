import tkinter as tk
from FitnessProject.Control.logic import *


class FFB2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create background for Home Page
        self.frame_photo_4 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Home page (noti off) (6).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_4)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)

        # Message Button
        self.message_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Message (off).png')
        message_button = tk.Button(self, image=self.message_image, bd=0, bg='#212121', activebackground='#212121',
                                   command=lambda: [Logic.delete_info_widgets(self), controller.show_frame('ChatPage')])
        message_button.place(x=29, y=339)

        # Stats Button
        self.stats_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Statistics.png')
        stats_button = tk.Button(self, image=self.stats_image, border=0, bg='#212121', activebackground='#212121',
                                 command=lambda: Logic.check_stats(self))
        stats_button.place(x=29, y=435.1)

        # Personal Settings Button
        self.user_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\User.png')
        user_button = tk.Button(self, image=self.user_image, border=0, bg='#212121', activebackground='#212121',
                                command=lambda: [Logic.delete_info_widgets(self),
                                                 controller.show_frame('UpdateHealthInfoPage')])
        user_button.place(x=29, y=530.1)

        # Notification Button
        self.noti_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Notification (off).png')
        noti_button = tk.Button(self, image=self.noti_image, border=0, bg='#212121', activebackground='#212121')
        noti_button.place(x=29, y=625)

        # Log Out Button
        self.log_out_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Log out.png')
        log_out_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121',
                                   command=lambda: [Logic.delete_info_widgets(self),
                                                    controller.show_frame('SignInPage')])
        log_out_button.place(x=32, y=1012)

        self.back_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\arrow left.png')
        back_button = tk.Button(self, image=self.back_image, border=0, bg='#141414', activebackground='#141414',
                                command=lambda: [controller.show_frame('FFB1')])
        back_button.place(x=145, y=1000)

        self.next_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\arrow right.png')
        next_button = tk.Button(self, image=self.next_image, border=0, bg='#141414', activebackground='#141414',
                                command=lambda: [controller.show_frame('FFB3')])
        next_button.place(x=1800, y=1000)




