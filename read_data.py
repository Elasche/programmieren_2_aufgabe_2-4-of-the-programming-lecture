import json

def get_names(person_data):
    names = [
        f"{person['firstname']} {person['lastname']}"
        for person in person_data
    ]
    return names


def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data




if __name__ == "__main__":
    person_data = load_person_data()
    print(type(person_data))

    print(person_data)
    print(get_names(person_data))

