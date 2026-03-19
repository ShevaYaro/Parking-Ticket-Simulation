class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self.minutes_purchased = minutes_purchased

    def get_minutes_purchased(self):
        return self.minutes_purchased
    
    def set_minutes_purchased(self, minutes):
        if minutes > 0:
            self.minutes_purchased = minutes
        else: print("Error: Minutes purchased must be greated than 0.")




