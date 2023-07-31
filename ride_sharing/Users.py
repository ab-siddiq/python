# abc stands for abstract base class
# ggg
from abc import ABC,abstractmethod
from datetime import datetime
class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.nId=nid
        self.wallet = 0
        # TODO: id will be set dynamically
        self.__id=0
    @abstractmethod
    def display_profile(self):
        # if someone call this method it will trough error that need to implement
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid) -> None:
        self.current_ride = None
        self.wallet=0
        super().__init__(name, email, nid)
    def display_profile(self):
        print(f'Rider: name: {self.name} email: {self.email}')
    
    def request_ride(self,location,destination):
        if not self.current_ride:
            # TODO: set ride properly
            ride_request=None
            self.current_ride = None

    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount


class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet=0

    def display_profile(self):
        print(f'Driver with name: {self.name} email: {self.email}')
    
    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None

    def set_driver(self,drive):
        self.driver=Driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self,rider,amount):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare