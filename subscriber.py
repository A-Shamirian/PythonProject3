
# create subscriber class
class Subscriber:

    # create constructor
    def __init__(self, name, userid, password):
        self.__name = name
        self.__userid = userid
        self.__password = password

    # create getter methods
    def get_name(self):
        """Returns name of subscriber."""
        return self.__name

    def get_userid(self):
        """Returns userid of subscriber."""
        return self.__userid

    def get_password(self):
        """Returns password of subscriber."""
        return self.__password

    # create setter methods
    def set_name(self, name):
        """Sets name of subscriber."""
        self.__name = name

    def set_userid(self, userid):
        """Sets userid of subscriber."""
        self.__userid = userid

    def set_password(self, password):
        """Sets password of subscriber."""
        self.__password = password

    # creating __repr__ function
    def __repr__(self):
        return 'Subscriber("{}", "{}", "{}")'.format(self.__name, self.__userid, self.__password)

    # creating equality function
    def __eq__(self, other):
        if self.__name == other.get_name():
            return True
        return False
