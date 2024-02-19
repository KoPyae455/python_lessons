class lady:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Frozen dancing lady!')

    def get_married_model(self):
        print(f"I'm marrying with {self.make} and {self.model}!")# and {self.Ex_id}


girlfriend = lady('Taylor Swift', 'Gal Gadot')

# girlfriend = lady()
# girlfriend.moves()

# print(girlfriend.make)
# print(girlfriend.model)

girlfriend.get_married_model()
girlfriend.moves()

girlfriend2 = lady('Jeon Somi', 'Blackpink')
girlfriend2.get_married_model()
girlfriend2.moves()


class Ex(lady):
    def __init__(self, make, model):#, Ex_id
        super().__init__(make, model)
        # self.make = make
        # self.model = model
        # self.Ex_id = Ex_id

    def moves(self):
        print('My Ex is still loving me')

class Wife(lady):
    def moves(self):
        print('Charming and kindhearted wives.') #overwrite

class Childhood_fri(lady):
    pass

chitsone = Ex('Wah', 'Whitey') #, 'Yupar'
wifey = Wife('Zar', 'Wai')
chil = Childhood_fri('Ei', 'Phyu')

chitsone.get_married_model()
chitsone.moves()

wifey.get_married_model()
wifey.moves()

chil.get_married_model()
chil.moves()


for MK in (girlfriend, girlfriend2, chitsone, wifey, chil): #polymorphism
    MK.get_married_model() #same method != same response
    MK.moves()

