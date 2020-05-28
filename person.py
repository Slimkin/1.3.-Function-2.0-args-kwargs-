
class Contact:

    def __init__(self, first_name, last_name, phone, favorites=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.favorites = favorites
        self.kwargs = kwargs


    def __str__(self):
        data = f'Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone}'
        data2 = self.in_favorites()
        data3 = self.additional_info()
        return (data2)
        

    def in_favorites(self):
        if self.favorites == True:
            return 'В избранных: да'
        else:
            return 'В избранных: нет'

    def additional_info(self):
        yield 'Дополнительная информация:'
        if self.kwargs.items() != None:
            for k, v in self.kwargs.items():
                return f'    {k} - {v}'
        else:
            return 'Отсутствует'

if __name__ == "__main__":
    
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')

    print(jhon)