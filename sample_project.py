import csv
import os

FILENAME = "students.csv"
FIELDS = ['ID', 'Name', 'Age', 'Department', 'Email']

# Initialize CSV file
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()  # Add header row

# Add a new student
def add_student():
    with open(FILENAME, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        dept = input("Enter Department: ")
        email = input("Enter Email: ")
        writer.writerow({'ID': id, 'Name': name, 'Age': age, 'Department': dept, 'Email': email})
    print("✅ Student added successfully!\n")

# Display all students
def display_students():
    if not os.path.exists(FILENAME):
        print("⚠️ No data found. Add students first.\n")
        return
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        print("\n--- Student Records ---")
        print(f"{'ID':<5} | {'Name':<15} | {'Age':<5} | {'Department':<12} | {'Email':<20}")
        print("-"*65)
        for row in reader:
            print(f"{row['ID']:<5} | {row['Name']:<15} | {row['Age']:<5} | {row['Department']:<12} | {row['Email']:<20}")
    print()

# Search student by ID
def search_student():
    id = input("Enter Student ID to search: ")
    found = False
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'] == id:
                print("\n✅ Student Found:")
                print(row)
                found = True
                break
    if not found:
        print("⚠️ No record found.\n")

# Update a student
def update_student():
    id = input("Enter Student ID to update: ")
    updated = False
    rows = []
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'] == id:
                row['Name'] = input(f"Enter new Name ({row['Name']}): ") or row['Name']
                row['Age'] = input(f"Enter new Age ({row['Age']}): ") or row['Age']
                row['Department'] = input(f"Enter new Department ({row['Department']}): ") or row['Department']
                row['Email'] = input(f"Enter new Email ({row['Email']}): ") or row['Email']
                updated = True
            rows.append(row)
    if updated:
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print("✅ Record updated successfully!\n")
    else:
        print("⚠️ No record found.\n")

# Delete a student
def delete_student():
    id = input("Enter Student ID to delete: ")
    deleted = False
    rows = []
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'] != id:
                rows.append(row)
            else:
                deleted = True
    if deleted:
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print("🗑️ Record deleted successfully!\n")
    else:
        print("⚠️ No record found.\n")

# Main menu
def main():
    initialize_file()
    while True:
        print("====== STUDENT DATABASE SYSTEM ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Have a Exciting Day")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
