
class BR1(object):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def age_check(self):
        if self._age >= 20:
            return True
        else:
            return False