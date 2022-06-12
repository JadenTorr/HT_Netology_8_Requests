import requests

list_heroes = ['Hulk', 'Thanos', 'Captain America']
# учииывая что имена героев известны с самого начала - сделал списко с их именами глобальной переменной

class SuperHero():
    def __init__(self, heroes_list):
        self.heroes_list = heroes_list
        self.host = 'https://superheroapi.com/api/2619421814940190/'
        self.id_list = []
        self.list_of_int = []

    def get_id(self, name):
        res = 'search/' + name
        response = requests.get(self.host+res).json()['results']

        for el in response:
            if el['name'] == name:
                # print(el['name'] + ': ' + el['id'])
                return (el['id'])
    
    def __add_hero_int(self, id_list):
        for el in self.heroes_list:
            self.id_list.append(self.get_id(el))

        for el in self.id_list:
            self.list_of_int.append(requests.get(self.host+el).json()['powerstats']['intelligence'])

    def show_int_hero(self):
        self.__add_hero_int(self.id_list)
        map(int, self.list_of_int)
        x = list(zip(self.heroes_list, self.list_of_int))
        print(f'Самый умный из героев: {(max(x))}')


some_var = SuperHero(list_heroes)
some_var.show_int_hero()