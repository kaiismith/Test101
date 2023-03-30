import tkinter as tk
from tkinter import messagebox
import sqlite3
import ctypes
from FitnessProject.Control.logic import *
import pyglet
pyglet.font.add_file('GOTHAM-MEDIUM.OTF')


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self.geometry('1920x1080')
        self.state('zoomed')
        self.title("UwU Gymnastics")
        self.wm_attributes('-transparentcolor', 'grey')
        self.overrideredirect(False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInPage, SignUpPage, HealthInfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("SignInPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def move_app(self, e):
        self.geometry(f'+{e.x_root}+{e.y_root}')

    def on_entry_click(self, e, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, "end")
            entry.insert(0, '')
            entry.config(fg='#939597')

    def on_focusout(self, e, entry, default_text):
        if entry.get() == '':
            entry.insert(0, default_text)
            entry.config(fg='#939597')


class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame_photo = tk.PhotoImage(file='Login (Eye close).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)

        self.login_image = tk.PhotoImage(file='Login.png')
        login_button = tk.Button(self, image=self.login_image, borderwidth=0, bg='#141414', activebackground='#141414',
                                 command=lambda: sign_in())
        login_button.place(x=171, y=585)

        global username_entry
        username_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, username_entry, 'Username'))
        username_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, username_entry, 'Username'))
        username_entry.place(x=188, y=418)

        password_entry = tk.Entry(self, show="*", font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, password_entry, 'Password'))
        password_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, password_entry, 'Password'))
        password_entry.place(x=188, y=507)

        def sign_in():
            found = Logic.check_sign_in(username_entry.get(), password_entry.get())
            if found:
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            else:
                messagebox.showerror(title="Error", message="Invalid login.")

            found1 = Logic.check_health_info(username_entry.get())
            if not found1 and found:
                controller.show_frame('HealthInfoPage')

        def show_pw():
            hide_button = tk.Button(self, image=self.hide_image, command=hide_pw, activebackground='#141414', bd=0, bg='#141414')
            hide_button.place(x=498, y=517)
            password_entry.config(show='')

        def hide_pw():
            show_button = tk.Button(self, image=self.show_image, command=show_pw, activebackground='#141414', bd=0, bg='#141414')
            show_button.place(x=498, y=517)
            password_entry.config(show='*')

        self.show_image = tk.PhotoImage(file='Eye close.png')
        self.hide_image = tk.PhotoImage(file='Eye Open.png')

        show_button = tk.Button(self, image=self.show_image, command=show_pw, activebackground='#141414', bd=0, bg='#141414')
        show_button.place(x=498, y=517)

        self.sign_up_text = tk.PhotoImage(file='Sign up.png')
        sign_up_button = tk.Button(self, image=self.sign_up_text, border=0, bg='#141414', activebackground='#141414',
                                   command=lambda: controller.show_frame('SignUpPage'))
        sign_up_button.place(x=183, y=674)

        self.forgot_pw_text = tk.PhotoImage(file='Forgot password.png')
        forgot_pw_button = tk.Button(self, image=self.forgot_pw_text, border=0, bg='#141414', activebackground='#141414',
                                   command=lambda: messagebox.showinfo(title="???", message="Haiyahhh! Why you forget your password!"))
        forgot_pw_button.place(x=254, y=712)


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame_photo_2 = tk.PhotoImage(file='Sign up (Eye close).png')
        frame_label_2 = tk.Label(self, border=0, bg='grey', image=self.frame_photo_2)
        frame_label_2.place(x=0, y=0)
        frame_label_2.bind('<B1-Motion>', controller.move_app)

        username_entry_2 = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        username_entry_2.insert(0, 'Username')
        username_entry_2.bind('<FocusIn>', lambda event: controller.on_entry_click(event, username_entry_2, 'Username'))
        username_entry_2.bind('<FocusOut>', lambda event: controller.on_focusout(event, username_entry_2, 'Username'))
        username_entry_2.place(x=188, y=329)

        name_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        name_entry.insert(0, 'Your Full Name')
        name_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, name_entry, 'Your Full Name'))
        name_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, name_entry, 'Your Full Name'))
        name_entry.place(x=188, y=418)

        pw_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597', show='*')
        pw_entry.insert(0, 'Password')
        pw_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, pw_entry, 'Password'))
        pw_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, pw_entry, 'Password'))
        pw_entry.place(x=188, y=507)

        cpw_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597', show='*')
        cpw_entry.insert(0, 'Confirm Password')
        cpw_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, cpw_entry, 'Confirm Password'))
        cpw_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, cpw_entry, 'Confirm Password'))
        cpw_entry.place(x=188, y=596)


        self.sign_up_box = tk.PhotoImage(file='Login (1).png')
        sign_up_btn = tk.Button(self, image=self.sign_up_box, bd=0, bg='#141414', activebackground='#141414',
                             command=lambda: [Logic.check_signup(username_entry_2.get(), name_entry.get(), pw_entry.get(), cpw_entry.get()), controller.show_frame('SignInPage')])
        sign_up_btn.place(x=171, y=674)

        self.sign_in_text = tk.PhotoImage(file='Sign up (1).png')
        sign_in_button = tk.Button(self, image=self.sign_in_text, bd=0, bg='#141414', activebackground='#141414',
                             command=lambda: [controller.show_frame('SignInPage')])
        sign_in_button.place(x=183, y=763)


class HealthInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global username_entry

        self.frame_photo_3 = tk.PhotoImage(file='Information.png')
        frame_label_3 = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_3)
        frame_label_3.place(x=0, y=0)
        frame_label_3.bind('<B1-Motion>', controller.move_app)

        age_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=7, bg='#141414', bd=0, fg='#939597')
        age_entry.insert(0, 'Age')
        age_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, age_entry, 'Age'))
        age_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, age_entry, 'Age'))
        age_entry.place(x=188, y=367)

        gender_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=10, bg='#141414', bd=0, fg='#939597')
        gender_entry.insert(0, 'Gender')
        gender_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, gender_entry, 'Gender'))
        gender_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, gender_entry, 'Gender'))
        gender_entry.place(x=370, y=367)

        weight_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        weight_entry.insert(0, 'Weight')
        weight_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, weight_entry, 'Weight'))
        weight_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, weight_entry, 'Weight'))
        weight_entry.place(x=188, y=456)

        height_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        height_entry.insert(0, 'Height')
        height_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, height_entry, 'Height'))
        height_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, height_entry, 'Height'))
        height_entry.place(x=188, y=545)

        self.submit_box = tk.PhotoImage(file='Submit.png')
        submit_button = tk.Button(self, image=self.submit_box, bd=0, bg='#141414', activebackground='#141414',
                                  command=lambda: Logic.add_health_info(username_entry.get(), gender_entry.get(), age_entry.get(), height_entry.get(), weight_entry.get()))
        submit_button.place(x=171, y=623)


class HomePage:
    pass


class AbsPage:
    pass


class ChestPage:
    pass





class ChatPage:
    pass


class PersonalSettings:
    pass


class Exit:
    pass


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
