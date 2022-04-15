# -*- coding: utf-8 -*-
from core.module import Person, Wizard, HealthPotion

def test_person():
    name = 'Jack'
    person = Person(name)
    expected_name = 'Jack'
    expected_life_points = 100
    actual_name = person.name
    actual_life_points = person.life_points
    assert expected_name == actual_name
    assert expected_life_points == actual_life_points
    
def test_person_hit():
    name = 'Jack'
    person = Person(name)
    person.hit(person)
    expected_life_points = 90
    actual_life_points = person.life_points
    assert expected_life_points == actual_life_points
    
def test_person_is_dead():
    name = 'Jack'
    person = Person(name)
    person.life_points = 0
    expected_is_dead = True
    actual_is_dead = person.is_dead(person)
    assert expected_is_dead == actual_is_dead
    
def test_person_gained_life_points():
    name = 'Jack'
    person = Person(name)
    person.gained_life_points(10)
    expected_life_points = 110
    actual_life_points = person.life_points
    assert expected_life_points == actual_life_points
    
def test_person_get_life_points():
    name = 'Jack'
    person = Person(name)
    expected_life_points = 100
    actual_life_points = person.get_life_points()
    assert expected_life_points == actual_life_points
    
def test_wizard():
    name = 'Jack'
    wizard = Wizard(name)
    expected_name = 'Jack'
    expected_life_points = 80
    actual_name = wizard.name
    actual_life_points = wizard.life_points
    assert expected_name == actual_name
    assert expected_life_points == actual_life_points

def test_wizard_hit():
    name = 'Jack'
    wizard = Wizard(name)
    wizard.hit(wizard)
    expected_life_points = 65
    actual_life_points = wizard.life_points
    assert expected_life_points == actual_life_points
    
def test_health_potion():
    name = 'Jack'
    person = Person(name)
    potion = HealthPotion()
    potion.was_used_by(person)
    expected_life_points = 110
    actual_life_points = person.life_points
    assert expected_life_points == actual_life_points    
    
    