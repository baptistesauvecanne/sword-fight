import numpy as np
from core.module import Person, Wizard, HealthPotion

first_user = Person("Hero")
second_user = Wizard("Wizard")

while first_user.is_dead(first_user) == False and second_user.is_dead(second_user) == False:
    random = np.random.randint(2)
    
    if random == 1:
        first_user.hit(second_user)
    else:
        second_user.hit(first_user)

    random_health_potion_use = np.random.randint(3)
        
    if random_health_potion_use == 0:
        HealthPotion.was_used_by(first_user)
    elif random_health_potion_use == 1:
        HealthPotion.was_used_by(second_user)
    else:
        pass

if first_user.get_life_points() <= 0:
    print(first_user.name + " wins")
if second_user.get_life_points() <= 0:
    print(second_user.name + " wins")


