
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
    

