def Credit_Validation(pCredits):
    '''
    Validates user input credits
    '''
    while(True):
        try:
            credits = int(input(f'Please enter your {pCredits}'))
            if credits in range(0, 121, 20): #check whether credits are in the right range
                break
            else:
                print('    Credits are out of range!!')

        except ValueError:
            print('    Integer required please try again!!')
    return credits
progress_list = []   #Global variables
progress = 0
module_tralier = 0
module_retriever = 0
exclude = 0
def Progress_Outcome(pPass_credits, pDefer_credits, pFail_credits):
    '''
    Calculates and displays the progress outcome
    '''
    global progress, module_tralier,module_retriever,exclude, progress_list
    if pPass_credits == 120:
        progress += 1
        print('Progress')
        temp_list = [f"Progress - {pPass_credits}, {pDefer_credits}, {pFail_credits}"]
        progress_list.append(temp_list) #appending the temporary list to the main list
    elif pPass_credits == 100:
        module_tralier += 1
        print('Progress (module trailer)')
        temp_list = [f"Progress (module trailer) - {pPass_credits}, {pDefer_credits}, {pFail_credits}"]
        progress_list.append(temp_list)
    else:
        if pFail_credits >= 80:
            exclude += 1
            print('Exclude')
            temp_list = [f"Exclude - {pPass_credits}, {pDefer_credits}, {pFail_credits}"]
            progress_list.append(temp_list)
        else:
            module_retriever += 1
            print('module retriever')
            temp_list = [f"module retriever - {pPass_credits}, {pDefer_credits}, {pFail_credits}"]
            progress_list.append(temp_list)

def Stu_Version():
    '''
    Asks for credits, validates the credits and displays the progress outcome to the students
    '''
    while True:
        pass_credits = Credit_Validation('credits at pass: ')
        defer_credits = Credit_Validation('credits at defer: ')
        fail_credits = Credit_Validation('credits at fail: ')
        credit_total = pass_credits + defer_credits + fail_credits
        if credit_total != 120:
            print('Incorrect total!! Please enter your credits again.')
            continue
        Progress_Outcome(pass_credits, defer_credits, fail_credits)
        break

def Horizontal_Histrogram():
    '''
    Displays a horizontal diagram of progress outcomes of the students to the staff
    '''
    outcome_total = progress + module_tralier + module_retriever + exclude
    print(f"Progress {progress}{': ':>12} {progress * '* '}")
    print(f"Trailer {module_tralier}{': ':>13} {module_tralier * '* '}")
    print(f"Retriever {module_retriever}{': ':>11} {module_retriever * '* '}")
    print(f"Exclude {exclude}{': ':>13} {exclude * '* '}")
    print(outcome_total,'outcomes in total')

def Staff_version():
    '''
    Asks for credits, validates the credits, displays the progress outcome and a horizontal diagram of progress outcomes of the students to the staff
    '''
    staff_input = 'y'
    while True:
        if staff_input == 'y':
            Stu_Version() 
            staff_input = input('Would you like to enter another set of data?\n Enter \'y\' for yes or \'q\' to quit and view results: ').lower()
        elif staff_input == 'q':
            print('___________________________________________________________________________________________________\n Horizontal Diagram')
            Horizontal_Histrogram()
            break
        else:
            print('Invalid option please try again!!')
            staff_input = input('Would you like to enter another set of data?\n Enter \'y\' for yes or \'q\' to quit and view results: ').lower()

def Vertical_Histrogram():
    '''
    Displays a vertical diagram of progress outcomes of the students to the staff
    '''
    global progress, module_tralier, module_retriever, exclude 
    outcome_total = progress + module_tralier + module_retriever + exclude
    print()
    print(f" Progress {progress} | Trailer {module_tralier} | Retriever {module_retriever} | Exclude {exclude} |")
    for x in range(max(progress,module_tralier,module_retriever, exclude)):
        if x < progress:
            print(f"{'*':>5}", end = '')
        else:
            print(f"{' ':>5}", end = '')
            
        if x < module_tralier:
            print(f"{'*':>13}", end = '')
        else:
            print(f"{' ':>13}", end = '')

        if  x < module_retriever:
            print(f"{'*':>13}", end = '')
        else:
            print(f"{' ':>13}", end = '')

        if x < exclude:
            print(f"{'*':>13}")
        else:
            print(f"{' ':>13}")
    print(outcome_total,'outcomes in total')

def Display_List():
    '''
    Displays a list containing credits values and their respective progress outcomes of the students to the staff
    '''
    print('List of progress data are as follows: ')
    for sublist in progress_list:
        print(*sublist)
    print()

def Write_To_File():
    '''
    Writing the list of credits values and their progress outcomes to the progress text file
    '''
    try:
        with open('progress.txt', 'w') as f:
            for sublist in progress_list:
                    f.write(str(*sublist) + '\n')
        print('Data has been written to the file successfully!\n')
    except IOError:
        print('File writing process unsuccessful')

def Read_To_File():
    '''
    Reading and displaying the list of credits values and their progress outcomes from the progress text file
    '''
    try:
        with open('progress.txt', 'r') as f:
            print('Entered progress data to the file are as follows: ')
            lines = f.readlines()
            print('\n',*lines)
    except FileNotFoundError:
        print('file not found!!')
    except IOError:
        print('File reading process unsuccessful')
    
#MAIN CODE
print('_____This program displays the progress outcome of the credits acquired throught the academic year by students._____')
print(' > Enter \'1\' For Part One. \n > Enter \'2\' For Part Two \n > Enter \'3\' For Part Three \n > Enter \'4\' For Part Four')
while(True):
        user_input = input("Please enter your menu option: ")
        if user_input == '1':
                print(' > Enter \'1\' For Student Version. \n > Enter \'2\' For Staff Version. \n ')
                while (True):
                    user_input = input('Please enter your option: ')
                    if user_input == '1':
                        Stu_Version()
                        exit()
                    elif user_input == '2':
                        Staff_version() 
                        exit()
                    else:
                        print('    Invalid menu option please try again')
                        continue
        elif user_input == '2': 
            Staff_version()
            print('\n\n___________________________________________________________________________________________________\n Vertical Diagram')
            Vertical_Histrogram()  
            break
        elif user_input == '3':
            Staff_version()
            print('\n\n___________________________________________________________________________________________________\n Vertical Diagram')
            Vertical_Histrogram()
            Display_List()  
            break
        elif user_input == '4':
            Staff_version()
            print('\n\n___________________________________________________________________________________________________\n Vertical Diagram')
            Vertical_Histrogram()
            Display_List()
            Write_To_File() 
            Read_To_File()  
            break
        else:
            print('    Invalid menu option please try again')





