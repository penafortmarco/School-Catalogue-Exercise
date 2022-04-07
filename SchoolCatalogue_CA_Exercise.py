# Parent class

class School:
    def __init__(self, name, level, numOfStudents):
        self.__name = name
        self.__level = level
        self.__num_of_students = numOfStudents
# ------------Methods---------------------------------

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_numOfStudents(self):
        return self.__num_of_students

    def set_numOfStudents(self, numOfStudents):
        self.__num_of_students = numOfStudents

    def __repr__(self):
        school_data = '''
        School's name: {}
        Level: {}
        Number of students: {}
        '''.format(self.__name, self.__level, self.__num_of_students)
        return school_data

    # Inherited classes


class PrimarySchool(School):
    def __init__(self, name, level, numOfStudents, pickup_policy):
        super().__init__(name, level, numOfStudents)
        self.__pickup_policy = pickup_policy
# ------------Methods---------------------------------

    def get_pickup_policy(self):
        return self.__pickup_policy

    def __repr__(self):
        return super().__repr__()+'Pickup policy: {}'.format(self.__pickup_policy)


class HighSchool(School):
    def __init__(self, name, level, numOfStudents, sports_teams):
        super().__init__(name, level, numOfStudents)
        self.__sports_teams = sports_teams
# ------------Methods---------------------------------

    def get_sports_teams(self):
        return self.__sports_teams

    def __repr__(self):
        str_sports = 'Sports: |'
        for i in self.__sports_teams:
            str_sports += i + '|'
        return super().__repr__() + str_sports
#------------------------------------------------------------------------#

    # Implement of inherited objects


school1 = PrimarySchool('Super Technology Center',
                        'Primary', 250,
                        'Pickup after 3pm')
school2 = HighSchool('High School Musical',
                     'High', 300,
                     ['Baseball', 'Football', 'Soccer'])
print(school1.__repr__())
print(school2.__repr__())
