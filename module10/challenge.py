class DigitalSchool():
    def __init__(self,name, city, state, courses):
        self.name=name
        self.city=city
        self.state=state
        self.courses=courses

    @property
    def name(self):
     return self.name


     @name.setter
     def name(self, name):
      self.name = name

     @property
     def city(self):
        return self.city

     @city.setter
     def city(self, city):
        self.city = city

     @property
     def State(self):
         return self.name

     @state.setter
     def State(self, state):
          self.state = state

     @property
     def Courses(self):
         return self.courses

     @state.setter
     def Courses(self, courses):
          self.courses = courses

