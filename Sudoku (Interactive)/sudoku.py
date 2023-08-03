print("\nWelcome to Sudoku!!!")


def rules():
    print(
        """\nRules :
--> Each row should have unique numbers
--> Each column should have unique numbers
--> Each 3x3 box should have unique numbers

Guide :
==> To UNDO a move, please type "undo" when asked to enter a number
==> To SHOW the board, please type "show" or "display" when asked to enter a number
==> To seek HELP, type "help" when asked to enter a number
==> To QUIT, type "quit" when asked to enter a number"""
    )


rules()


##############################################################################################################################################


def QuestionWriter():  # WRITES THE QUESTIONS INTO THE NOTEPAD
    q1 = """     1   2   3    4   5   6    7   8   9
  =========================================
A ||   |   |   || 4 |   | 5 ||   |   |   ||
  ||---|---|---||---|---|---||---|---|---||
B ||   |   | 9 ||   | 6 |   ||   | 8 |   ||
  ||---|---|---||---|---|---||---|---|---||
C || 5 |   |   ||   |   | 8 ||   | 7 | 4 ||
  ++===+===+===++===+===+===++===+===+===++
D ||   |   |   || 3 | 9 | 6 || 2 |   |   ||
  ||---|---|---||---|---|---||---|---|---||
E ||   | 3 | 2 || 1 |   | 7 || 4 |   | 6 ||
  ||---|---|---||---|---|---||---|---|---||
F || 1 |   | 6 ||   | 8 | 4 ||   |   |   ||
  ++===+===+===++===+===+===++===+===+===++
G ||   | 8 |   ||   | 7 | 2 || 5 | 3 | 1 ||
  ||---|---|---||---|---|---||---|---|---||
H ||   | 5 | 7 ||   | 3 |   ||   | 4 |   ||
  ||---|---|---||---|---|---||---|---|---||
I || 6 |   | 3 || 5 | 4 |   ||   | 2 |   ||
  ========================================="""

    q2 = """     1   2   3    4   5   6    7   8   9
  =========================================
A || 1 | 5 | 7 ||   | 3 | 2 ||   |   |   ||
  ||---|---|---||---|---|---||---|---|---||
B ||   | 9 |   ||   | 4 |   || 1 | 2 |   ||
  ||---|---|---||---|---|---||---|---|---||
C ||   |   | 4 ||   | 9 | 6 ||   |   |   ||
  ++===+===+===++===+===+===++===+===+===++
D ||   | 1 | 5 ||   | 7 |   || 6 |   |   ||
  ||---|---|---||---|---|---||---|---|---||
E || 7 |   |   ||   |   |   || 8 |   | 5 ||
  ||---|---|---||---|---|---||---|---|---||
F ||   | 2 |   ||   |   |   ||   |   |   ||
  ++===+===+===++===+===+===++===+===+===++
G || 6 |   | 2 || 9 |   |   || 3 |   |   ||
  ||---|---|---||---|---|---||---|---|---||
H ||   | 3 | 1 || 2 | 5 |   || 4 |   | 9 ||
  ||---|---|---||---|---|---||---|---|---||
I ||   |   |   ||   |   |   ||   |   |   ||
  ========================================="""

    q3 = """     1   2   3    4   5   6    7   8   9
  =========================================
A || 5 | 6 |   ||   |   |   ||   |   | 1 ||
  ||---|---|---||---|---|---||---|---|---||
B ||   |   |   ||   | 5 |   ||   | 6 |   ||
  ||---|---|---||---|---|---||---|---|---||
C ||   |   | 7 || 8 | 3 |   || 4 |   |   ||
  ++===+===+===++===+===+===++===+===+===++
D ||   |   | 5 || 3 |   | 1 ||   |   |   ||
  ||---|---|---||---|---|---||---|---|---||
E || 7 |   |   ||   |   |   || 2 |   | 6 ||
  ||---|---|---||---|---|---||---|---|---||
F || 2 |   |   ||   |   | 7 ||   | 5 |   ||
  ++===+===+===++===+===+===++===+===+===++
G ||   |   |   ||   |   |   || 5 | 3 |   ||
  ||---|---|---||---|---|---||---|---|---||
H ||   | 5 | 1 || 4 |   |   ||   |   |   ||
  ||---|---|---||---|---|---||---|---|---||
I || 4 |   |   ||   |   | 2 ||   |   |   ||
  ========================================="""

    f = open("Questions.txt", "w")
    f.seek(0, 0)
    f.write(q1)
    f.write(".\n")
    f.write(q2)
    f.write(".\n")
    f.write(q3)


##############################################################################################################################################


def QuestionReader():  # READS THE QUESTIONS FROM THE NOTEPAD FILE AND STORES THE NUMBERS
    # GIVEN IN THE QUESTION ALONG WITH THEIR POSITION IN THE SUDOKU IN
    f = open(
        "Questions.txt", "r"
    )  # THE LISTS 'row', 'column' and 'box'. THIS IS TO ENSURE THAT USER
    f.seek(0, 0)  # CANNOT ENTER THE SAME NUMBER IN A PARTICULAR ROW, COLUMN OR BOX.
    k = f.read()
    for i in range(len(k)):
        if k[i] == ".":
            q1 = k[:i]
            temp = 2 * i + 2
            q2 = k[i + 2 : temp]
            q3 = k[temp + 2 :]
            break

    global Q_No
    Q_No = 0
    while Q_No not in ["1", "2", "3"]:
        print("-" * 75)
        print("\nEASY(1)                    MEDIUM(2)                    HARD(3)")
        Q_No = input("\nChoose difficulty level: ")
        if Q_No == "1":
            q = q1
        elif Q_No == "2":
            q = q2
        elif Q_No == "3":
            q = q3
        else:
            print("\nEnter valid number")
    print("-" * 75)

    global sudoku
    sudoku = """     1   2   3    4   5   6    7   8   9
  =========================================
A || A1| A2| A3|| A4| A5| A6|| A7| A8| A9||
  ||---|---|---||---|---|---||---|---|---||
B || B1| B2| B3|| B4| B5| B6|| B7| B8| B9||
  ||---|---|---||---|---|---||---|---|---||
C || C1| C2| C3|| C4| C5| C6|| C7| C8| C9||
  ++===+===+===++===+===+===++===+===+===++
D || D1| D2| D3|| D4| D5| D6|| D7| D8| D9||
  ||---|---|---||---|---|---||---|---|---||
E || E1| E2| E3|| E4| E5| E6|| E7| E8| E9||
  ||---|---|---||---|---|---||---|---|---||
F || F1| F2| F3|| F4| F5| F6|| F7| F8| F9||
  ++===+===+===++===+===+===++===+===+===++
G || G1| G2| G3|| G4| G5| G6|| G7| G8| G9||
  ||---|---|---||---|---|---||---|---|---||
H || H1| H2| H3|| H4| H5| H6|| H7| H8| H9||
  ||---|---|---||---|---|---||---|---|---||
I || I1| I2| I3|| I4| I5| I6|| I7| I8| I9||
  ========================================="""

    global row
    global column
    global box
    row = []
    column = []
    box = []
    for i in range(len(q)):
        if q[i] in "123456789":
            if sudoku[i - 2] == sudoku[i + 2] == "|":
                a = [str(sudoku[i].upper()), q[i]]
                b = [str(sudoku[i + 1].upper()), q[i]]
                if str(sudoku[i].upper()) in "ABC":
                    if str(sudoku[i + 1]) in "123":
                        c = ["BOX1", q[i]]
                    elif str(sudoku[i + 1]) in "456":
                        c = ["BOX2", q[i]]
                    elif str(sudoku[i + 1]) in "789":
                        c = ["BOX3", q[i]]
                if str(sudoku[i].upper()) in "DEF":
                    if str(sudoku[i + 1]) in "123":
                        c = ["BOX4", q[i]]
                    elif str(sudoku[i + 1]) in "456":
                        c = ["BOX5", q[i]]
                    elif str(sudoku[i + 1]) in "789":
                        c = ["BOX6", q[i]]
                if str(sudoku[i].upper()) in "GHI":
                    if str(sudoku[i + 1]) in "123":
                        c = ["BOX7", q[i]]
                    elif str(sudoku[i + 1]) in "456":
                        c = ["BOX8", q[i]]
                    elif str(sudoku[i + 1]) in "789":
                        c = ["BOX9", q[i]]
                row.append(a)
                column.append(b)
                box.append(c)
                sudoku = sudoku.replace(str(sudoku[i] + sudoku[i + 1]), (q[i] + " "))


##############################################################################################################################################


def AnswerWriter():
    ans1 = """     1   2   3    4   5   6    7   8   9
  =========================================
A || 3 | 7 | 8 || 4 | 1 | 5 || 9 | 6 | 2 ||
  ||---|---|---||---|---|---||---|---|---||
B || 4 | 2 | 9 || 7 | 6 | 3 || 1 | 8 | 5 ||
  ||---|---|---||---|---|---||---|---|---||
C || 5 | 6 | 1 || 9 | 2 | 8 || 3 | 7 | 4 ||
  ++===+===+===++===+===+===++===+===+===++
D || 7 | 4 | 5 || 3 | 9 | 6 || 2 | 1 | 8 ||
  ||---|---|---||---|---|---||---|---|---||
E || 8 | 3 | 2 || 1 | 5 | 7 || 4 | 9 | 6 ||
  ||---|---|---||---|---|---||---|---|---||
F || 1 | 9 | 6 || 2 | 8 | 4 || 7 | 5 | 3 ||
  ++===+===+===++===+===+===++===+===+===++
G || 9 | 8 | 4 || 6 | 7 | 2 || 5 | 3 | 1 ||
  ||---|---|---||---|---|---||---|---|---||
H || 2 | 5 | 7 || 8 | 3 | 1 || 6 | 4 | 9 ||
  ||---|---|---||---|---|---||---|---|---||
I || 6 | 1 | 3 || 5 | 4 | 9 || 8 | 2 | 7 ||
  ========================================="""

    ans2 = """     1   2   3    4   5   6    7   8   9
  =========================================
A || 1 | 5 | 7 || 8 | 3 | 2 || 9 | 4 | 6 ||
  ||---|---|---||---|---|---||---|---|---||
B || 3 | 9 | 6 || 7 | 4 | 5 || 1 | 2 | 8 ||
  ||---|---|---||---|---|---||---|---|---||
C || 2 | 8 | 4 || 1 | 9 | 6 || 5 | 7 | 3 ||
  ++===+===+===++===+===+===++===+===+===++
D || 4 | 1 | 5 || 3 | 7 | 8 || 6 | 9 | 2 ||
  ||---|---|---||---|---|---||---|---|---||
E || 7 | 6 | 3 || 4 | 2 | 9 || 8 | 1 | 5 ||
  ||---|---|---||---|---|---||---|---|---||
F || 9 | 2 | 8 || 5 | 6 | 1 || 7 | 3 | 4 ||
  ++===+===+===++===+===+===++===+===+===++
G || 6 | 7 | 2 || 9 | 8 | 4 || 3 | 5 | 1 ||
  ||---|---|---||---|---|---||---|---|---||
H || 8 | 3 | 1 || 2 | 5 | 7 || 4 | 6 | 9 ||
  ||---|---|---||---|---|---||---|---|---||
I || 5 | 4 | 9 || 6 | 1 | 3 || 2 | 8 | 7 ||
  ========================================="""

    ans3 = """     1   2   3    4   5   6    7   8   9
  =========================================
A || 5 | 6 | 8 || 2 | 7 | 4 || 3 | 9 | 1 ||
  ||---|---|---||---|---|---||---|---|---||
B || 3 | 4 | 2 || 1 | 5 | 9 || 7 | 6 | 8 ||
  ||---|---|---||---|---|---||---|---|---||
C || 1 | 9 | 7 || 8 | 3 | 6 || 4 | 2 | 5 ||
  ++===+===+===++===+===+===++===+===+===++
D || 6 | 8 | 5 || 3 | 2 | 1 || 9 | 4 | 7 ||
  ||---|---|---||---|---|---||---|---|---||
E || 7 | 3 | 4 || 9 | 8 | 5 || 2 | 1 | 6 ||
  ||---|---|---||---|---|---||---|---|---||
F || 2 | 1 | 9 || 6 | 4 | 7 || 8 | 5 | 3 ||
  ++===+===+===++===+===+===++===+===+===++
G || 9 | 2 | 6 || 7 | 1 | 8 || 5 | 3 | 4 ||
  ||---|---|---||---|---|---||---|---|---||
H || 8 | 5 | 1 || 4 | 9 | 3 || 6 | 7 | 2 ||
  ||---|---|---||---|---|---||---|---|---||
I || 4 | 7 | 3 || 5 | 6 | 2 || 1 | 8 | 9 ||
  ========================================="""

    f = open("Answers.txt", "w")
    f.seek(0, 0)
    f.write(ans1)
    f.write(".\n")
    f.write(ans2)
    f.write(".\n")
    f.write(ans3)


##############################################################################################################################################


def AnswerReader():
    f = open("Answers.txt", "r")
    f.seek(0, 0)
    k = f.read()
    for i in range(len(k)):
        if k[i] == ".":
            ans1 = k[:i]
            temp = 2 * i + 2
            ans2 = k[i + 2 : temp]
            ans3 = k[temp + 2 :]
            break
    global ans
    if Q_No == "1":
        ans = ans1
    elif Q_No == "2":
        ans = ans2
    elif Q_No == "3":
        ans = ans3


##############################################################################################################################################


def display(x):  # DISPLAYS THE SUDOKU WITHOUT THE COORDINATES
    sudoku_display = ""  # (A1,A2,A3,B1,B2,B3,ETC.)
    g = 0
    while g < len(x):
        if x[g] in "ABCDEFGHI" and x[g + 1] in "123456789":
            sudoku_display += "  "
            g += 2
        else:
            sudoku_display += x[g]
            g += 1
    print("\n", sudoku_display)


##############################################################################################################################################


QuestionWriter()  # CALLS THE FUNCTIONS
QuestionReader()
AnswerWriter()
AnswerReader()
display(sudoku)


###############################################################################################################################################


sudoku_update = sudoku

turn = 0
Quit = 0
undocount = 0
second_break = 0
while (
    sudoku_update != ans or Quit == 1
):  # ALLOWS USER TO ENTER NUMBERS ACCORDING TO SUDOKU RULES
    error1 = 0
    error2 = 0
    while error1 == 0:
        print("-" * 75)
        number = input("\nEnter number: ")
        if len(number) == 0:
            pass
        elif number.upper() in ["SHOW!", "SHOW", "DISPLAY!", "DISPLAY"]:
            display(sudoku_update)
        elif number.upper() in ["HELP!", "HELP"]:
            rules()
        elif number.upper() in ["QUIT!", "QUIT"]:
            second_break = 1
            break
        elif number.upper() in ["UNDO!", "UNDO"]:  # ALLOWS USER TO UNDO A MOVE
            if turn != undocount:  # TO UNDO A MOVE TYPE "UNDO" WHEN ASKED TO ENTER
                n = row[-1][1]  # A NUMBER (NOT CASE SENSITIVE)
                r = row[-1][0]
                c = column[-1][0]
                pos = " " + str(r) + str(c)
                linenumber = 1 + (2 * (ord(r) - 64))
                line = sudoku_update.split("\n")[linenumber - 1]
                linecopy = line
                line = line.replace(" " + str(n) + " ", pos)
                sudoku_update = sudoku_update.replace(str(linecopy), str(line))
                row.pop()
                column.pop()
                box.pop()
                undocount += 1
                display(sudoku_update)
                print("\nMove undone!")
            elif turn == 0:
                print("\nPlease play a move first!")
            elif turn == undocount:
                print("\nCannot undo further!")
        elif number not in "123456789" or len(number) != 1:
            print("\nEnter a number from 1-9!")
        else:
            error1 += 1
    if second_break == 1:
        break

    while error2 == 0:
        print("-" * 75)
        position_input = input("\nEnter position (row,column) : ")
        if len(position_input) == 0:
            pass
        if len(position_input) != 2:
            print(
                "\nEnter a valid position specifying the Row(R) and Column(C) as RC \nex: G4 for Row G and Column 4"
            )
        elif (
            position_input[0] not in "abcdefghiABCDEFGHI"
            or position_input[1] not in "123456789"
        ):
            print(
                "\nEnter a valid position specifying the Row(R) and Column(C) as RC \nex: G4 for Row G and Column 4"
            )
        else:
            position = str(str(position_input[0]) + str(position_input[1]))
            error2 += 1
            print("-" * 75)

    a = [str(position[0].upper()), str(number)]
    b = [str(position[1].upper()), str(number)]
    if str(position[0].upper()) in "ABC":
        if str(position[1]) in "123":
            c = ["BOX1", number]
        elif str(position[1]) in "456":
            c = ["BOX2", number]
        elif str(position[1]) in "789":
            c = ["BOX3", number]
    if str(position[0].upper()) in "DEF":
        if str(position[1]) in "123":
            c = ["BOX4", number]
        elif str(position[1]) in "456":
            c = ["BOX5", number]
        elif str(position[1]) in "789":
            c = ["BOX6", number]
    if str(position[0].upper()) in "GHI":
        if str(position[1]) in "123":
            c = ["BOX7", number]
        elif str(position[1]) in "456":
            c = ["BOX8", number]
        elif str(position[1]) in "789":
            c = ["BOX9", number]

    if a not in row and b not in column and c not in box:
        row.append(a)
        column.append(b)
        box.append(c)
        sudoku_update = sudoku_update.replace(
            str(position.upper()), str(str(number) + " ")
        )
        turn += 1
        display(sudoku_update)
    else:
        print("\nInvalid!")

else:
    print("\nCongrats!!!\nSudoku Solved")


##############################################################################################################################################
