# You own a car wash and would like to implement a program to keep up with the queue of cars waiting.
# When you open your car wash (at the start of the program), your queue is empty.
# Once the cars start coming, you add them to your queue. Every car has a make (string), a color (string)
# and a plate number (int).
# Once you finish washing a car you remove it from the queue and print all the information about the car.
# If no more cars are waiting (the queue is empty), you close your program.

# The program contains a menu with the following options:
# 1. To insert a car to the queue
# 2. To remove the car from the queue
# When you want to add a car to the queue, you should also add the in

# Inside class Queue, write the following functions:
#  enqueue(c): Insert car cat the rear of the queue.
#  dequeue(): Remove and return from the queue the car at the front
#  size(): Return the number of cars in the queue.
#  isEmpty(): Return a Boolean (True or False) value that indicates whether the queue is empty.
#  front(): Return, but do not remove, the front car in the queue


###############################################################################################################



class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

    def __str__(self):
        return f"Make: {self.make}, Color: {self.color}, Plate Number: {self.plate_number}"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, car):
        self.items.append(car)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return None


def main():
    wash_car = Queue()

    while True:
        print("\nCar Wash Menu:")
        print("1. Add a car")
        print("2. Remove a car")
        print("3. Exit")

        choice = input("Enter your choice Number: ")

        if choice == "1":
            make = input("Enter car make: ")
            color = input("Enter car color: ")
            plate_number = int(input("Enter car plate number: "))
            car = Car(make, color, plate_number)
            wash_car.enqueue(car)
            print(f"Car {car} added.")

        elif choice == "2":
            if not wash_car.isEmpty():
                removed_car = wash_car.dequeue()
                print(f"Car {removed_car} removed  and washed.")
            else:
                print("No cars .")

        elif choice == "3":
            break

        else:
            print("Wrong Number. Please enter a valid number from 1 to 3")



main()
