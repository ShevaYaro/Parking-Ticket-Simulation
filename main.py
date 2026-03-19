from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def main():
    # Scenario 1: A Car Is Parked Legally
    print(" Scenario 1: Legally Parked Car ")
    car1 = ParkedCar("Nissan", "350Z", "Blue", "1919XM", 30)
    meter1 = ParkingMeter(50)
    officer1 = PoliceOfficer("Nazar", "320")

    ticket1 = officer1.inspect_car(car1, meter1)

    if ticket1 is not None:
        print(ticket1)
    else:
        print("No ticket was issued. The car is legally parked.\n")

    # Scenario 2: A Car Is Parked Illegally (under 1 hr)
    print(" Scenario 2: Illegally Parked Car Under 1 hr")
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")
    
    ticket2 = officer2.inspect_car(car2, meter2)
    
    if ticket2 is not None:
        print(ticket2)
    else:
        print("No ticket was issued. The car is legally parked.\n")

    # Scenario 3: A Car Is Parked Illegally (multiple houts)
    print(" Scenario 3: Illegally Parked Car Multiple hours")
    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")
    
    ticket3 = officer3.inspect_car(car3, meter3)
    
    if ticket3 is not None:
        print(ticket3)
    else:
        print("No ticket was issued. The car is legally parked.\n")
        
    print()


    #Scenario 4: Multiple Cars in a Parking Lot
    print(" Scenario 4: Multiple Cars in a Parking Lot ")
    officer_sarah = PoliceOfficer("Sarah Green", "9999")
    
    parking_lot = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),   # Legal
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),   # Overtime
        (ParkedCar("Subaru", "Outback", "Green", "RTY456", 45), ParkingMeter(60)),  # Legal
        (ParkedCar("Dodge", "Charger", "Yellow", "UIO789", 125), ParkingMeter(60)), # Overtime (just over 1 hr)
        (ParkedCar("Jeep", "Wrangler", "Orange", "PAS123", 240), ParkingMeter(60))  # Well over time (3 hrs)
    ]
    
    # Loop through each car-meter pair in our lot list
    for index, (car, meter) in enumerate(parking_lot, start=1):
        print(f"Inspecting Car {index} ({car.make} {car.model})...")
        ticket = officer_sarah.inspect_car(car, meter)
        
        if ticket is not None:
            print(ticket)
        else:
            print(f"No ticket issued for the {car.color} {car.make}.\n")

if __name__ == "__main__":
    main()

