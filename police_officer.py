from parking_ticket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
    
    def inspect_car(self, car, meter):
        minutes_parked = car.get_minutes_parked()
        minutes_purchased = meter.get_minutes_purchased()

        if (minutes_parked - minutes_purchased > 0):
            illegal_minutes = minutes_parked - minutes_purchased
            return ParkingTicket(car, self, illegal_minutes)
        else: return None