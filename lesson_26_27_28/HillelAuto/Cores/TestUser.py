from faker import Faker

class TestUser:


    def __init__(self):
        self.faker = Faker()
        self.name, self.last_name = self.generate_name_and_last_name()
        self.mail = self.name + self.last_name + "@gmail.com"
        self.password = self.faker.password()

    def generate_name_and_last_name(self):
        name_and_last_name = self.faker.name()
        name, last_name = name_and_last_name.split()
        return name, last_name
