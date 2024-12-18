#class, object, inheritance,abs,pol,enc

# class Demo:
#     x=5
#     y=10
#     z=15

#     def __init__(self, a, b, c):
#         self.x = a
#         self.y = b
#         self.z = c

# # methods = functions that are written in a class
#     def add(self):
#         return self.x + self.y + self.z 
    


# d=Demo(10,20,30) # parametrized constructor
# print(d.add())

# constructor  -> default constructor,parametrized constructor


# inheritance -> single level ,multi-level,multiple, hybrid
# class Parent:
#     #constructor ->
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     #method to print
#     def print_parent(self):
#         print("parent:", self.a, self.b)


# class Child(Parent):
#     #constructor 
#     def __init__(self,a,b, c):
#         super().__init__(a,b) # calling constructor of parent class
#         self.c = c

# # how i can call method of parent class with the child class object

# #object

# obj=Child(10,5,20)
# obj.print_parent()


#accesss modifier 
#private ,protected ,public

# _sample --> protected
#__sample --> private
#sample --> public

#abstraction 
# class Student():

#     #private 
#     __name="Disha"
#     __roll=23
#     __maths=None
#     __science=None
#     __english=None

#     #private member function
#     def __display_all_details(this):
#         print("Name:", this.__name)
#         print("Roll:", this.__roll)
#         print("Maths:", this.__maths)
#         print("Science:", this.__science)
#         print("English:", this.__english)

#     #public member function
#     def display_details(this): #getter
#         this.__display_all_details()

#     def set_marks(self,m,s,e):  #setter
#         self.__maths=m
#         self.__science=s
#         self.__english=e

# #getter -> a method that we use to get the value 
# #setter -> a method that we use to set the value

# #object
# obj=Student()
# obj.set_marks(90,80,95)
# obj.display_details()

#poly -> a method that we we can use for multiple purpose
# compile time , runtime 

# def add(a,b,c=0):
#     return a+b+c

# print(add(3,6,7))
# print(add(3,5))