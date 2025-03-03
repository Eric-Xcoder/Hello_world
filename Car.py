class Car:
    number_of_wheels = None
    brand_name       = None
    mileage          = None
    price            = None

    def __init__(self, number_of_wheels, brand_name, mileage, price):
        self.number_of_wheels = number_of_wheels
        self.brand_name = brand_name
        self.mileage = mileage
        self.price = price 
    
    def __str__(self):
        return "Car: " + self.brand_name + " has " + str(self.number_of_wheels) + " wheels, mileage is " + str(self.mileage) + " and price is " + str(self.price)

    # TODO: Take in another car, compare the cars price, and return the car with the higher price
    
