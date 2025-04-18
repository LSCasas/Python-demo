class Animal:
    """Animal"""
    def __init__(self, legs, eyes):
        self.legs = legs
        self.eyes = eyes  

class Human(Animal):
    def __init__(self, hair_color, eye_color):
        super().__init__(legs=2, eyes=2)
        self.hair_color = hair_color
        self.eye_color = eye_color
    
class Spider(Animal):
    def __init__(self, hair_color):
        super().__init__(legs=8, eyes=8)
        self.hair_color = hair_color
