# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:49:27 2026
Design a simple Hospital Management System with:

Person
 ├── Doctor
 └── Patient

Requirements:

Person should contain common information.
Doctor should have specialization.
Patient should have disease.
Doctor can diagnose a patient.
Use inheritance.
Use polymorphism.
Use encapsulation.
@author: Admin
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. ENCAPSULATION & INHERITANCE (Base Class)
# ==========================================
class Person(ABC):
    """
    Abstract base class representing a generic Person.
    Demonstrates Encapsulation by keeping attributes private/protected 
    and providing getter/setter methods.
    """
    def __init__(self, name: str, age: int, gender: str):
        # Encapsulated (private) attributes
        self.__name = name
        self.__age = age
        self.__gender = gender

    # Getters and Setters for Encapsulation
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive.")

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str):
        self.__gender = gender

    @abstractmethod
    def display_details(self):
        """Abstract method to support polymorphism."""
        pass


# ==========================================
# 2. INHERITANCE (Doctor class)
# ==========================================
class Doctor(Person):
    """
    Doctor class inherits from Person and adds specialization.
    """
    def __init__(self, name: str, age: int, gender: str, specialization: str):
        super().__init__(name, age, gender)
        self.__specialization = specialization
        self.__assigned_patients = []  # List to keep track of diagnosed patients

    def get_specialization(self) -> str:
        return self.__specialization

    def set_specialization(self, specialization: str):
        self.__specialization = specialization

    # Polymorphism: Overriding display_details method
    def display_details(self):
        print(f"[Doctor] Dr. {self.get_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}, Specialization: {self.__specialization}")

    # Doctor functionality: Diagnosing a patient
    def diagnose_patient(self, patient, disease: str):
        print(f"-> Dr. {self.get_name()} ({self.__specialization}) is examining patient {patient.get_name()}...")
        patient.set_disease(disease)
        self.__assigned_patients.append(patient)
        print(f"-> Diagnosis complete! {patient.get_name()} has been diagnosed with: {disease}\n")


# ==========================================
# 3. INHERITANCE (Patient Class)
# ==========================================
class Patient(Person):
    """
    Patient class inherits from Person and adds disease.
    """
    def __init__(self, name: str, age: int, gender: str, disease: str = "Undiagnosed"):
        super().__init__(name, age, gender)
        self.__disease = disease

    def get_disease(self) -> str:
        return self.__disease

    def set_disease(self, disease: str):
        self.__disease = disease

    # Polymorphism: Overriding display_details method
    def display_details(self):
        print(f"[Patient] {self.get_name()}, Age: {self.get_age()}, Gender: {self.get_gender()}, Current Disease/Condition: {self.__disease}")


# ==========================================
# 4. DEMONSTRATION OF THE SYSTEM 
# ==========================================
if __name__ == "__main__":
    print("--- HOSPITAL MANAGEMENT SYSTEM DEMO ---\n")

    # Creating Doctor and Patient instances
    doc1 = Doctor(name="Alice Smith", age=45, gender="Female", specialization="Cardiologist")
    doc2 = Doctor(name="Bob Jones", age=50, gender="Male", specialization="Neurologist")

    patient1 = Patient(name="John Doe", age=30, gender="Male")
    patient2 = Patient(name="Emma Watson", age=25, gender="Female")

    # Polymorphism in action: Treating a list of diverse 'Person' objects the same way
    print("--- Displaying Initial Details (Polymorphism) ---")
    people = [doc1, doc2, patient1, patient2]
    for person in people:
        person.display_details()
    print("-" * 50 + "\n")

    # Doctor diagnoses a patient
    print("--- Doctor Diagnosis Workflow ---")
    doc1.diagnose_patient(patient1, "Hypertension")
    doc2.diagnose_patient(patient2, "Migraine")

    # Displaying updated details
    print("--- Displaying Updated Details ---")
    patient1.display_details()
    patient2.display_details()
    print("-" * 50)
