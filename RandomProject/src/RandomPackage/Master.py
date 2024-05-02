import json;

class Master(object):
    def __init__(self, firstValue, secondValue):
        self.json = dict();
        self.firstValue = firstValue;
        self.secondValue = secondValue;

    def add(self):
        return (self.firstValue + self.secondValue);

    def subtract(self):
         return (self.firstValue - self.secondValue);

    def product(self):
        return (self.firstValue * self.secondValue);

    def divider(self):
        return (self.firstValue / self.secondValue);

    def getJson(self):
        return (self.json);

    def main(self):
        self.json["add"] = self.add();
        self.json["subtract"] = self.subtract();
        self.json["product"] = self.product();
        self.json["divide"] = self.divider();


if __name__ == "__main__":
    obj = Master(20,10);
    obj.main();

    print(json.dumps(obj.getJson(), indent = 3));

