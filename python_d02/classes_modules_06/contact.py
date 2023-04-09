class Addressable:
    def __init__(self,address):

        self.address =address



class Nameable:
    def __init__(self,name):

        self.name = name



class HasFriend:
    def __init__(self, friends):

        self.friends = [friends]


class Contact(Addressable,Nameable,HasFriend):
    pass