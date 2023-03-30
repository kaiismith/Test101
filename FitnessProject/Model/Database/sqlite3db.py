import sqlite3

#Create the database and connect to it 
connection = sqlite3.connect('Fitness.db')
cursor = connection.cursor() #cursor for database command

#Create a table for user info 
cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR, name CHAR, password CHAR, phone_number CHAR)")

#User table data dump
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('tensingnightco', 'Ho Cong Thanh', '14o35XoWU','0123466456')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('killerxkiller', 'Dinh Huy Thai Son', '8979wE7P2', '035573565')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('spring317', 'Dao Xuan Quy', '7bM7R79Cp', '0123466244')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('fuyohaiyaaa', 'Phung Dam Quan', '64X5kIVoN', '035572435')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('kiwiahihi', 'Nguyen Tran Duc Quy', 'p746BhrZ5', '0123545533')")

connection.commit()

#Create a table for health info
cursor.execute("DROP TABLE IF EXISTS health")
cursor.execute("CREATE TABLE IF NOT EXISTS health (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR, gender CHAR, age INT, height FLOAT, weight FLOAT, bmi FLOAT, bmr FLOAT, bodyfat FLOAT, lbm FLOAT)")

#Health table data dump
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('tensingnightco', '1', 20, 164.5, 65.7, NULL, NULL, NULL, NULL)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('killerxkiller', '1', 25, 165.7, 63.7, NULL, NULL, NULL, NULL)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('spring317', '1', 18, 175.7, 73.4, NULL, NULL, NULL, NULL)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('fuyohaiyaaa', '1',  22, 155.6, 84.4, NULL, NULL, NULL, NULL)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('kiwiahihi', '1',  19, 168.5, 57.2, NULL, NULL, NULL, NULL)")

connection.commit()

#Create a table for exercise info
cursor.execute("DROP TABLE IF EXISTS exercise")
cursor.execute("CREATE TABLE IF NOT EXISTS exercise (id INTEGER PRIMARY KEY AUTOINCREMENT, exername CHAR, effectarea CHAR, difficulty CHAR, note CHARC)")


#User table data dump
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('push-ups', 'overall', 'easy', 'none')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('triceps dips', 'arm', 'easy', 'chair required')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('floor tricep dips', 'arm', 'medium', 'optional tool: mattress')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('squats', 'leg', 'easy', 'none')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('cat cow pose', 'shoulder & back', 'easy', 'none')")

connection.commit()

#Total changes to the database and terminate connection
print(connection.total_changes)
connection.close()




    





