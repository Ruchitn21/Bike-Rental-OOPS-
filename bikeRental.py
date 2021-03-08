import datetime

class BikeRental:

    def __init__(self,stock=0):

        self.stock= stock
    
    def displaystock(self):

        print(f"Currently we have {self.stock} bikes available to rent")
        return self.stock
    
    def rentBikeonHourlyBasis(self,n):

        if n<=0:
            print("Number of Bikes should be positive")
            return None
        
        elif n>self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent")
            return None
        
        else:
            now= datetime.datetime.now()
            print(f"You have rented {n} bikes on hourly basis today at {now.hour}")
            print("You will be charged Rs.10 per hour per bike")
            print("We hope that you enjoy our service")

            self.stock-=n
            return now
        
    def rentBikeonDailyBasis(self,n):

        if n<=0:
            print("Number of bikes should be positive")
            return None
        
        elif n> self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent")
            return None
        
        else:
            now= datetime.datetime.now()
            print(f"You have rented {n} bikes on daily basis today at {now.hour}")
            print("You will be charged Rs.200 for each day per bike")
            print("We hope that you enjoy our service")

            self.stock-=n
            return now
    
    def rentBikeonWeeklyBasis(self,n):

        if n<=0:
            print("Number of bikes should be positive")
            return None
        
        elif n>self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available on rent")
            return None
        
        else:
            now= datetime.datetime.now()
            print(f"You have rented {n} bikes on weekly basis at {now.hour}")
            print("You will be charged Rs.1200 per week")
            print("We have that you enjoy our service")

            self.stock-=n
            return now
        
    def returnBike(self,request):

        rentalTime, rentalBasis, numOfBikes= request
        bill= 0

        if rentalTime and rentalBasis and numOfBikes:

            self.stock+=numOfBikes
            now= datetime.datetime.now()

            rentalPeriod= now-rentalTime

            if rentalBasis==1:  # on hourly basis
                bill= round(rentalPeriod.seconds/3600)*10*numOfBikes

            elif rentalBasis==2:  # on daily basis
                bill= round(rentalPeriod.days)*200*numOfBikes
            
            elif rentalBasis==3:  # on weekly basis
                bill= round(rentalPeriod.days/7)*1200*numOfBikes
            
            if 3<=numOfBikes<=5:
                print("Congrats..!! You are eligible for Family Rental Promotion of 30% discount")
                bill= bill*0.7

            print("Thanks for returning your bikes. Hope you enjoyed our service")
            print(f"Your bill is : Rs.{bill}")
            return bill

        else:
            print("Are you sure you rented a bike with us??")
            return None   

class Customer:

    def __init__(self):

        self.bikes= 0
        self.rentalBasis= 0
        self.rentalTime= 0
        self.bill= 0

    def requestBike(self):

        bikes= input("How many bikes would you like to rent??")
        
        try:
            bikes= int(bikes)
        
        except ValueError:
            print("That's not a positive Integer")
            return -1
        
        if bikes<1:
            print("Invalid Input. Number of bikes should be greater than 0..!!")
            return -1
        
        else:

            self.bikes= bikes

        return self.bikes
    
    def returnBike(self):

        if self.rentalBasis and self.rentalTime and self.bikes:


            return self.rentalTime, self.rentalBasis, self.bikes  
        else:

            return 0,0,0

