class WrongStatusException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PizzaExistenceException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)