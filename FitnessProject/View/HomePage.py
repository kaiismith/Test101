import tkinter as tk
from FitnessProject.Control.logic import *
from FitnessProject.View.SignInPage import SignInPage


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        posx = [267, 455]
        posy = [294, 362, 430]
        idx = 0

        self.frame_photo_4 = tk.PhotoImage(file='Home page (noti off).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_4)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)


        username_entry = SignInPage.get_username_entry
        # print(username_entry)

        """username_entry = SignInPage.get_username_entry(self)
        health_info = Logic.display(username_entry.get())

        for y in posy:
            for x in posx:
                info = tk.Label(self, bd=0, font=('iCiel Gotham Medium', 15), text=health_info[idx], fg='#F5DF4D', bg='#212121')
                info.place(x=x, y=y)
                idx += 1

        idx = 0"""


        self.message_image = tk.PhotoImage(file='Message (off).png')
        message_button = tk.Button(self, image=self.message_image, bd=0, bg='#212121', activebackground='#212121')
        message_button.place(x=29, y=339)

        self.stats_image = tk.PhotoImage(file='Statistics.png')
        stats_button = tk.Button(self, image=self.stats_image, border=0, bg='#212121', activebackground='#212121')
        stats_button.place(x=29, y=435.1)

        self.user_image = tk.PhotoImage(file='User.png')
        user_button = tk.Button(self, image=self.user_image, border=0, bg='#212121', activebackground='#212121')
        user_button.place(x=29, y=530.1)

        self.noti_image = tk.PhotoImage(file='Notification (off).png')
        noti_button = tk.Button(self, image=self.noti_image, border=0, bg='#212121', activebackground='#212121')
        noti_button.place(x=29, y=625)

        # When hit log out, the text should be destroyed
        self.log_out_image = tk.PhotoImage(file='Log out.png')
        log_out_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121', command=lambda: controller.show_frame('SignInPage'))
        log_out_button.place(x=32, y=1012)
