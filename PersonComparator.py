class PersonComparator:
    @staticmethod
    def by_name(person):
        return person.get_name()

    @staticmethod
    def by_age_when_same_name(person):
        return (person.get_name(), person.get_age())
