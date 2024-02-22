import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='aren',
    password='aren',
    database='pySQL'
)
mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE pySQL")   

mycursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))''')
db.commit()

def create_user(name, email):
    mycursor.execute('''SELECT id FROM users WHERE name = %s''', (name,))
    existing_user = mycursor.fetchone()
    if existing_user:
        print(f"\nUser with name '{name}' already exists.")
        return
    mycursor.execute('''INSERT INTO users (name, email) VALUES (%s, %s)''', (name, email))
    db.commit()

def read_users():
    mycursor.execute('''SELECT * FROM users''')
    return mycursor.fetchall()

def update_user_email(name, new_email):
    mycursor.execute('''UPDATE users SET email = %s WHERE name = %s''', (new_email, name))
    db.commit()

def delete_user(name):
    mycursor.execute('''DELETE FROM users WHERE name = %s''', (name,))
    db.commit()

def delete_all_user():
    mycursor.execute('''DELETE FROM users''')
    db.commit()

# Create Users
create_user('Aren Ramirez', 'arenRamirez@example.com')
create_user('Ann Ngy', 'AnnNgy@example.com')
print("Initial users:")
print(read_users())

# Attempt to create a user with the same name again
create_user('Aren Ramirez', 'newemail@example.com')

# Update user email
update_user_email('Aren Ramirez', 'aRamirez@example.com')
print("\nUsers after updating email for user with name Aren Ramirez:")
print(read_users())

# Delete a user
delete_user('Aren Ramirez')
print("\nUsers after deleting user with name Aren Ramirez:")
print(read_users())

# Delete all users
print("\nDeleting all users!!")
delete_all_user()
print(read_users())

# Close the connection
db.close()
