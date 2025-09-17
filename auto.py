class Truck:
    # The class represents a truck with a maximum capacity of 3000 kg
    capacity = 3000
    load_weight = 0

    def load(self, weight):
        if self.load_weight + weight <= self.capacity:
            self.load_weight += weight

    def unload(self, weight):
        if weight <= self.load_weight:
            self.load_weight -= weight

    def display_load(self):
        print(f"The truck is loaded with {self.load_weight} kg")

# Creating an instance
tatra = Truck()

tatra.load(10000)
tatra.load(500)
tatra.unload(300)
tatra.unload(1000)
# Output
tatra.display_load()