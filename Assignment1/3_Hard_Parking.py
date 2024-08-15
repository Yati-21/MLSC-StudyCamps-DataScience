""" 
3. Implement a Parking Lot System
Requirements:
Implement classes for Vehicle, Car, Bike, ParkingSpot, ParkingLot.
Vehicle should be a base class with attributes like license_plate and vehicle_type.
Car and Bike should inherit from Vehicle.
ParkingSpot should have attributes like spot_id, is_available, and vehicle.

ParkingLot should manage multiple parking spots and provide methods to park and retrieve vehicles, 
and to get the status of the parking lot.

"""
class Vehicle:
    def __init__(self,license_plate, vehicle_type):
        self.license_plate =license_plate
        self.vehicle_type =vehicle_type

class Car(Vehicle):
    def __init__(self,license_plate):
        super().__init__(license_plate,"Car")

class Bike(Vehicle):
    def __init__(self,license_plate):
        super().__init__(license_plate, "Bike")

class ParkingSpot:
    def __init__(self,spot_id):
        self.spot_id =spot_id
        self.is_available=True
        self.vehicle= None

class ParkingLot:
    
    def __init__(self, num_spots):
        self.spots =[ ]
        for spot_id in range(1 , num_spots+1 ):
            self.spots.append(ParkingSpot( spot_id))

    def park_vehicle(self,vehicle):
        for spot in self.spots:
            
            if spot.is_available:
                spot.is_available =False
                spot.vehicle =vehicle
                return spot.spot_id
            
        return None

    def retrieve_vehicle(self,spot_id):
        for spot in self.spots:
            if spot.spot_id ==spot_id:
                
                spot.is_available = True
                vehicle=spot.vehicle
                spot.vehicle= None
                return vehicle
            
        return None

    def get_parking_status(self):
        status = []
        
        for spot in self.spots:
            status.append(f"Spot{spot.spot_id} : {'Available' if spot.is_available else 'Occupied'}")
        
        return "\n".join(status)

parking_lot = ParkingLot(num_spots=10)

car1 =Car("Aaa123")
car2 =Car("Bbb789")

bike1=Bike("Ccc456")

spot1 =parking_lot.park_vehicle(car1)
spot5 =parking_lot.park_vehicle(bike1)
spot3 =parking_lot.park_vehicle(car2)

print(parking_lot.get_parking_status())

retrieved_vehicle = parking_lot.retrieve_vehicle(spot5)
if retrieved_vehicle:
    print(f"vehicle at entered spot: {retrieved_vehicle.license_plate}")
else:
    print("empty spot")
