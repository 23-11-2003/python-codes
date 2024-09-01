class animal:
    def eat(self):
        print("i can eat")
    def sleep(self):
        print("i can sleep")
class dog(animal):
    def bark(self):
        print("i can bark!")
dog=dog()
dog.eat()
dog.sleep()
dog.bark()            