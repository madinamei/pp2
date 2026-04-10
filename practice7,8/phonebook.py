from connect import connect
import csv

# CREATE (добавление)
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# READ (просмотр)
def get_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# UPDATE
def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()

# DELETE
def delete_contact(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()

# CSV импорт
def import_csv(file):
    conn = connect()
    cur = conn.cursor()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()

# Меню
def menu():
    while True:
        print("\n1. Add contact")
        print("2. Show contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Import CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            get_contacts()

        elif choice == "3":
            name = input("Name: ")
            phone = input("New phone: ")
            update_contact(name, phone)

        elif choice == "4":
            name = input("Name: ")
            delete_contact(name)

        elif choice == "5":
            file = input("CSV file name: ")
            import_csv(file)

        elif choice == "0":
            break

menu()