
class Car:
    # class variable | access directly -> print(Car.total_car)
    total_car = 0

    def __init__(self,brand,model):

        #basic public attributes
        # self.brand = brand
        # self.model = model

        #encapsulation of attributes : _ none public |  - protected can be accessed in sub_classes | -- private  CANNOT BE ACCESS OUTSIDE PARENT
        self._brand = brand
        self._model = model
        Car.total_car += 1


        #functionalities
    # def show_details(self):
    #     return f"{self.brand} {self.model}"
    #         # print(self.brand)
    #         # print(self.model)


    # getter method for encapsulation
    def get_brand_(self):
        return self._brand + "!"
    # polymorphism

    def get_fuel_type(self):
        return "Unknown"

#Inheritance
class ElectricCar(Car):
    def __init__(self,brand,model):
        # initializing parent class
        super().__init__(brand,model)
        self._battery_size = battery_size=0

    def set_battery_size(self,value):
        if value < 10: # validation
            raise ValueError (" battery size must > 10 ")
        self._battery_size = value

    # method overriding
    def get_details(self):
        return f"{self._brand} {self._model} {self._battery_size}"

    # Polymorphism
    def get_fuel_type(self):
        return "Electric Charged"

