class Train:
    def __init__(self, name, fare, seat):
        self.name = name
        self.fare = fare
        self.seat = seat
    def getStatus(self):
        print("********")
        
        print(f"The name of the Train is{self.name}")
        print(f"The seat available in the train is {self.seat}")
        print("********")
    def getFareInfo(self):
        print(f"The Fare of the Train is Rs: {self.fare}" )   
    def bookTickets(self):
             if(self.seat>0):
                print(f"Your Ticket has been booked! Your seat number is {self.seat}")
                self.seat = self.seat - 1
             else:
                 print("Sorry this Train is full! Please try in tatkal")
                   
intercity = Train("Intercity Express: 14013", 90, 2)
intercity.getStatus()
intercity.getFareInfo()
intercity.bookTickets()        
intercity.bookTickets()        
intercity.bookTickets()        
intercity.getStatus()