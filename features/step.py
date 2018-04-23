from lettuce import *
from nose.tools import assert_equals
from beacon import Beacon as b

@step(u'I have a key of "([^"]*)" and "([^"]*)"')
def test_keys(step, k1, k2):
    print (k1)
    print (k2)
    world.key = k1
    world.key2 = k2

@step('I build Beacon')
def calc_frequence(step):
    world.dai_beacon = b.Beacon()
        
    
@step('I receive (\d)')
def receive(step,result):
    world.dai_beacon.config()
    res = world.dai_beacon.start(world.key,world.key2)
    assert_equals(res, int(result))

