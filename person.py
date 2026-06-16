import json
from PIL import Image
from datetime import date


def get_person_data():
    """
    Returns the person data loaded from the JSON file.
    """
    with open("data/person_db.json", "r", encoding="utf-8") as file:
        person_data = json.load(file)

    person_object_list = []
    for person_dict in person_data:
        person_object = Person(
            person_dict["id"],
            person_dict["date_of_birth"],
            person_dict["firstname"],
            person_dict["lastname"],
            person_dict["picture_path"],
            person_dict["ekg_tests"],
            person_dict["gender"],
        )
        person_object_list.append(person_object)
    return person_object_list


def get_person_object_by_full_name(full_name):
    persons = get_person_data()
    firstname = full_name.split(", ")[1]
    lastname = full_name.split(", ")[0]

    for person in persons:
        if person.firstname == firstname and person.lastname == lastname:
            return person


class Person:
    @staticmethod
    def get_person_db(pfad_db):
        with open(pfad_db, "r", encoding="utf-8") as file:
            db = json.load(file)
        return db

    ###############################
    @staticmethod  # Decorator um die Methode als static zu kennzeichnen
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the Persons-Dictionary and returns a List auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " + eintrag["firstname"])
        return list_of_names

    @staticmethod
    def find_person_data_by_name(suchstring):
        """Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        # print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            print(eintrag)
            if eintrag["lastname"] == nachname and eintrag["firstname"] == vorname:
                print()

                return eintrag
        else:
            return {}

    @staticmethod
    def load_by_id(person_id):
        person_data = Person.load_person_data()

        for person_dict in person_data:
            if person_dict["id"] == person_id:
                person_object = Person(
                    person_dict["id"],
                    person_dict["date_of_birth"],
                    person_dict["firstname"],
                    person_dict["lastname"],
                    person_dict["picture_path"],
                    person_dict["ekg_tests"],
                    person_dict["gender"],
                )
                return person_object
        return None

    #########################

    def __init__(self, id: int, date_of_birth: int, firstname, lastname, picture_path, ekg_tests, gender="Male"):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests
        self.hr_max = 220 - (2025 - int(date_of_birth))
        self.gender = gender

    def set_hr(self, hr):
        self.hr_max = hr

    def get_full_name(self):
        return self.lastname + ", " + self.firstname

    def get_image(self):
        image = Image.open(self.picture_path)
        return image

    #################################
    def calc_age(self):
        current_year = date.today().year
        age = current_year - int(self.date_of_birth)
        return age

    def calc_max_heart_rate(self):
        age = self.calc_age()

        if self.gender == "male":
            max_heart_rate = 220 - age

            return max_heart_rate
        else:
            max_heart_rate = 226 - age

            return max_heart_rate

    ################################


if __name__ == "__main__":
    # print("_______________________")
    personen = Person.get_person_db("data/person_db.json")
    # print(personen)
    # print("_______________________")

    print("_______________________")
    person = Person.load_by_id(2)

    print(person.get_full_name())
    print(person.calc_age())
    print(person.calc_max_heart_rate())
    print("_______________________")

    # print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()  # statik kein self und geht auf klasse insgesamt und er oben angeordnet
    person_names = Person.get_person_list(persons)  # statik
    # print(person_names)
    # print(Person.find_person_data_by_name("Huber, Julian"))                             #statik
