x=5
ranks = {str(i): i for i in range(2,10)}
ranks.update({"A":14, "K":13, "Q":12, "J":11, "T":10})

ranks_inverse = [str(k) for k in range(2,10)]
ranks_inverse.append("T")
ranks_inverse.append("J")
ranks_inverse.append("Q")
ranks_inverse.append("K")
ranks_inverse.append("A")
print(ranks_inverse)

def sq(nums):
    for i in nums:
        yield (i*i)

mynums = sq([1,3,9])

for num in mynums:
    print (num)

import sys
print(sys.path)

print ([
            'High card',
            'One pair',
            'Two pair',
            'Three of a kind',
            'Straight',
            'Flush',
            'Full house',
            'Four of a kind',
            'Straight flush',
            'Royal flush',
        ].index('Flush'))


print ( 6 in [1,6,7])



class Foo(object):
    def __init__(self):
        self.name = 'John'

instance_name_1 = Foo()

globals()['instance_name_2'] = Foo()

instance_name_1.height = 80
instance_name_2.height = 100
print(instance_name_2.height)
"""
def create_new_instance(class_name,instance_name):
    globals()[instance_name] = class_name()
    #print('Class instance '{}' created!'.format(instance_name))

create_new_instance(Foo,'new_instance') #Class instance 'new_instance' created!
print(new_instance.name) #John


def create_instance(class_name,instance_name):
    count = 0
    while True:
        name = instance_name + str(count)
        globals()[name] = class_name()
        count += 1
        print('Class instance: {}'.format(name))
        yield True

generator_instance = create_instance(Foo,'instance_') 

for i in range(5):
    next(generator_instance)

#out
#Class instance: instance_0
#Class instance: instance_1
#Class instance: instance_2
#Class instance: instance_3
#Class instance: instance_4

print(instance_0.name) #john
print(instance_1.name) #john
print(instance_2.name) #john
print(instance_3.name) #john
print(instance_4.name) #john

#print(instance_5.name) #error.. we only created 5 instances.. 

next(generator_instance) #Class instance: instance_5
print(instance_5.name) #John  Now it works.. 
"""
print('\u2667')
print('\u2662')
print('\u2661')
print('\u2664')

def update_next_turn(iterable):
    iterator = iter(iterable)
    prev_item = 5
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (next_item)
        prev_item = current_item
        current_item = next_item
    yield (None)


for next in update_next_turn([1,2,3,4,5,6,7,8,9]):
    print (next)



def isSitting(player_instance):
    try:
        a = player_instance.dealt_hand
        return True
    except NameError:
        print("FUCK")
        return False

isSitting(dgs)
