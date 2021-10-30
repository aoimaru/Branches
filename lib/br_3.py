
class BR3(object):
    def __init__(self, name: str, major: str):
        self._name = name
        self._major = major
    
    @property
    def name(self):
        return self._name
    
    @property
    def major(self):
        return self._major