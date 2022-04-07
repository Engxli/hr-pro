from pickletools import int4
from datetime import date


class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return  date.today().year - int(self.employment_year)

    def __str__(self):
        # Name: sammy, Age: 52, Salary: 4600, Working Years: 119, Bonus: 1380.000000
        wy = str(self.get_working_years())
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {wy}'


class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return float(self.bonus_percentage)*int(self.salary)

    def __str__(self):
        # Name: sammy, Age: 52, Salary: 4600, Working Years: 119, Bonus: 1380.000000
        wy = str(self.get_working_years())
        bouns = str(self.get_bonus())
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {wy}, Bonus: {bouns}'

def main():
	# main code here
    employees = []
    managers = []
    def printOtions():
        print("Options: ")
        print("\t1. Show Employees: ")
        print("\t2. Show Managers: ")
        print("\t3. Add An Employee: ")
        print("\t4. Add A Manager: ")
        print("\t5. Exit: \n")

    def show_employees():
        print("-----------------")
        print("Employees")
        for employee in employees:
            print(employee)
        print("-----------------")

    def show_managers():
        print("-----------------")
        print("Managers")
        for manager in managers:
            print(manager)
        print("-----------------")

    def add_to_list(type):
        print("-----------------")
        name = input("Name: ")
        age = input("Age: ")
        salary = input("Salary: ")
        working_years = input("Working Years: ")
        if(type=="employee"):
            employees.append(Employee(name, age, salary, working_years))
            print("Employee added succesfully!\n")
            return 
        bonus = input("Bonus Percentage: ")
        managers.append(Manager(name, age, salary, working_years, bonus))
        print("Manager added succesfully!\n")


    print("Welcome to HR Pro 2019")
    while True:
        printOtions()
        user_selection = (input("What would you like to do? "))

        match str(user_selection):
            case "5":
                break
            case "1":
                show_employees()
            case "2":
                show_managers()
            case "3":
                add_to_list("employee")
            case "4":
                add_to_list("manager")
            case _:
                print("\n------------------")
                print("There is no such option!")
                print("------------------\n")


        if(user_selection == 5):
            break







    
if __name__ == '__main__':
	main()
