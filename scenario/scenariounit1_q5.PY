class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Treatment Cost:", self.treatment_cost)
        print("Category:", self.category)
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_records(self):
        print("\n--- Patient Records ---")
        for patient in self.patients:
            patient.display()


# Creating Hospital object
hospital = Hospital()

# Adding patients
p1 = Patient(101, "Rahul", 5000, "General")
p2 = Patient(102, "Amit", 15000, "Special")
p3 = Patient(103, "Priya", 8000, "General")

hospital.add_patient(p1)
hospital.add_patient(p2)
hospital.add_patient(p3)

# Display all records
hospital.display_records()