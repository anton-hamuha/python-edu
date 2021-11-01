class mouse:
    def talk(self):
        print('\nmouse says: squeak')
def coat(self):
    print('mouse wears: fur')
from duck import*
from mouse import*
def describe(object):
    object.talk()
    object.coat()
donald = duck()
mickey = mouse()
describe(donald)
describe(mickey)
