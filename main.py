import json

def register_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    patient = {"name": name, "age": age}
    return patient

try:
    with open("patients.json", "r") as file:
        patients = json.load(file)
except FileNotFoundError:
    patients = []

def save_patients():
    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)
        
while True:
    print("1. Register new patient")
    print("2. View all patients")
    print("3. Search for a patient")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_patient = register_patient()
        patients.append(new_patient)
        save_patients()
    elif choice == "2":
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}")
    elif choice == "3":
    
        search_name = input("Enter name to search: ")
        for patient in patients:
            if patient["name"].lower() == search_name.lower():
                print(f"Found: {patient['name']}, Age: {patient['age']}") 
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4")
        
