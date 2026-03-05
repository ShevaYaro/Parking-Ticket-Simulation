import math

class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self.minutes_purchased = minutes_purchased

    def get_minutes_purchased(self):
        return self.minutes_purchased
    
    def set_minutes_purchased(self, minutes):
        if minutes > 0:
            self.minutes_purchased = minutes
        else: print("Error: Minutes purchased must be greated than 0.")

class ParkedCar:
    def __init__(self, make, model, color, licenseNumber, minutesParked = 60):
        #public atttributes
        self.make = make
        self.model = model
        self.color = color
        self.licenseNumber = licenseNumber
        
        #private attribute
        self.minutesParked = minutesParked

    def get_minutes_parked(self):
        return self.minutesParked
    
    def set_minutes_parked(self, minutes):
        if minutes > 0:
            self.minutes_purchased = minutes
        else: print("Error: Minutes parked must be greated than 0.")

    def __str__(self):
        return f"{self.color} {self.make} {self.model} License: {self.licenseNumber}"
    
class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
    
    def inspect_car(self, car, meter):
        minutes_parked = car.get_minutes_parked()
        minutes_purchased = meter.minutes_purchased()

        if (minutes_parked - minutes_purchased > 0):
            illegal_minutes = minutes_parked - minutes_purchased
            return ParkingTicket(car, self, illegal_minutes)
        else: return None

class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer = officer
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()
        
    def calculate_fine(self):
        hours_over = math.ceil(self.illegal_minutes / 60)
        
        fine = 25

        if (hours_over > 1):
            fine += (hours_over - 1) *10
        return fine
    def __str__(self):
        return (f"   PARKING TICKET   \n"
                f"Vehicle: {self.car.color} {self.car.make} {self.car.model} (License: {self.car.license_number})\n"
                f"Minutes Overtime: {self.illegal_minutes}\n"
                f"Fine Amount: ${self.fine}\n"
                f"Issued By: Officer {self.officer.name} (Badge: {self.officer.badge_number})\n")
