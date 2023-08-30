class Vehicle:
    def __init__(self, company, model, year, color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color


class Car(Vehicle):
  def __init__(self, company, model, year, color, car_type):
    # Using super to access __init__ method of Parent Class
    super().__init__(company, model, year, color)
    self.car_type = car_type


my_car = Car("Tesla", "S", 2021, "Silver", "Sedan")
print(f"I have a {my_car.company} model {my_car.model}.")