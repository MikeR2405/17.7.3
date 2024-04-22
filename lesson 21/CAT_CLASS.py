class Cat:
    def __init__(self, name ='', sex= '', age=0):
        self.name = name
        self.sex = sex
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get('name')
        self.sex = cat_dict.get('sex')
        self.age = cat_dict.get('age')
