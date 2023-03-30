import sqlite3
from FitnessProject.Model.calculator import *
from tkinter import messagebox

class Logic:
    def check_sign_in(username, password):
        conn1 = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
        cursor1 = conn1.cursor()
        cursor1.execute("SELECT username, password FROM user")
        results = cursor1.fetchall()
        for result in results:
            if username == result[0] and password == result[1]:
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

    def check_signup(username,name, password, cf_password):
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