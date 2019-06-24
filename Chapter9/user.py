class User():

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("This User is " + full_name + " and age is " +
              str(self.age) + ".")

    def greet_user(self):
        print("Hi " + self.first_name + "~")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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