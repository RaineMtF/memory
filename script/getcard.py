import common
from datetime import datetime

def load_card():
    return common.load_json('people.json')

def get_countdown(target):
    today = datetime.now()
    target = datetime.strptime(target, "%Y-%m-%d")
    target = datetime(today.year, target.month, target.day)
    if target < today:
        target = datetime(target.year + 1, target.month, target.day)
    return (target - today).days

def m_cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj)
    return K

def cmp_date(a, b, key):
    if a[key] == 'None':
        return False
    if b[key] == 'None':
        return True
    return get_countdown(a[key]) < get_countdown(b[key])

def cmp_b(a, b):
    return cmp_date(a, b, 'born')
def getcard_b(i):
    return sorted(load_card(), key=m_cmp_to_key(cmp_b))[i]

def cmp_d(a, b):
    return cmp_date(a, b, 'departed')
def getcard_d(i):
    return sorted(load_card(), key=m_cmp_to_key(cmp_d))[i]
