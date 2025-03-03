from Car import Car

Toyota = Car(4, "Toyota", 12, 10000)

print(Toyota.number_of_wheels)
print(Toyota.brand_name)
print(Toyota.mileage)
print(Toyota.price)
print(Toyota)

Lambo = Car(4, "Lambo", 10, 20000)

print(Toyota.compare(Lambo))