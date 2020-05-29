
class Contact:

    def __init__(self, first_name, last_name, phone, favorites=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.favorites = favorites
        self.kwargs = kwargs


    def __str__(self):
        data = [
            f'Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone}'
        ]
        if self.favorites == True:
            data.append('В избранных: да')
        else:
            data.append('В избранных: нет')
        data.append('Дополнительная информация:')
        for k, v in self.kwargs.items():
            data.append(f'    {k} - {v}')
        if not self.kwargs:
            data.append('   Отсутствует')
        return '\n'.join(data)

    
if __name__ == "__main__":
    
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')

    print(jhon)
