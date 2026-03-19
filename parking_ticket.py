import math

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
                f"Vehicle: {self.car.color} {self.car.make} {self.car.model} (License: {self.car.licenseNumber})\n"
                f"Minutes Overtime: {self.illegal_minutes}\n"
                f"Fine Amount: ${self.fine}\n"
                f"Issued By: Officer {self.officer.name} (Badge: {self.officer.badge_number})\n")