class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

user = Human("Yuichi Kawata", 30)

user.printinfo()