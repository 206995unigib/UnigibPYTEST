from abc import ABC, abstractmethod

# Define an Abstract Base Class for a generic Vehicle
class Vehicle(ABC):
    
    __engine_rpm=0
    engine_wear=0
    @abstractmethod
    def start_engine(self):
        """Abstract method to start the vehicle's engine."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method to stop the vehicle's engine."""
        pass

    def refuel(self, amount):
        """Concrete method to refuel the vehicle."""
        print(f"Refueling with {amount} liters of fuel.")

# Concrete subclass: Car
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")

    def stop_engine(self):
        print("Car engine stopped.")

    def check_speed(self):
        self.__engine_rpm=1000
        return self.__engine_rpm

# Concrete subclass: ElectricCar
class ElectricCar(Vehicle):
    def start_engine(self):
        print("Electric car motor activated silently.")

    def stop_engine(self):
        print("Electric car motor deactivated.")

    # Override refuel for electric cars
    def refuel(self, amount):
        print(f"Charging with {amount} kWh of electricity.")

# Demonstrate usage
if __name__ == "__main__":
    my_car = Car()
    
    print(my_car.check_speed())
    print(my_car.engine_wear)

    my_car.start_engine()
    my_car.refuel(50)
    my_car.stop_engine()

    print("-" * 20)

    my_electric_car = ElectricCar()
    my_electric_car.start_engine()
    my_electric_car.refuel(20) # This will call the overridden method
    my_electric_car.stop_engine()

    # Attempting to instantiate the abstract class will raise an error
    try:
        generic_vehicle = Vehicle()
    except TypeError as e:
        print(f"\nError: {e}")