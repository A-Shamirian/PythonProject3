import csv
from program import Program
from subscriber import Subscriber
from streaming_service import StreamingService


def build_new_service(service_data):
    """Takes data from a streaming service and returns a streaming service object."""
    found = False
    while not found:  # keep running through the loop until a valid file is inputted
        try:
            with open(service_data, 'r') as file_handle:  # if a valid file was found, continue with function
                found = True
        except IOError:  # if file was not found, continue loop
            return None
    with open(service_data, 'r') as file_handle:
        reader = csv.reader(file_handle)
        service_name = next(reader)
        program_list = []
        sub_list = []
        is_program = False
        for row in reader:
            if row[0] == 'PROGRAMS' and len(row) == 1:
                is_program = True
            if is_program and len(row) > 1:
                p = Program(row[0], row[1], row[2], row[3])
                program_list.append(p)
            if row[0] == 'SUBSCRIBERS' and len(row) == 1:
                is_program = False
            if not is_program and len(row) > 1:
                s = Subscriber(row[0], row[1], row[2])
                sub_list.append(s)
    return StreamingService(service_name, program_list, sub_list)


def update_service(update_file, streaming_service):
    """Update the contents of the given streaming service using the contents of the
    given update file and return the updated and sorted streaming service."""
    found = False
    while not found:  # keep running through the loop until a valid file is inputted
        try:
            with open(update_file, 'r') as file_handle:  # if a valid file was found, continue with function
                found = True
                reader = csv.reader(file_handle)
                next(reader)
                is_program = False # becomes True when we hit the program line in the input file
                # reading each line as a list of words and storing them in row object
                for row in reader:
                    if row[0] == 'PROGRAMS' and len(row) == 1:
                        is_program = True
                    if row[0] == '+' and is_program:
                        p = Program(row[1], row[2], row[3], row[4])
                        streaming_service.add_program(p)
                        print('Adding program... {}'.format(row[1]))
                    elif row[0] == '-' and is_program == True:
                        p = Program(row[1], row[2], row[3], row[4])
                        streaming_service.remove_program(p)
                        print('Removing program... {}'.format(row[1]))
                    elif row[0] == '^' and is_program == True:
                        p = Program(row[1], row[2], row[3], row[4])
                        streaming_service.update_program(p)
                        print('Updating program... {}'.format(row[1]))
                    elif row[0] == 'SUBSCRIBERS' and len(row) == 1:
                        is_program = False # becomes False when we hit the subscriber line in the input file
                    elif row[0] == '+' and not is_program:
                        s = Subscriber(row[1], row[2], row[3])
                        streaming_service.add_subscriber(s)
                        print('Adding subscriber... {}'.format(row[1]))
                    elif row[0] == '-' and not is_program:
                        s = Subscriber(row[1], row[2], row[3])
                        streaming_service.remove_subscriber(s)
                        print('Removing subscriber... {}'.format(row[1]))
                    elif row[0] == '^' and not is_program:
                        s = Subscriber(row[1], row[2], row[3])
                        streaming_service.update_subscriber(s)
                        print('Updating subscriber... {}'.format(row[1]))
                streaming_service.sort()  # sort
                return "done"
        except IOError:  # if file was not found, continue loop
            raise IOError




def write_update(outfile, streaming_service):
    """Takes an updated streaming service and writes the data to the file name given."""
    with open(outfile, 'w') as outfile:
        header = StreamingService.get_name(streaming_service) # get the name of the streaming service
        header = str(header).strip('[').strip(']').strip("'") # strip header
        outfile.write(header.upper()) # write streaming service header capitalized
        outfile.write('\nPROGRAMS')
        p = streaming_service.get_programs()
        for element in p: # get info from programs and write to outfile
            titles = Program.get_title(element)
            genres = Program.get_genre(element)
            creators = Program.get_creator(element)
            dates = Program.get_release_date(element)
            outfile.write('\n{},{},{},{}'.format(str(titles), str(genres), str(creators), str(dates)))
        outfile.write('\nSUBSCRIBERS')
        s = streaming_service.get_subscribers()
        for element in s: # get info from subscribers and write to outfile
            names = Subscriber.get_name(element)
            userids = Subscriber.get_userid(element)
            passwords = Subscriber.get_password(element)
            outfile.write('\n{},{},{}'.format(str(names), str(userids), str(passwords)))
        outfile.write('\n')




