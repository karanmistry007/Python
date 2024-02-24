from datetime import datetime


# PYTHON OOPS USING CLASS AND CONSTRUCTOR METHODS
class Vehicle:

    # INIT CONSTRUCTOR OF CLASS
    def __init__(self, id, name, owner, type, make, rc_no, year=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.type = type
        self.make = make
        self.rc_no = rc_no
        self.year = year

    # PRINT KEY VALUES OF THE CLASS
    def print_values(self):
        print("Key Value Pair :")
        for key, value in self.__dict__.items():
            print(f"{key} : {value}")

    # CUSTOM CLASS METHOD GET YEAR DIFFERENCE
    @classmethod
    def get_year_diff(cls, year):
        current_year = datetime.now().year
        year_diff = current_year - year
        return f"Vehicle Year : {year}\nCurrent Year : {current_year}\nYear Differance : {year_diff}"


# THIS WILL EXECUTE ONLY IF THE FILE IS MAIN
if __name__ == "__main__":
    # VEHICLE ONE WITH VEHICLE CLASS
    vehicle_one = Vehicle(1, "Audi RS 7", "Karan", "Sedan", "Audi", 3350, 2020)
    print(f"Vehicle One Class : {vehicle_one}")

    # VEHICLE TWO WITH CUSTOM METHOD GET YEAR DIFFERENCE
    vehicle_two = Vehicle.get_year_diff(2020)
    print(f"Get Year Difference : \n{vehicle_two}")

    # PRINT ALL THE KEY VALUES OF THE CLASS VEHICLE
    vehicle_one.print_values()
