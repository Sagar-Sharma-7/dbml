import mysql.connector


host = 'localhost'
user = 'root' 
password = 'ait123'
database = 'dummy' 

def connect_db():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def add_user(connection):
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    
    try:
        # 1. Using 'with' for the cursor
        with connection.cursor() as cursor:
            cursor.execute(query, (name, email))
        
        # 2. Committing *after* the 'try' block is successful
        connection.commit()
        print("User added successfully!")

    # 3. Catching any database errors
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # 4. Rolling back the change if something went wrong
        connection.rollback()

def edit_user(connection):
    user_id = input("Enter user ID to edit: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    
    cursor = connection.cursor()
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    cursor.execute(query, (name, email, user_id))
    connection.commit()
    
    print(f"User with ID {user_id} updated successfully!")


def delete_user(connection):
    user_id = input("Enter user ID to delete: ")
    
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    
    print(f"User with ID {user_id} deleted successfully!")


def view_users(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    
    users = cursor.fetchall()
    print("Users in the database:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")


def main():
    connection = connect_db()
    if not connection:
        return

    while True:
        print("\n--- User Management ---")
        print("1. Add User")
        print("2. Edit User")
        print("3. Delete User")
        print("4. View Users")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_user(connection)
        elif choice == '2':
            edit_user(connection)
        elif choice == '3':
            delete_user(connection)
        elif choice == '4':
            view_users(connection)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")
    
    connection.close()

if __name__ == "__main__":
    main()