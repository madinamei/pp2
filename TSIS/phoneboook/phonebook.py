import json
import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# ---------------- ADD CONTACT ----------------
def add_contact():
    name = input("Name: ")

    cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
    if cur.fetchone():
        print("Contact already exists!")
        return

    email = input("Email: ")
    birthday = input("Birthday: ")
    group = input("Group: ")

    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    g = cur.fetchone()

    if g:
        gid = g[0]
    else:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        gid = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES (%s,%s,%s,%s)
    """, (name, email, birthday, gid))

    conn.commit()
    print("Added")


# ---------------- CHANGE CONTACT ----------------
def change_contact():
    name = input("Name: ")

    cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
    row = cur.fetchone()

    if not row:
        print("Not found")
        return

    cid = row[0]

    email = input("New email: ")
    birthday = input("New birthday: ")
    group = input("New group: ")

    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    g = cur.fetchone()

    if g:
        gid = g[0]
    else:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        gid = cur.fetchone()[0]

    cur.execute("""
        UPDATE contacts
        SET email=%s, birthday=%s, group_id=%s
        WHERE id=%s
    """, (email, birthday, gid, cid))

    conn.commit()
    print("Updated")


# ---------------- SEARCH ----------------
def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    print(cur.fetchall())


# ---------------- PAGINATION ----------------
def pagination():
    limit = int(input("Limit: "))
    offset = 0

    while True:
        cur.execute("SELECT * FROM get_contacts(%s,%s)", (limit, offset))
        rows = cur.fetchall()

        for r in rows:
            print(r)

        cmd = input("next / prev / exit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break


# ---------------- EXPORT JSON ----------------
def export_json():
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
    """)

    data = []
    for r in cur.fetchall():
        data.append({
            "id": r[0],
            "name": r[1],
            "email": r[2],
            "birthday": str(r[3]),
            "group": r[4]
        })

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Export done")

def delete_contact():
    name = input("Enter contact name to delete: ")

    # проверяем существует ли контакт
    cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
    row = cur.fetchone()

    if not row:
        print("Contact not found")
        return

    confirm = input(f"Are you sure you want to delete {name}? (yes/no): ")

    if confirm != "yes":
        print("Cancelled")
        return

    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()

    print("Contact deleted")

# ---------------- IMPORT JSON ----------------
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (c["name"],))
        exists = cur.fetchone()

        if exists:
            action = input(f"{c['name']} exists (skip/overwrite): ")

            if action == "skip":
                continue

            cur.execute("""
                UPDATE contacts
                SET email=%s, birthday=%s
                WHERE name=%s
            """, (c["email"], c["birthday"], c["name"]))
        else:
            cur.execute("""
                INSERT INTO contacts(name,email,birthday)
                VALUES (%s,%s,%s)
            """, (c["name"], c["email"], c["birthday"]))

    conn.commit()
    print("Imported")


# ---------------- CSV IMPORT ----------------
def import_csv():
    file = input("CSV file: ")

    with open(file, newline='') as f:
        reader = csv.DictReader(f)

        for r in reader:
            # защита от пустых/битых строк
            if not r["name"] or r["name"] == "name":
                continue

            name = r["name"]
            email = r["email"]
            birthday = r["birthday"]
            group = r["group"]
            phone = r["phone"]
            ptype = r["type"]

            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            g = cur.fetchone()

            if g:
                gid = g[0]
            else:
                cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
                gid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts(name,email,birthday,group_id)
                VALUES (%s,%s,%s,%s)
                RETURNING id
            """, (name, email, birthday, gid))

            cid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id,phone,type)
                VALUES (%s,%s,%s)
            """, (cid, phone, ptype))

    conn.commit()
    print("CSV imported")


# ---------------- PROCEDURES ----------------
def move_group():
    name = input("Name: ")
    group = input("Group: ")
    cur.execute("CALL move_to_group(%s::varchar,%s::varchar)", (name, group))
    conn.commit()


def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type: mobile/work/home: ")
    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()


# ---------------- MENU ----------------
def menu():
    while True:
        print("""
1 Add contact
2 Change contact
3 Search
4 Pagination
5 Export JSON
6 Import JSON
7 CSV Import
8 Move group
9 Add phone
10 Delete contact
0 Exit
        """)

        c = input("Choose: ")

        if c == "1":
            add_contact()
        elif c == "2":
            change_contact()
        elif c == "3":
            search()
        elif c == "4":
            pagination()
        elif c == "5":
            export_json()
        elif c == "6":
            import_json()
        elif c == "7":
            import_csv()
        elif c == "8":
            move_group()
        elif c == "9":
            add_phone()
        elif c == "10":
            delete_contact()
        elif c == "0":
            break


menu()