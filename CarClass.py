class Car(object):
    def __init__(self,name="General",model="GM",typ1="saloon", num_of_doors=4, num_of_wheels=4, speed=0):
        self.typ1 = typ1
        self.name = name
        self.model = model
        self.num_of_wheels = num_of_wheels
       #defining conditions for number of wheels 
        if self.typ1== "trailer":
          self.num_of_wheels=8
		#defining number of whhels given car name
        if name == "Porshe" or name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.typ1 == "trailer":
            self.num_of_wheels = 8
        self.speed = 0
    #returns true if vehicle type is saloon and false if not
    def is_saloon(self):
        #"Saloon" if self.typ1=="saloon" else "Trailer"
        if self.typ1 == "saloon":
            return True
        else:
            return False
    def drive(self, spd):
        if spd == 7:
            self.speed = 77
        elif spd == 3:
            self.speed = 1000
        return self

    def speed():
        if self.typ1 == "trailer":
            self.speed = speed
        else:
            self.speed = 1000

if __name__ == "__main__":
    car = Car(model="Mercedes",typ1="Estate")
    car.is_saloon()