class lego:
    brand = 'lego'
    matter = 'plastic'


    def fahren(self):
        if self.name == 'auto':
            print('BRUUUUM')
        elif self.name == 'roboter':
            print('i can just walk :(')


project_1 = lego()
project_2 = lego()

project_1.name = 'auto'
project_2.name = 'roboter'

print('#######################')

project_2.fahren()

#print(project_1.name)

for i in [0,1,2,3,4,5]:
    print(i)

