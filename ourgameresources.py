resources = []
class resource:
    def __init__(self,name,amount=0,condition=""):
        self.amount = amount
        self.name = name
        self.condition = condition
        resources.append(self)

    def getamount(self):
        return self.amount

    def changeamount(self,change):
        self.amount += change

    def setamount(self,amount):
        self.amount = amount

def getamount(resourceName,condition=""):
    for x in resources:
        if x.name == resourceName and x.condition == condition:
            return x.amount
    return Exception("Resource does not exist")

def changeamount(resourceName,change,condition=""):
    for x in resources:
        if x.name == resourceName and x.condition == condition:
            x.amount += change
            return
    return Exception("Resource does not exist")

def setamount(resourceName,amount,condition=""):
    for x in resources:
        if x.name == resourceName and x.condition == condition:
            x.amount = amount
            return
    return Exception("Resource does not exist")


foodTypes = ['raw', 'fried', 'roasted']


resource("wood")
resource("berries")
resource("science")
resource("fruits")
resource("vegetables")

for meatType in foodTypes:
    resource("meat",0,meatType)
for fishType in foodTypes:
    resource("fish",0,fishType)
