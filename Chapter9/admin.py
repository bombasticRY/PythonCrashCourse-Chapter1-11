from Chapter9.user import User

class Privileges():

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges1 = Privileges()

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)