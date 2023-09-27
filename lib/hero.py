class Hero():
    '''
    Герой в игре
    Обладает следующими свойствами
    - coord_x и coord_y - нахождение героя на двумерной карте
    - health - здоровье героя, по умолчанию 1000
    - damage - урон героя, по умолчанию, 10
    - armour - броня от обмундирования, по умолчанию, 0
    - velocity - скорость передвижения, по умолчанию, 5
    '''
    __coord_x = 0
    __coord_y = 0
    __health = 1000
    __damage = 10
    __armour = 0
    __velocity = 5

    def __init__(self):
        pass

    @property
    def coord_x(self):
        return self.__coord_x
    
    @property
    def coord_y(self):
        return self.__coord_y
    
    @property
    def damage(self):
        return self.__damage
    
    @property
    def armour(self):
        return self.__armour
    
    @property
    def velocity(self):
        return self.__velocity
    
    @property
    def health(self):
        return self.__health

    @property.setter
    def damage(self, new_damage):
        self.__damage = new_damage

    @property.setter
    def armour(self, new_armour):
        self.__armour = new_armour

    @property.deleter
    def armour(self):
        print("Броня обнулена, новое значение 0")

    def __str__(self):
        return f'''HERO: {self.coord_x},\n
        {self.coord_y},\n
        {self.health},\n 
        {self.damage},\n
        {self.armour},\n
        {self.velocity}'''

