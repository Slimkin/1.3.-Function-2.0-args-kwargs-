from person import Contact

class PhoneBook:

    def __init__(self, name_pb):
        self.name_pb = name_pb
        self.pb_data = []
        print(f'создана телефонная книга {name_pb}')

    def show_all(self):
        if not self.pb_data:
            print(f'телефонная книга {self.name_pb} пуста')
        else:
            for n, contact in enumerate(self.pb_data, 1):
                print(f'{n} - {contact}\n')


    def add_new(self, contact_name, first_name, last_name, phone, **kwargs):
        not_new = False
        for contact in self.pb_data:
            if contact.first_name == first_name and contact.last_name == last_name:
                not_new = True
                print(f'{contact_name} - такая запись уже существует')
        if not_new == False:
            contact_name = Contact(first_name, last_name, phone, **kwargs)
            self.pb_data.append(contact_name)
            print(f'{contact_name}\n - запись создана -')


    def del_contact(self, phone):
        not_number = True
        for contact in self.pb_data:
            if contact.phone == phone:
                self.pb_data.remove(contact)
                not_number = False
                print(f'{contact}\n - был удален -')
        if not_number == True:
            print(f'{phone} - нет такого номера')


    def search_favorites(self):
        self.f_list = []
        for contact in self.pb_data:
            if contact.favorites == True:
                self.f_list.append(contact)
        if not self.f_list:
            print('нет избранных')
        else:
            for n, name in enumerate(self.f_list, 1):
                print(f'{n} - {name}\n')


    def search_by_name(self, first_name, last_name):
        not_contact = True
        for contact in self.pb_data:
            if contact.first_name == first_name and contact.last_name == last_name:
                print(contact)
                not_contact = False
        if not_contact == True:
            print('нет такой записи')


if __name__ == "__main__":
    
    pb = PhoneBook('test')
    print("-----"*10)
    pb.show_all()
    print("-----"*10)
    pb.add_new('jhonny', 'Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print("-----"*10)
    pb.add_new('jhonny', 'Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print("-----"*10)
    pb.add_new('zily', 'duck', 'zilla', '46480', favorites=True)
    print("-----"*10)
    pb.search_favorites()
    print("-----"*10)
    pb.show_all()
    print("-----"*10)
    pb.del_contact('+71234567809')
    print("-----"*10)
    pb.show_all()
    print("-----"*10)
    pb.search_by_name('Jhon', 'Smith')
    print("-----"*10)
    pb.search_by_name('duck', 'zilla')
    print("-----"*10)
    pb.del_contact('+71234567809')