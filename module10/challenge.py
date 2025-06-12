class DigitalSchool:
    def __init__(self,name, city, state, courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses

    @property
    def name(self):
        return  self.__name
    @name.setter
    def name(self,name):
        self.__name=name


    @property
    def city(self):
        return  self.__city
    @city.setter
    def city(self,city):
        self.__city=city

    @property
    def state(self):
        return  self.__state
    @state.setter
    def state(self,state):
        self.__state=state

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self,courses):
        self.__courses=courses


    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses

        }
    def organize_hackathon(self):
        print("Organizing a generic hackathon")



#define a subclass called DS Prishtina where it has a private atribute called student number and two methods organize_hackathone and scf
class DS_Prishitna(DigitalSchool):
    def __init__(self,name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number=student_number

    def SCF(self):
        print("First edition")

    def organize_hackathon(self):
        print("we are doing a data analysis hackathon")


prishtina_obj=DS_Prishitna("DS_Prishtina","prishtina","kosovo","PHP",3000)
print(prishtina_obj.show_school_info())

class DS_Ferizaj(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number

    def organize_hackathon(self):
        print("we are doing a data analysis hackathon")

    def intership(self):
        print("intership ")

ferizaj_obj=DS_Ferizaj("DS_Ferizaj","Ferizaj","kosovo","PHP",3000)
print(ferizaj_obj.show_school_info())




























