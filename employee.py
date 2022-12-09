"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, monthly_salary, hourly_salary, hours, commision_type, bonus, contract_count, commision_per_contract):
        ##Initiates the variables for Employee
        self.name = name
        self.salary_type = salary_type
        self.monthly_salary = monthly_salary
        self.hourly_salary = hourly_salary
        self.hours = hours
        self.commision_type = commision_type
        self.bonus = bonus
        self.contract_count = contract_count
        self.commision_per_contract = commision_per_contract

    #Calculates the pay
    def get_pay(self):
        #Calculate the pay based on assumption:
        #Employee can either be monthly or hourly, not both
        total = (self.hourly_salary*self.hours) + self.monthly_salary
        total = total + self.bonus + (self.contract_count*self.commision_per_contract)
        return total

    def __str__(self):
        #Returns the string
        print(f"{self.name} works on a {self.salary_type} of total {self.get_pay(self)}.")
        return self.name




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000, 0, 0, "no commisions", 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 0, 25, 100, "no commision", 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, 0, 0, "contract", 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 0, 25, 150, "contract", 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, 0, 0, "bonus", 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 0, 30, 120, "bonus", 600, 0, 0)
