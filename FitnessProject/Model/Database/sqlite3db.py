import sqlite3

#Create the database and connect to it 
connection = sqlite3.connect(r'E:\USTH\Personal Fitness\FitnessProject\Model\Database\Fitness.db')
cursor = connection.cursor() #cursor for database command

#Create a table for user info 
cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR, name CHAR, password CHAR)")

#User table data dump
cursor.execute("INSERT INTO user (username, name, password) VALUES ('tensingnightco', 'Ho Cong Thanh', '14o35XoWU')")
cursor.execute("INSERT INTO user (username, name, password) VALUES ('killerxkiller', 'Dinh Huy Thai Son', '8979wE7P2')")
cursor.execute("INSERT INTO user (username, name, password) VALUES ('spring317', 'Dao Xuan Quy', '7bM7R79Cp')")
cursor.execute("INSERT INTO user (username, name, password) VALUES ('fuyohaiyaaa', 'Phung Dam Quan', '64X5kIVoN')")
cursor.execute("INSERT INTO user (username, name, password) VALUES ('kiwiahihi', 'Nguyen Tran Duc Quy', 'p746BhrZ5')")

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

# Create a table for fitness_for_beginners
cursor.execute("DROP TABLE IF EXISTS fitness_for_beginners")
cursor.execute("CREATE TABLE IF NOT EXISTS fitness_for_beginners (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR)")
connection.commit()

# Create a table for pose_method_for_marathon
cursor.execute("DROP TABLE IF EXISTS pose_method_for_marathon")
cursor.execute("CREATE TABLE IF NOT EXISTS pose_method_for_marathon (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR)")
connection.commit()

# Create a table for strength_development_for_runners
cursor.execute("DROP TABLE IF EXISTS strength_development_for_runners")
cursor.execute("CREATE TABLE IF NOT EXISTS strength_development_for_runners (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR)")
connection.commit()

# Create a table for yoga_mobility_challenge
cursor.execute("DROP TABLE IF EXISTS yoga_mobility_challenge")
cursor.execute("CREATE TABLE IF NOT EXISTS yoga_mobility_challenge (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR)")
connection.commit()

#Total changes to the database and terminate connection
print(connection.total_changes)
connection.close()




    





