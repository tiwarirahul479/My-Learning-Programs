# # class methods and attributes
# class Employee:
#     company = "TCS"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def change_company(cls):
#         print(f"Before===={cls.company}")
#         cls.company = "Infosys"
#         print(f"After===={cls.company}")

# e1 = Employee("Rahul", 28)
# e2 = Employee("Ramesh", 25)

# print(e1.__dict__)
# print(e1.company)
# e1.company = "Wipro"
# print(e2.__dict__)
# print(e2.company)

# print(Employee.company)
# Employee.company = "Wipro"
# print(Employee.company)
# print(e2.company)

# e1.change_company()
# print(e1.company)
# print(e1.__dict__)
# print(e2.company)
# print(Employee.company)



# # __name__ == "__main__"
# # here, __name__ is the variable which python is managing on its own. 
# # __name__ returns "__main__" when the code is executed directly
# # __name__ returns "file_name", when run the code by importing into some other file 
# # ex:-
# def add(a, b):
#     return a+b

# print(f"Running before __name__, value is: {__name__}")

# if __name__ == "__main__":
#     print(f"Direct Execution = {add(10, 20)}")

# # check it by importing "oops_concept" into other *.py file. The code inside __name__ isn't get executed



# # static methods
# class Bank:
#     bank_name = "SBI"
#     r_o_i = 12

#     @staticmethod
#     def compute_interest(p, t):
#         si = (p * t * Bank.r_o_i) / 100
#         print(si)

# Bank.compute_interest(1000, 10)
# b1 = Bank()
# b1.compute_interest(1200, 12)



