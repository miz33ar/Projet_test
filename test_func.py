from Module import Wizard,Person,HealthPotion

def test_wizard_points():
    wiz=Wizard('wiz')
    hp=wiz.get_life_points()
    expected_result=80
    assert hp == expected_result

def test_wizard_nom():
    wiz=Wizard('wiz')
    hp=wiz.name
    expected_result="wiz"
    assert hp == expected_result

def test_Person_points():
    user=Person('pers')
    hp=user.get_life_points()
    expected_result=100
    assert hp == expected_result

def test_Person_nom():
    user=Person('pers')
    hp=user.name
    expected_result="pers"
    assert hp == expected_result

def test_wizer_hit():
    wiz=Wizard('wiz')
    user=Person('pers')
    hp_wiz=user.get_life_points()
    hp=user.get_life_points()
    wiz.hit(user)
    hp_new=user.get_life_points()
    assert hp_new == hp -15
def test_person_hit():
    wiz=Wizard('wiz')
    user=Person('pers')
    hp_wiz=user.get_life_points()
    hp=wiz.get_life_points()
    user.hit(wiz)
    hp_new=wiz.get_life_points()
    assert hp_new == hp -10

def test_Person_is_dead():
    user = Person('pers')
    user.life_points = 0
    assert user.is_dead() == True

def test_gained_life_points():
    user = Person('pers')
    user.gained_life_points(20)
    result = user.life_points
    except_result = 120
    assert except_result == result



