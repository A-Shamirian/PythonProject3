
# create program class
class Program:

    # creating constructor
    def __init__(self, title, genre, creator, date):
        self.__title = title
        self.__genre = genre
        self.__creator = creator
        self.__date = date

    # create getter methods
    def get_title(self):
        """Returns title of program."""
        return self.__title

    def get_genre(self):
        """Returns genre of program"""
        return self.__genre

    def get_creator(self):
        """Returns creator of program."""
        return self.__creator

    def get_release_date(self):
        """Returns release date of program."""
        return self.__date

    # create setter methods
    def set_title(self, title):
        """Sets title of program"""
        self.__title = title

    def set_genre(self, genre):
        """Sets genre of program."""
        self.__genre = genre

    def set_creator(self, creator):
        """Sets creator of program."""
        self.__creator = creator

    def set_release_date(self, date):
        """Sets release date of program."""
        self.__date = date

    # creating __repr__ function
    def __repr__(self):
        return 'Program("{}", "{}", "{}", "{}")'.format(self.__title, self.__genre, self.__creator, self.__date)

    # creating equality function
    def __eq__(self, other):
        if self.__title == other.get_title():
            return True
        else:
            return False



