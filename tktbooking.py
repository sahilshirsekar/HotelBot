class Train :
    def __init__(self,name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*********************************")
        print(f"The name of the train is {self.name}")
        print(f"The number of seats of the train are {self.seats}")
        print('*********************************')

    def fareInfo(self):
        print(f"The price of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, seats are full! ")
rajdhani = Train("Rajdhani Express: 904545",150,2)
rajdhani.getStatus()
rajdhani.fareInfo()
rajdhani.bookTicket()
rajdhani.getStatus()
rajdhani.bookTicket()
rajdhani.getStatus()
rajdhani.bookTicket()




