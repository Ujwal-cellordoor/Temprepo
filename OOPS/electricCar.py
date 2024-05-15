class ElectricCar:
    def __init__(self, brand, model, made_year, battary_capacity):
        self.brand = brand
        self.model = model
        self.made_year = made_year
        self.battary_capacity = battary_capacity
        # self.battary_level = 100
        self.motion = False
        self.on_track = True
        self.charging = False

    def start(self):
        if self.battary_capacity > 0:
            self.motion = True
            print("Vat Kat vat..... Car is started!")
        else:
            print("There is no charge left! Battery is empty!")

    def stop(self):
        if self.motion == True:
            self.motion = False
            print("The car is stopped")
        else:
            print("The car has zero velocity.")

    def show_battery_status(self):
        if self.charging == True:

            battary_level = self.total_charge
            print(f"Charge: {battary_level}%")
        else:
            print(f"{self.battary_capacity}%")

    def charge(self, hours):
        self.charging = True
        if self.battary_capacity < 100:
            add_charge = 20 * hours  # Assuming 20% charge per hour

            self.total_charge = add_charge + self.battary_capacity
            if self.total_charge > 100:
                print("100% !! Fully charged!")
            else:
                (f"The car battery after charge of {hours} is {self.total_charge}%")
        else:
            print("Cannot be charged beyond 100%.")

    def object_detection(self, object):
        self.on_track = False
        if self.motion == True and self.on_track == False:
            detected_object = f"{object } is ahead stop the car or use safety measures!!"
            print(detected_object)


car1_obj = ElectricCar("Tesla", "X3", 2020, 40)
car1_obj.start()
# car1_obj.object_detection("Tree")
# car1_obj.charge(1)
# car1_obj.show_battery_status()
# car1_obj.stop()
car1_obj.show_battery_status()
car1_obj.charge(6)
