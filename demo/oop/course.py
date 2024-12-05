class Course:
    # Static attribute or class attribute
    taxRate = 18

    # Constructor
    def __init__(self, title, fee=0):
        # Object attributes
        self.title = title
        self.fee = fee

    # Method
    def netFee(self):
        return self.fee + self.fee * Course.taxRate // 100

    @staticmethod
    def getTaxRate():
        return Course.taxRate

    # create an object of Course


c1 = Course("Python", 10000)
print(c1.netFee())  # Call a method

print(Course.getTaxRate())
c2 = Course("AWS", 5000)
