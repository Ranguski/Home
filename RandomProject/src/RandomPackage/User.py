class User(object):
    user = None;

    @staticmethod
    def getInstance():
        if (User.user is None):
            User.user = User("", "", "");
        return (User.user);

    @staticmethod
    def getVariables():
        if (User.user is None):
            User.getInstance();
        return (User.user.__dict__);

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname;
        self.lastname = lastname;
        self.age = age;

    def toJson(self):
        return (self.__dict__);
