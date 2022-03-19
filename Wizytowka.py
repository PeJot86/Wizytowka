from faker import Faker
fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, first_name, last_name, private, email):
       self.first_name = first_name
       self.last_name = last_name
       self.private = private
       self.email = email 
    
    def contact(self):
            print (f"Wybieram numer prywatny: {self.private}, dzwonię do: {self.first_name} {self.last_name}.")    
    
    
class BusinessContact(BaseContact):
    def __init__(self, company, ocupation, phone, *args,**kwargs):
       super().__init__(*args, **kwargs)
       self.company = company
       self.ocupation = ocupation
       self.phone = phone

    def contact(self):
       print (f"Wybieram numer służbowy: {self.phone}, dzwonię do: {self.first_name} {self.last_name}.")
   

cards = [
    BaseContact('Tomasz', 'Luźny', 123456789, 's@x.pl'),
    BaseContact('Artur', 'Ważny', 987654321, 's@x.pl'),
    BaseContact('Aleksandra', 'Ważna', 11223344, 's@x.pl'),
    BaseContact('Igor', 'Ważny', 999888777, 's@x.pl'),
    BusinessContact('Spawacz', 'Stalex', 123456789, 'Artur', 'Ważny', 987654321, 's@x.pl'),
    BusinessContact('Sprzątaczka', 'SP. nr3', 123456789, 'Andrzej', 'Nikt', 11223344, 's@x.pl'),
    BusinessContact('Lek. med.', 'Szpital Wojewódzki', 123456789, 'Iga', 'Zielona', 999888777, 's@x.pl')]


by_name = sorted(cards, key=lambda x: x.last_name)
for i in by_name :
    i.contact  ()

def create_base_contact():
    return BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())

def create_business_contact():
    return BusinessContact(fake.company(), fake.job(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())

def create_contact(type):
    if type == "BaseContact":
        return create_base_contact()
    elif type == "BusinessContact":
        return create_business_contact()
    else:
        raise "Invalid type name"

def create_many_contacts(count, type):
    contacts=[]
    for i in range (0, count):
            contacts.append (create_contact(type))
    return contacts

my_contacts = create_many_contacts(5, "BusinessContact")
for i in my_contacts:
    i.contact()
