from database import create_table, add_patient

create_table()

while True:
    print("1. Register new patient")
    # print("2. View all patients")
    # print("3. Search for a patient")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        add_patient(name, age)
        print("Patient registered.")
    elif choice == "4":
        print("Goodbye!")
        break