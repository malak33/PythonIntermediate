class Contact:
    def __init__(self, name='', address='', phone=''):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return '{0}'.format(self.name)

    def __eq__(self, c2):
        if type(self) is not type(c2):
            return False
        elif self.name == c2.name and self.address == c2.address:
            return True
        else:
            return False

c1 = Contact('John Smith', '123 Main St.', '(970)322-9088')
c2 = Contact('John Smith', '123 Main St.', '(970)421-8032')
c3 = Contact('John Smith', '321 Main St.', '(970)421-8032')

print(c1 == c2)
print(c2 == c3)