class calculator:
    def _init_(self,num):
        self.number  = num

    @staticmethod
    def man():
        print("hello developer your answers are just below .......................")
    def square(self):
        print(f"square of {self.number} is {self.number **2 }")  
    def squareroot(self):
        print(f"squareroot of {self.number} is {self.number ** 0.5} ")
    def cube(self):
        print(f"cube of {self.number} is {self.number **3}" )


a = calculator(int(input("type number to find square,squareroot and cube of number =>")))
a.man()
a.square()
a.squareroot()
a.cube()
