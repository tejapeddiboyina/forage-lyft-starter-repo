from abc import ABC
from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.last_service_date.year + 2 < self.current_date
