class Travel:
    def __init__(self, destination, root, time):
        self.Des = destination
        self.root = root
        self.Time = time
        print(self.Des, self.root, self.Time)

    def ticket(self, price, number_tickets):
        self.p = price
        self.no_t = number_tickets

    def ticket_Details(self):
        print("each ticket price for {}:".format(self.Des),self.p)
        print("number of tickets for {}:".format(self.Des),self.no_t)
        print("total amount is:",self.p *self.no_t)
        print("Thanks")


T = Travel("Kadapa", "xyz", 3.30)

T.ticket(300, 2)
T.ticket_Details()

print("\n")
L = Travel("ATP", "ABC", 3)
L.ticket(250, 5)
L.ticket_Details()

print("\n")
b= Travel("Banglore", "----", 4)
b.ticket(200, 3)
b.ticket_Details()