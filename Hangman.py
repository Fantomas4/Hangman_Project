############################################################################################################test
def server_func():

    #thread gia server_win_check_func
    from threading import Thread

    server_thread = Thread(target=server_win_check_func)
    server_thread.start()



    import socket

    HOST = socket.gethostname()
    print("DIAG: gethostname(): ", socket.gethostname(),file=sys.stderr)
    PORT = 9999

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(5)
    print('Serving HTTP on port %s ...' % PORT,file=sys.stderr)

    target_word = random.choice(word_list)

    while True:
        client_connection, client_address = listen_socket.accept()
        print("Got a connection from %s" % str(client_address),file=sys.stderr)
        request = client_connection.recv(1024)
        print("Server got the request: ",request.decode('ascii'),file=sys.stderr)

        if request.decode('ascii') == "word":
            print("DIAG: Server shares word with client!",file=sys.stderr)

            print("DIAG: SERVER WORD: ", target_word,file=sys.stderr)
            client_connection.send(target_word.encode("ascii"))


            # client_connection.close()


############################################################################################################
def client_func():


    import socket
    # create a socket object

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 9999
    # connection to hostname on the port.
    s.connect((host, port))

    send_msg = "word"
    s.send(send_msg.encode("ascii"))

    # Receive no more than 1024 bytes
    received_msg = s.recv(1024)
    #print(received_msg.decode("ascii"))
    s.close()
    target_word = received_msg.decode("ascii")
    menu_choice = main_game_func(6,settings,target_word)

    return menu_choice
############################################################################################################
def server_win_check_func():


    import socket

    win_status = False  # no client has won yet

    HOST = socket.gethostname()
    print("DIAG: gethostname(): ", socket.gethostname(),file=sys.stderr)
    PORT = 9998

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(5)
    print('Serving WIN HTTP on port %s ...' % PORT,file=sys.stderr)

    while True:
        client_connection, client_address = listen_socket.accept()
        print("WIN_SERVER got a WIN connection from %s" % str(client_address),file=sys.stderr)
        request = client_connection.recv(1024)
        request = request.decode('ascii')
        print("Server got the WIN request: ", request,file=sys.stderr)
        if request == "win_status":
            if win_status == True:
                client_connection.send("end_game".encode('ascii'))
            elif win_status == False:
                client_connection.send("pending_game".encode('ascii'))
        elif request == "win":
            win_status = True

############################################################################################################
def client_win_check_func():

    import socket
    # create a socket object

    win_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 9998
    # connection to hostname on the port.
    win_socket.connect((host, port))

    send_msg = "win_status"
    win_socket.send(send_msg.encode('ascii'))
    received_msg = win_socket.recv(1024)

    received_msg = received_msg.decode("ascii")
    print("Client got answer from server: ", received_msg,file=sys.stderr)

    win_socket.close()

    return received_msg
############################################################################################################
hangman_art=[]
for i in range(0,7):
    hangman_art.append("_EMPTY_")

hangman_art[0]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /
| |
| |
| |
| |
============================
"""

hangman_art[1]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |
| |
| |
| |
| |
============================
"""

hangman_art[2]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |          -`--'
| |          |. .|
| |          |   |
| |          | . |
| |          |   |
| |            -
| |
| |
| |
| |
============================
"""

hangman_art[3]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'
| |        /Y . .
| |       // |   |
| |      //  | . |
| |     ')   |   |
| |            -
| |
| |
| |
| |
============================
"""

hangman_art[4]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |            -
| |
| |
| |
| |
============================
"""

hangman_art[5] = """
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||-
| |          ||
| |          ||
| |          ||
| |         / |
============================
"""
hangman_art[6]="""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||-||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
============================
"""
###############################################################################################


class login_data(object):

    users_index = 0
    login = "guest"



################################################################################################


def user_func(users):
    print("1. Register new user.")
    print("2. Existing user.")
    choice = input("Enter your choice: ")
    choice = choice_check(choice,1,2)

    if choice == 1:
        print("DIAG: List in func before entry is: ",users)
        name = input("Please enter a username: ")

        while name in users:
            print("  *** ERROR: User name alredy exists ***")
            name=input("  *** Please enter a different username: ")
        login_data.users_index += 1

        print("DIAG: USER_INDEX is: ",login_data.users_index)
        login_data.login = name
        print("DIAG: name is:",name)
        users.append(name)
        print("DIAG: MPIKA SINARTISI USER_FUNC/APPEND NAME")
    elif choice == 2:
        name = input("Please enter your username: ")
        if name in users:
            print("Diagnostics: USER FOUND!")
            login_data.login = name

    return



#################################################################
def main_game_func(menu_choice,settings,target):


    char_found = 0
    word_print = []
    wrong_used_char = []
    total_used_char = []
    gu_left = 6
    match_found = False

    ###multi_end_game = False #flag gia ton termatismo toy paixnidioy otan dothei sima nikis gia kapoion client

    if menu_choice ==5 or menu_choice == 6 : #multiplayer mode
        multiplayer = 1
    else:
        multiplayer = 0           #single player mode

        ### multiplayer == 2 --->stop game!


    print("Diagnostics: Target word is:", target)
    target_len = len(target)
    # print("Diagnostics: Target length is:", target_len)

    for i in range(0, target_len):
        word_print.append("_")

    if settings[0] == "True":  ##Ginetai pros apofigi BUG otan dinw to prwto gramma.
        for i in range(0,target_len):  # Emfanizw se oles tis theseis tis lexis ta grammata poy einai idia me to proto gramma.
            if target[0] == target[i]:
                total_used_char.append(target[0])
                word_print[i] = target[0]
                char_found += 1

    ##### MAIN GAME ######
    while gu_left > 0 and char_found < target_len and multiplayer != 2:

        print(hangman_art[6 - gu_left])

        for i in range(0, target_len):
            print(word_print[i], end=" ")  # Prints on the same line
        print("\n")

        if wrong_used_char:  # checks if list is NOT empty
            print(wrong_used_char)

        print("You have", gu_left, "guesses left.")


        #####################  SINGLEPLAYER  ################################

        # if menu_choice != 5 and menu_choice != 6:
        #     import multiprocessing
        #     char_queue = multiprocessing.Queue(maxsize=5)  # ftiaxnw oura
        #
        # #h eisagogi xaraktira ginetai me parallili epexergasia me thread oste na mporoyn
        # # na prosthethoyn mellontika
        # #leitoyrgies opos px xronometrisi kai time limit.
        #
        # create_process = True  # flag gia na xekinisei process MONO stin proti ektelesi tis loopas
        # import time  # TEMPORARY?
        # while True:
        #     if create_process == True:
        #         ##to bug poy emfanizei pali to menu prokaleitai kapws edw!
        #         print("DIAG: Initializing char_entry_func parallel process!...")
        #
        #         from threading import Thread
        #         char_input_thread = Thread(target=char_entry_func, args=(char_queue, total_used_char))
        #         char_input_thread.start()
        #
        #         create_process = False
        #
        #     if not char_queue.empty():
        #         # char_input_thread.exit()
        #         print("EFTASA 4")
        #         print("H OYRA EXEI XARAKTIRA STI LOOPA")
        #         given_char = char_queue.get()  ##pairnw ton char poy edwse o user
        #         break

        #####################  MULTIPLAYER  ################################


        if menu_choice == 5 or menu_choice == 6:
            import multiprocessing
            char_queue =multiprocessing.Queue(maxsize=5) #ftiaxnw oura

        create_process = True #flag gia na xekinisei process MONO stin proti ektelesi tis loopas
        import time #TEMPORARY?

        #######################################################################################################
        while True:

            import sys

            if create_process == True:
                ##to bug poy emfanizei pali to menu prokaleitai kapws edw!
                print("DIAG: Initializing char_entry_func parallel process!...")

                # from threading import Thread
                # char_input_thread = Thread(target=char_entry_func, args=(char_queue,total_used_char))
                # char_input_thread.start()
                import sys
                fn = sys.stdin.fileno()  # get original file descriptor
                print("DIAG: fn is: ",fn)
                import multiprocessing
                char_input_process = multiprocessing.Process(target=char_entry_func, args=(char_queue,total_used_char,fn))
                char_input_process.start()

                create_process = False

            ## elegxw gia niki apo allon client
            received_msg = client_win_check_func()
            if received_msg == "end_game":
                print("EFTASA 3")
                print("DIAG: end_game STI LOOPA")
                multiplayer = 2 #stop game
                char_input_process.terminate()
                break

            if not char_queue.empty():
                #char_input_thread.exit()
                print("EFTASA 4")
                print("H OYRA EXEI XARAKTIRA STI LOOPA")
                given_char = char_queue.get()  ##pairnw ton char poy edwse o user
                char_input_process.terminate()
                break
            time.sleep(1)

        ####################################################################################################

        if multiplayer != 2: #multiplayer == 2 --->stop game!
            total_used_char.append(given_char)
            for i in range(0, target_len):
                if target[i] == given_char:
                    match_found = True
                    char_found += 1
                    word_print[i] = given_char

            if match_found == False:
                print("\n\nWrong guess!")
                wrong_used_char.append(given_char)
                gu_left = gu_left - 1

            match_found = False
            print("\n")
        else:
            print("*** GAME OVER! Another Client has already won! ***\n\n")

    ###################################################

    if char_found != target_len and multiplayer != 2:
        print("You are out of guesses!")
        print("The word was:", target)
        print("   *** GAME OVER ***")
    elif char_found == target_len:
        for i in range(0, target_len):
            print(word_print[i], end=" ")  # Prints on the same line
        print("\n")
        print("Congratulations! YOU HAVE WON !")



        if menu_choice == 5 or menu_choice == 6:
            ##STELNW SIMA NIKIS STON SERVER
            import socket
            # create a socket object

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # get local machine name
            host = socket.gethostname()
            port = 9998
            # connection to hostname on the port.
            s.connect((host, port))

            send_msg = "win"
            s.send(send_msg.encode("ascii"))





    #score = score_func(settings, target_len, gu_left)
    #print("Your score is:", score)
    #print("Would you like to save your score?")
    print("Would you like to start a new game?")
    choice = input("Please enter Yes or No: ")
    while choice != "Yes" and choice != "No":
        print("Wrong entry!")
        choice = input("Please enter Yes or No:")

    if choice == "No":
        print("DIAG mpika sto NO2")
        print("\n\n\n\n\n\n\n\n")
        print("DIAG: welcome_func apo to simeio 3!")


        menu_choice = welcome_func(login_data.login)
        return menu_choice


###############################################################################################


def score_func(settings, target_len, gu_left):

    if settings[0] == False:
        points = 50
    else:
        points = 0

    points = points + gu_left *100

    if settings[1] == "1.txt":
        points = points*1
    elif settings[1] == "2.txt":
        points = points*2
    elif settings[1] == "3.txt":
        points = points*3

    points = points + 20 * target_len

    return points
###########################################################################################


def choice_check(choice,min,max):

    while True:

        try:                                         #
            choice= int(choice)                      # checks if the user input
            #print("DIAGNOSTICS: INPUT IS int")      # is an integer or not.
            integer=True                             #
        except ValueError:                           #
            #print("DIAGNOSTICS: INPUT IS not int")  #
            integer=False

        if integer==True:
            if choice<min or choice>max:
                in_range=False
            else:
                in_range=True


        if integer==True and in_range==True:
            return choice
        else:
            if integer==False:
                print("Wrong entry! Please enter an integer choice.")
            elif in_range==False:
                print("Wrong entry! Please select one of the given options.")

            choice = input("Please enter your choice: ")

###################################################################################
def char_entry_func(char_queue,total_used_char,fn): #MULTIPLAYER##
    import sys
    import os
    sys.stdin = os.fdopen(fn)  # open stdin in this process
    print("DIAG: multiplayer char_entry_func!!!!!!!!")

    choice = input("Please enter a single character as your guess: ")
    print("\n\n")  ## TEMPORARY
    choice = choice.upper()
    choice = entry_check(choice, total_used_char)
    char_queue.put(choice)

    #import sys

    # read = sys.stdin.read(1)
    # print("DIAG: read is: ",read)

    # print("DIAG MPIKA")
    # print(sys.stdin.read(2) != " ")
    # char_queue.put(sys.stdin.read(1))


    return



###################################################################################
def entry_check(choice, total_used_char):

    verified=False

    while verified==False:

        try:                                        #
            choice= int(choice)                     # checks if the user input
            #print("DIAGNOSTICS: INPUT IS not str")  #is a string or not. This prevents
            string=False                            #
        except ValueError:                          #the user from entering a number
            #print("DIAGNOSTICS: INPUT IS str")      #
            string=True                             #

        if string==True:
            if len(choice)>1:
                single=False
            else:
                single=True

            if choice in total_used_char:
                unique=False
            else:
                unique=True

            if choice.isalpha():
                letter=True
            else:
                letter=False

        if string==True and single==True and unique==True and letter==True:
            verified=True
            return choice
        else:
            if string==False:
                print("Wrong entry! Please enter a character as input.")
            elif single==False:
                print("Wrong entry! Please enter a single character as input.")
            elif unique==False:
                print("Wrong entry! You have entered this character during a previous guess.")
            elif letter==False:
                print("Wrong entry! Please enter an alphabetic letter.")

            choice=input("Please enter your guess: ")
            choice=choice.upper()


############################################################################################
def test_func():
    print("%%%%TEST TEST TEST TEST TEST%%%%%%")

###############

def status(setting,opt_choice):

    if opt_choice == 2:
        print("Setting is currently set to: ", setting)
    elif opt_choice == 1:
        if setting == "1.txt":
            setting = "Easy"
        elif setting == "2.txt":
            setting = "Medium"
        elif setting == "3.txt":
            setting = "Hard"

        print("Setting is currently set to: ", setting)
    choice=input("Enter the new status of the setting: ")

    if opt_choice==1:
        while choice != "Easy" and choice != "Medium" and choice != "Hard":
            print("Wrong entry!")
            choice = input("Please enter Easy, Medium or Hard as status: ")
        if choice == "Easy":
              return "1.txt"
        elif choice == "Medium":
               return "2.txt"
        elif choice == "Hard":
               return "3.txt"
    elif opt_choice == 2:
        while choice!="True" and choice!="False":
            print("Wrong entry!")
            choice=input("Please enter True or False as status: ")
        return choice

#########################################################################################


def options_func(settings):

    print("   **** OPTIONS ****")
    print("==> 0. Exit to the main menu.")
    print("==> 1. Choose the level of difficulty.")
    print("==> 2. Print the first letter of the word as a hint.")
    choice = input("Enter your choice: ")
    opt_choice = choice_check(choice, 0, 2)
    if opt_choice == 0:
        return True
    elif opt_choice == 1:
        settings[1] = status(settings[1],opt_choice)
    elif opt_choice == 2:
        settings[0] = status(settings[0],opt_choice)  # The "status" function changes the
    return False                           # the condition of a particular option.

######################################################################################


def welcome_func(login):

    print("     **** Welcome to the Hangman Application ****")
    print("1.Login as a user")
    print("2.Start a new game as", login)
    print("3.Enter the options submenu.")
    print("4.Exit the application.")
    print("5.Host a multiplayer session (BETA!)")
    print("6.Join a multiplayer session (ALPHA!)")

    choice = input("Enter your choice: ")
    menu_choice = choice_check(choice, 1, 6)
    return menu_choice
#############################################################################################################

if __name__ == '__main__':

    import random
    import sys #used for try/except block
    import os.path #used for os.path.isfile() ==> checks if file exists in directory

    users = []
    settings = []


    set_index = 2 #settings index

    ### CHECKS IF THE settings.txt file exists ###
    if os.path.isfile("settings.txt"):
        print("SETTINGS FILE EXISTS")
        with open('settings.txt', 'r') as saved_set:
            settings = saved_set.read().splitlines()
    else:
        print("SETTINGS FILE DOES NOT EXIST.")
        with open('settings.txt', 'w') as saved_set:
            saved_set.write("True")
            saved_set.write("\n")
            saved_set.write("1.txt")

        with open('settings.txt', 'r') as saved_set:
            settings = saved_set.read().splitlines()

    ### CHECKS IF THE users.txt file exists ###
    if os.path.isfile("users.txt"):
        print("USERS FILE EXISTS")
        with open('users.txt', 'r') as saved_users:
            users = saved_users.read().splitlines()
    else:
        print("USERS FILE DOES NOT EXIST.")  ##Mono entos tou with open einai anoixto to  arxeio






    print("Diagnostics: settings0: ",settings[0])
    print("Diagnostics: settings1: ",settings[1])
    with open(settings[1],'r') as dictionary: #settings[1] contains the file name (name.txt)
        word_list = dictionary.read().upper().splitlines()

    login = "guest"
    print("DIAG: welcome_func apo to simeio 1!")

    menu_choice=welcome_func(login_data.login)

    while menu_choice != 4: ## Condition depends on amount of choices. Currently set to 4
        ##termination condition

        if menu_choice == 1:
            user_func(users)
            with open('users.txt', 'w') as saved_users:  ### SAVES USERS TO TEXT FILE!
                for i in range(0,login_data.users_index):
                    print("DIAG: LOOP TYPOSIS SE ARXEIO")
                    print("DIAG: users",users)
                    print("DIAG: users[i]",users[i])
                    saved_users.write(users[i])
                    saved_users.write("\n")


            print("DIAG: welcome_func apo to simeio 4!")


            menu_choice = welcome_func(login_data.login)


        if menu_choice == 3:
            print("DIAGNOSTICS: settings[0]: ",settings[0])
            exit_loop = False
            while exit_loop != True:
                exit_loop = options_func(settings)
            print("DIAG: welcome_func apo to simeio 2!")


            menu_choice = welcome_func(login_data.login)
            with open('settings.txt', 'w') as saved_set:  ### SAVES SETTINGS TO TEXT FILE!
                for i in range(0,set_index):
                    saved_set.write(settings[i])
                    saved_set.write("\n")



        while menu_choice==2:  ### FOR MENU
            target_word = random.choice(word_list)
            menu_choice =main_game_func(2,settings,target_word)
            print("\n\n\n\n\n\n\n\n")

        if menu_choice == 5:  ##host server
            #ektelei to arxeio toy server

            from threading import Thread

            server_thread = Thread(target=server_func)
            server_thread.start()
            print("DIAG: Initializing server thread...",file=sys.stderr)
            menu_choice=client_func()



        if menu_choice == 6:  ##join server
            menu_choice = client_func()






