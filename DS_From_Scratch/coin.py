import enum, random, pprint

from Stats import normal_pdf

class Coin(enum.Enum):
    HEADS = 1
    TAILS = 0


def random_coin()->Coin:
    return random.choice([Coin.HEADS, Coin.TAILS])

random.seed()

head_count = 0
tail_count = 0

for _ in range(10000):
    value = random_coin()
    if value == Coin.HEADS:
        head_count += 1
    else:
        tail_count += 1

print(head_count, tail_count)        


# Function converts base 10 numbers to base 2. 
def to_base_two(val : int) -> int :
    '''Converts `val` to base 2. Also, i just found out that int() can convert its input from one base to another. 
       Check out the docs.'''
    reminder = []
    base = 2
    while val != 0 :
        reminder.append( val % base )
        val =  int(val / 2) if val != 1  else 0    
    return int(''.join(str(i) for i in reversed(reminder)))   

print(to_base_two(333))                  


