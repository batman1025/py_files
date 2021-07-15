class Train:

    company = "THE INDIAN RAILWAYS"

    def __init__(self, name, status, fare):
        self.name = name
        self.stats = status
        self.fare = fare

    def names(self):
        print(f"The {self.company} has been booked for {self.name}\n")
        
    def status(self):
        print(f"The status for {self.name} is {self.stats}\n")

    def fares(self):
        print(f"The fares for {self.name} is Rs.{self.fare}\n")
        
    def bookTickets(self):
        if self.stats>0:
            print(f"Yes booking availabe, and your seat number is : {self.stats} \n")
            self.stats = self.stats-1
            
        else:
            print("No Booking not available")
            
    def cancelTicket(self):
        print(f"Your ticket number {self.stats} has been cancelled\n")
        self.stats = self.stats+1
        print(f"Total available seats are {self.stats}")
        
    

a= Train("Express : 1025", 400, 120)

a.names()
a.status()
a.bookTickets()
a.fares()
a.status()
a.cancelTicket()
