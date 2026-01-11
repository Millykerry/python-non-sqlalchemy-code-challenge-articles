class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must be longer than 0 characters")
        self._category = value
        


