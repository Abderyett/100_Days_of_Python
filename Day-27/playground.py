# Unlimited positioned agruments
def add(*args):
    res = sum(list(args))
    # print(res)


add(1, 2, 3, 4, 5, 6, 7, 8)

# Unlimited named agruments


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(value)
    #     print(key)
    # print(kwargs["add"])
    n += kwargs["add"]
    n /= kwargs["devide"]
    # print(n)


calculate(2, add=5, devide=3)


class Car:
    def __init__(self, **kw):
        #! we use get if the key didn't exist in dic it wouldn't crash
        self.brand = kw.get("brand")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(brand="Nissan", model="GT-R")


print(my_car.model)
