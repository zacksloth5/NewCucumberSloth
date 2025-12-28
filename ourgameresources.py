resources = []
class resource:
    def __init__(self,name,amount=0,condition=""):
        self.amount = amount
        self.condition = condition
        resources.append(self)

    def getamount(self):
        return self.amount

    def changeamount(self,change):
        self.amount += change

    def setamount(self,amount):
        self.amount = amount

def getamount(name,condition=""):
    for resource in resources:
        if resource.name == name and resource.condition == condition:
            return resource.amount
    return Exception("Resource does not exist")

def changeamount(name,change,condition=""):
    for resource in resources:
        if resource.name == name and resource.condition == condition:
            resource.amount += change
            return
    return Exception("Resource does not exist")

def setamount(name,amount,condition=""):
    for resource in resources:
        if resource.name == name and resource.condition == condition:
            resource.amount = amount
            return
    return Exception("Resource does not exist")


foodTypes = ['Raw', 'Fried', 'Roasted']


resource("Wood")
resource("Berries")
resource("Science")
resource("Fruits")
resource("Vegetables")

for meatType in foodTypes:
    resource("Meat",0,meatType)

for fishType in foodTypes:
    resource("Fish",0,fishType)


