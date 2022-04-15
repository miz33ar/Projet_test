from Module import *


def test_wizard_points():
    wiz=Wizard('wiz')
    hp=wiz.get_life_points()
    expected_result=80
    assert hp == expected_result

# def test_wizard_nom():
#     wiz=Wizard('wiz')
#     hp=wiz.name
#     expected_result="wiz"
#     assert hp == expected_result

# def test_Person_points():
#     user=Person('pers')
#     hp=user.get_life_points()
#     expected_result=100
#     assert hp == expected_result

# def test_Person_nom():
#     user=Person('pers')
#     hp=user.name
#     expected_result="pers"
#     assert hp == expected_result

# def test_person_hit():
#     wiz=Wizard('wiz')
#     hp_wiz=user.get_life_points()
#     user=Person('pers')
#     hp=user.get_life_points()
#     wiz.hit(user)
#     hp_new=user.get_life_points()

#     assert hp_new == hp -15

test_person_hit()