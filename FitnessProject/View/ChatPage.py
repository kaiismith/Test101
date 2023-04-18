import re
import tkinter as tk
from tkinter import scrolledtext
from FitnessProject.Control.logic import *
import openai

openai.api_key = "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"


class ChatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame_photo_5 = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Chat page (noti off - bot on).png')
        frame_label_5 = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_5)
        frame_label_5.place(x=0, y=0)
        frame_label_5.bind('<B1-Motion>', controller.move_app)

        self.home_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Home page.png')
        home_button = tk.Button(self, image=self.home_image, bd=0, bg='#212121', activebackground='#212121', command=lambda: [Logic.display(posx=[267, 485], posy=[304, 372, 440]), controller.show_frame('HomePage')])
        home_button.place(x=30, y=245)

        self.stats_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Statistics.png')
        stats_button = tk.Button(self, image=self.stats_image, border=0, bg='#212121', activebackground='#212121', command=lambda: Logic.check_stats(self))
        stats_button.place(x=29, y=435.1)

        self.user_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\User.png')
        user_button = tk.Button(self, image=self.user_image, border=0, bg='#212121', activebackground='#212121', command=lambda: controller.show_frame('UpdateHealthInfoPage'))
        user_button.place(x=29, y=530.1)

        self.noti_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Notification (off).png')
        noti_button = tk.Button(self, image=self.noti_image, border=0, bg='#212121', activebackground='#212121')
        noti_button.place(x=29, y=625)

        """self.censor = tk.Label(self, bd=0, bg="#141414", width=10, height=50)
        self.censor.place(x=1710, y=240)"""

        # When hit log out, the text should be destroyed
        self.log_out_image = tk.PhotoImage(file=r'E:\USTH\Personal Fitness\FitnessProject\View\Image\Log out.png')
        log_out_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121',
                                   command=lambda: [controller.show_frame('SignInPage'), ChatPage.clear_screen(self)])
        log_out_button.place(x=32, y=1012)

        self.chat_log = scrolledtext.ScrolledText(self, state='disabled', width=103, height=25, bg="#141414", fg="#939597", font=('iCiel Gotham Medium', 18),
                                                  borderwidth=0, highlightthickness=0)
        self.chat_log.place(x=170, y=233)

        self.user_input = tk.Entry(self, width=55, bd=0, font=('iCiel Gotham Medium', 18), bg="#141414", fg='#939597')
        self.user_input.place(x=508, y=1007)
        self.user_input.bind("<Return>", self.handle_user_input)

    def handle_user_input(self, event):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.update_chat_log("You: " + user_input)

        # Preprocessing the user input
        user_input = re.sub('[^a-zA-Z0-9 \n\.]', '', user_input).strip()

        # Generating a response from OpenAI GPT-3
        prompt = f'Q: {user_input}\nA:'
        response = openai.Completion.create(
            # gpt-3.5-turbo
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=10
        )

        # Extracting the response from OpenAI GPT-3
        bot_response = response.choices[0].text.strip()

        self.update_chat_log("ChatSonTG: " + bot_response)

    def update_chat_log(self, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.configure(state='disabled')
        self.chat_log.yview(tk.END)

    def clear_screen(self):
        self.chat_log.configure(state='normal')
        self.chat_log.delete('1.0', tk.END)
        self.chat_log.configure(state='disabled')
        self.chat_log.insert(tk.END, '')

