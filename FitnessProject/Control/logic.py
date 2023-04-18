import sqlite3
import subprocess

from FitnessProject.Model.calculator import *
from tkinter import messagebox
import tkinter as tk

info_widgets = []


class Logic:
    def __init__(self, username_entry):
        self.username_entry = username_entry

    def check_sign_in(username, password):
        conn1 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor1 = conn1.cursor()
        cursor1.execute("SELECT username, password FROM user")
        results = cursor1.fetchall()
        for result in results:
            if username == result[0] and password == result[1]:
                return True
        return False

    def update_health_info(age, gender, weight, height):
        conn3 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT username, gender, age, height, weight FROM health")
        results = cursor3.fetchall()
        with open("temp.txt", 'r') as f:
            user_name = f.read()
        for result in results:
            if user_name == result[0]:

                query = "UPDATE health SET age = ?, gender = ?, weight = ?, height = ? WHERE username = ?"
                cursor3.execute(query, (age, gender, weight, height, user_name))
                conn3.commit()
                break

        conn3.close()
        Logic.calculate_stats(user_name)

    def check_admin(username, password):
        connect = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor = connect.cursor()
        cursor.execute("SELECT username, password FROM user")
        results = cursor.fetchall()
        for result in results:
            if username == "admin" and password == result[1]:
                return True
        return False

    def check_health_info(username):
        conn2 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT username FROM health")
        results = cursor2.fetchall()

        for result in results:
            if username == result[0]:
                return True
        return False

    def calculate_stats(user_name):
        conn3 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT username, gender, age, height, weight FROM health")
        results = cursor3.fetchall()
        calculator = Calculator()

        for result in results:
            if user_name == result[0]:
                query = "UPDATE health SET bmi = ?, bmr = ?, bodyfat = ?, lbm = ? WHERE username = ?"
                bmi = calculator.calculate_BMI(float(result[4]), float(result[3]))
                bmr = calculator.calculate_BMR(float(result[4]), float(result[2]), float(result[3]), float(result[1]))
                bodyfat = calculator.calculate_body_fat(float(result[2]), float(result[4]), float(result[3]),
                                                        float(result[1]))
                lbm = calculator.calculate_LBM(float(result[4]), float(result[3]), float(result[1]))
                cursor3.execute(query, (bmi, bmr, bodyfat, lbm, user_name))
                conn3.commit()
                break

        conn3.close()

    def check_signup(username, name, password, cf_password):
        conn2 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT username FROM user")
        results = cursor2.fetchall()

        found = False
        for result in results:
            if username == result[0]:

                found = True
                break
            else:
                found = False

        if len(password) < 6:
            messagebox.showerror(title="Error", message="Password must have at least 6 characters!")
        else:
            if password == cf_password:
                if not found:
                    cursor2.execute("INSERT INTO user (username, name, password) VALUES (?, ?, ?)",
                                    (username, name, password))
                    messagebox.showinfo("Success", "New account created successfully!")
                else:
                    messagebox.showerror(title="Error", message="Usename existed!")
            else:
                messagebox.showerror(title="Error", message="Password does not match!")

        conn2.commit()
        conn2.close()

    def add_health_info(username, gender, age, height, weight):
        conn3 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT username, age, height, weight FROM health")
        results = cursor3.fetchall()
        found = False
        for result in results:
            if username == result[0]:

                found = True
                break
            else:
                found = False

        if not found:
            query = "INSERT INTO health (username, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)"
            if gender == "1" or gender == "0":

                params = username, gender, age, height, weight

                # print(username)
                cursor3.execute(query, params)

                messagebox.showinfo("Success", "Submission successfully")
            else:
                messagebox.showerror(title="Error", message="Gender must be 1 for male and 0 for woman.")

        conn3.commit()
        Logic.calculate_stats(username)

        conn3.close()

    def delete_info_widgets(self):
        for widget in info_widgets:
            widget.destroy()

    # Display text on HomePage
    def display(posx, posy):
        conn4 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor4 = conn4.cursor()
        cursor4.execute("SELECT username, height, weight, bmi, bmr, bodyfat, lbm FROM health")
        results = cursor4.fetchall()
        with open("temp.txt", "r") as f:
            user_name = f.read()

        for result in results:
            if result[0] == user_name:
                height = str(result[1])
                weight = str(result[2])
                bmi = str(result[3])
                bmr = str(result[4])
                bodyfat = str(result[5])
                lbm = str(result[6])
                # return [height, weight, bmi, bmr, bodyfat, lbm]

        health_info = [height + "m", weight + "kg", bmi + "kg/m2", bmr, bodyfat + "%", lbm + "lbf"]
        idx = 0

        for y in posy:
            for x in posx:
                info = tk.Label(bd=0, highlightthickness=0, borderwidth=0, font=('iCiel Gotham Medium', 15),
                                text=health_info[idx], fg='#F5DF4D',
                                bg='#212121')
                info.place(x=x, y=y)
                info_widgets.append(info)
                idx += 1

    def open_db(self):
        db_browser_path = r'E:\SQLLite\DB Browser for SQLite.exe'
        db_file_path = r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db'

        subprocess.Popen([db_browser_path, db_file_path])

    def check_stats(self):
        with open(r"E:\USTH\Personal Fitness\FitnessProject\View\temp.txt", 'r') as f:
            username = f.read()

        if username == "admin":
            Logic.open_db(self)
        else:
            messagebox.showerror(title="Error", message="You're not admin!")

    def register(course_name):
        messagebox.showinfo(title="", message=f"You've have enrolled {course_name}!")

    def join_course(course_name):
        with open(r"E:\USTH\Personal Fitness\FitnessProject\View\temp.txt", 'r') as f:
            username = f.read()

        conn5 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor = conn5.cursor()
        cursor.execute("SELECT username FROM fitness_for_beginners")
        results = cursor.fetchall()

        found = False
        for result in results:
            if username == result[0]:

                found = True
                break
            else:
                found = False

        if not found:
            if course_name == "fitness_for_beginners":
                cursor.execute("INSERT INTO fitness_for_beginners (username) VALUES (?)", (username,))
                Logic.register(course_name)

        if course_name == "pose_method_for_marathon":
            messagebox.showinfo(title="", message="COMING SOON!")
        elif course_name == "strength_development_for_runners":
            messagebox.showinfo(title="", message="COMING SOON!")
        elif course_name == "yoga_mobility_challenge":
            messagebox.showinfo(title="", message="COMING SOON!")

        conn5.commit()
        conn5.close()

    def quit_program(frame):
        frame.quit()
