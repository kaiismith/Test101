import tkinter as tk
from FitnessProject.Control.logic import *


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create background for SignUpPage
        self.frame_photo_2 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Sign up (Eye close).png')
        frame_label_2 = tk.Label(self, border=0, bg='grey', image=self.frame_photo_2)
        frame_label_2.place(x=0, y=0)
        frame_label_2.bind('<B1-Motion>', controller.move_app)

        # Username Entry for username's input
        username_entry_2 = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        username_entry_2.insert(0, 'Username')
        username_entry_2.bind('<FocusIn>', lambda event: controller.on_entry_click(event, username_entry_2, 'Username'))
        username_entry_2.bind('<FocusOut>', lambda event: controller.on_focusout(event, username_entry_2, 'Username'))
        username_entry_2.place(x=188, y=329)

        # Name Entry for name's input
        name_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        name_entry.insert(0, 'Your Full Name')
        name_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, name_entry, 'Your Full Name'))
        name_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, name_entry, 'Your Full Name'))
        name_entry.place(x=188, y=418)

        # Password Entry for password's input
        pw_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597', show='*')
        pw_entry.insert(0, 'Password')
        pw_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, pw_entry, 'Password'))
        pw_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, pw_entry, 'Password'))
        pw_entry.place(x=188, y=507)

        # Confirm Password Entry for confirm password's input
        cpw_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597', show='*')
        cpw_entry.insert(0, 'Confirm Password')
        cpw_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, cpw_entry, 'Confirm Password'))
        cpw_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, cpw_entry, 'Confirm Password'))
        cpw_entry.place(x=188, y=596)

        # Sign Up Button
        self.sign_up_box = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Login (1).png')
        sign_up_btn = tk.Button(self, image=self.sign_up_box, bd=0, bg='#141414', activebackground='#141414',
                             command=lambda: [Logic.check_signup(username_entry_2.get(), name_entry.get(), pw_entry.get(), cpw_entry.get()), controller.show_frame('SignInPage')])
        sign_up_btn.place(x=171, y=674)

        # "Already have an account? Sign in" Button
        self.sign_in_text = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Sign up (1).png')
        sign_in_button = tk.Button(self, image=self.sign_in_text, bd=0, bg='#141414', activebackground='#141414',
                             command=lambda: [controller.show_frame('SignInPage')])
        sign_in_button.place(x=183, y=763)
