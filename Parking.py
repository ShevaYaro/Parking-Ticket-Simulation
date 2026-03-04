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
            illigal_minutes = minutes_parked - minutes_purchased
            return ParkingTicket(car, self, illigal_minutes)
        else: return None