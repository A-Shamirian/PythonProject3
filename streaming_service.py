
# create streaming service class
class StreamingService:

    # create constructor
    def __init__(self, name, program_list, subscriber_list):
        self.__creator = None
        self.__name = name
        self.__program_list = program_list
        self.__subscriber_list = subscriber_list

    # create getter methods
    def get_name(self):
        """Returns name of streaming service."""
        return self.__name

    def get_programs(self):
        """Returns list of programs in streaming service."""
        return self.__program_list

    def get_subscribers(self):
        """Returns list of subscribers in streaming service."""
        return self.__subscriber_list

    def get_program(self, title):
        """Returns program in streaming service."""
        for p in self.__program_list:
            if p.get_title() == title:
                return p
        return None

    def get_subscriber(self, name):
        """Returns subscriber in streaming service."""
        for s in self.__subscriber_list:
            if s.get_name() == name:
                return s
        return None

    # setter methods
    def set_name(self, name):
        """Sets name of streaming service."""
        self.__name = name

    # other methods
    def add_program(self, program):
        """Adds program to streaming service."""
        self.__program_list.append(program)

    def add_subscriber(self, subscriber):
        """Adds subscriber to streaming service."""
        self.__subscriber_list.append(subscriber)

    def remove_program(self, program):
        """Removes program from streaming service."""
        self.__program_list.remove(program)

    def remove_subscriber(self, subscriber):
        """Removes subscriber from streaming service."""
        self.__subscriber_list.remove(subscriber)

    def update_program(self, program):
        """Updates programs in streaming service."""
        for pro in self.__program_list:
            if program == pro:
                if program.get_genre() != '':
                    pro.set_genre(program.get_genre())
                if program.get_creator() != '':
                    pro.set_creator(program.get_creator())
                if program.get_release_date() != '':
                    pro.set_release_date(program.get_release_date())

    def update_subscriber(self, subscriber):
        """Updates subscribers in streaming service."""
        for s in self.__subscriber_list:
            if s == subscriber:
                if subscriber.get_userid() != '':
                    s.set_userid(subscriber.get_userid())
                if s.get_password() != '':
                    s.set_password(subscriber.get_password())


    def sort(self):
        """Sorts the service's program list by title and the service's
        subscriber list by name."""
        title_list = []
        sub_list = []
        for program in StreamingService.get_programs(self):
            title_list.append((program.get_title()))
        title_list.sort()
        sorted_program_list = []
        for title in title_list:
            sorted_program_list.append(self.get_program(title))

        for sub in StreamingService.get_subscribers(self):
            sub_list.append(sub.get_name())
        sub_list.sort()
        sorted_sub_list = []
        for name in sub_list:
            sorted_sub_list.append(self.get_subscriber(name))

        self.__program_list = sorted_program_list
        self.__subscriber_list = sorted_sub_list

    def __repr__(self):
        return 'StreamingService("{}", {}, {})'.format(self.__name, self.__program_list, self.__subscriber_list)












