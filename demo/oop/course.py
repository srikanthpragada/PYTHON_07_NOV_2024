class Course:
    # Constructor
    def __init__(self, title, fee=0):
        # Object attributes
        self.title = title
        self.fee = fee
        self.taxRate = 18

    # Method
    def netFee(self):
        return self.fee + self.fee * self.taxRate // 100

    def getTaxRate(self):
        return self.taxRate

    # create an object of Course


c1 = Course("Python", 10000)
print(c1.netFee())  # Call a method
print(c1.fee, c1.title)

c2 = Course("AWS", 5000)
