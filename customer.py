class Customer:
    def __init__(self, id, custPin = 1234 ) :
        self.id = id
        self.pin = custPin

    def checkId(self):
        return self.id
    def checkPin(self):
        return self.pin
    