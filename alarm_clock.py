class Alarm_clock:
    def __init__(self):
        self.time = "1pm"
        self.alarm_on = True
        self.alarm_time = "2pm"


    def set_time(self):
        self.time = input("Enter current time: ")
        print("The current time is: ", self.time)

    def set_alarm_on_or_off(self):
        self.alarm_on = True

    def set_alarm_time(self):
        self.alarm_time = input("Enter alarm time: ")
        print("Alarm time is: ", self.alarm_time)