import sqlite3
from FitnessProject.Model.calculator import *
from tkinter import messagebox
import tkinter as tk


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

        if password == cf_password:
            if not found:
                cursor2.execute("INSERT INTO user (username, name, password) VALUES (?, ?, ?)",
                                (username, name, password))
                messagebox.showinfo("Success", "New account created successfully")
            else:
                messagebox.showerror(title="Error", message="Invalid sign-up.")
        else:
            messagebox.showerror(title="Error", message="Invalid sign-up.")

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

    # Display text on HomePage
    def display(user_name, posx, posy):
        conn4 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor4 = conn4.cursor()
        cursor4.execute("SELECT username, height, weight, bmi, bmr, bodyfat, lbm FROM health")
        results = cursor4.fetchall()
        for result in results:
            if result[0] == user_name:
                height = str(result[1])
                weight = str(result[2])
                bmi = str(result[3])
                bmr = str(result[4])
                bodyfat = str(result[5])
                lbm = str(result[6])
                # return [height, weight, bmi, bmr, bodyfat, lbm]

        health_info = [height + "cm", weight + "kg", bmi + "kg/m2", bmr, bodyfat + "%", lbm + "lbf"]
        idx = 0

        for y in posy:
            for x in posx:
                info = tk.Label(bd=0, highlightthickness=0, borderwidth=0, font=('iCiel Gotham Medium', 15), text=health_info[idx], fg='#F5DF4D',
                                bg='#212121')
                info.place(x=x, y=y)
                idx += 1


        idx = 0







