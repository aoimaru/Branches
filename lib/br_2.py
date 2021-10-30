
class BR2(object):
    def __init__(self, name: str, gender: bool):
        self._name = name
        self._gender = gender
    
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return "Male" if self._gender == True else "Female"