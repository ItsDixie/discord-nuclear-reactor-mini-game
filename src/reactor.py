import asyncio
from math import floor

class Reactor(): # VVER-1000
    #         uran235
    __Nfuel = [5.56]
    __t = 0.001

    def __init__(self, CR, AZsize, fuel):   # cr - control rods, amount | AZsize - active zone size | fuel - fuel type
        self.CR = CR
        self.AZsize = AZsize # in cm
        self.fuel = fuel 

        self.CRpower = 1
        self.k = 1
        self.pastST = 0

    async def manageCR(self): # state - state of the control rods 1-full inside, 0-full outside
        state = float(input('Enter control rods state: '))
        if(self.pastST > state):
            print('Upping...')
        else:
            print('Lowering...')
        await asyncio.sleep(state + self.CR * 1.5)
        self.CRpower =  (self.CR ** 7) * state
        self.pastST = state
        print(f'CRpower = {self.CRpower}')
        

    async def run(self):
        print('Intiating start-up procedure...')
        await asyncio.sleep(floor((self.AZsize + self.CR) / 30))
        self.alive = True
        print('Reactor started')
        while self.alive:
            await asyncio.sleep(floor((self.AZsize + self.CR) / 100))
            await self.reaction()
            await self.manageCR()

    async def danger(self):
        pass # WIP


    async def reaction(self):
        self.k = (((self.__Nfuel[0] - 1) / self.__t) * self.AZsize) / self.CRpower
        if self.k == 0:
            self.k = 1
        self.p = (self.k -1) / self.k
        print('---------')
        print(f'p = {self.p}')
        print(f'k = {self.k}')


vver = Reactor(8, 80, 'Uran')
asyncio.run(vver.run())