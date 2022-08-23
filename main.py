# Assignment 4: Annie Shamirian (251103387)

import file_processing

def main():
    """Main function prompts the user for a file to update, a file with the updates, and an outfile to
    write updates to. Upon exiting, the program creates a new updated file.
    If the user gives invalid input at any point, the program will continue to prompt the user for correct
    input unless the user exits the program voluntarily."""
    try: # if the user does not respond with Y, exit the program
        user_input = input('Would you like to update a file? Y/N\n').upper()
        if user_input != 'Y' and user_input != 'N':
            raise ValueError
        elif user_input == 'N':
            print('Exiting program...')
            exit(0)
    except ValueError:
        exit(0)
    while True: # ask for streaming service file until valid input is received or program is exited
        user_input = input("Please enter the streaming service creation file (or 'done' to exit):\n")
        if user_input == 'done':
            print('Exiting program...')
            exit(0)

        found = False
        while found is False: # ask user for updating file until valid input is received or program is exited
            try:
                with open(user_input, 'r') as file_handle:
                    streaming_service = file_processing.build_new_service(user_input)
                    if streaming_service is None:
                        raise IOError
                    update_file = input(
                        "Please enter the update file you would like to read (or 'done' to exit):\n")
                    if update_file == 'done':
                        print('Exiting program...')
                        exit(0)
                    else:
                        try:
                            updating = file_processing.update_service(update_file, streaming_service)
                            if updating is None:
                                raise IOError
                            user_outfile = input('Please enter the name of the new file to be written:\n')
                            if user_outfile == 'done':
                                print('Exiting program...')
                                exit(0)
                            else:
                                file_processing.write_update(user_outfile, streaming_service)
                                found = True
                                print('Writing updates to {}...'.format(user_outfile))

                            user_input = input('Would you like to enter another set of files? Y/N\n').upper()
                            if user_input == 'done' or user_input == 'N':
                                print('Exiting program...')
                                exit(0)
                        except IOError:
                            print('Unfortunately, that file could not be found.')

            except IOError:
                print('Unfortunately, that file could not be found.')
                user_input = input("Please enter the streaming service creation file (or 'done' to exit):\n")
                if user_input == 'done' or user_input == 'N':
                    print('Exiting program...')
                    exit(0)
                else:
                    continue


main()
