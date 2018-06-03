# Created by Ethan Katnic, Andrew Mahoney-Fernandes, and Emillie Kuo

GRADEBOOK = {}
FINALSCORES = []

def compute_score(score_list):
    home_work = score_list[0] + score_list[1] + score_list[2]
    tests = score_list[3] + score_list[4]
    hw_score = home_work / 150.  # 150 = total possible hw points
    test_score = tests / 200.  # 200 = total possible test points
    score = (hw_score * .6) + (test_score * .4)  # gets percentage
    score = round(score * 100)  # gets points
    return score


def compute_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    return grade


def process_inputs(user_string):
    input_strings = user_string.split()
    key = input_strings.pop(0)
    scores = list(map(int, input_strings))
    return key, scores


def process_line(userLine):
    key, scores = process_inputs(userLine)  # process input
    final_score = compute_score(scores)  # compute final score
    FINALSCORES.append(final_score) # add final score to global list
    scores.append(final_score) # add final score to current list
    grade = compute_grade(final_score)  # compute final grade
    scores.append(grade)  # add final score and grade to score list
    return key, scores  # return name and scores


def compute_stats(intlist):
    mean = sum(intlist) / len(intlist)
    delta_squares = [ (mean-num) ** 2 for num in intlist]
    variance = sum(delta_squares) / len(delta_squares)
    std_dev = variance ** 0.5
    median = get_median(intlist)
    mode = get_mode(intlist)
    return [round(mean, 2), round(std_dev, 2), median, mode]

def get_median(intlist):
    sortedLst = sorted(intlist)
    length = len(intlist)
    index = (length - 1) // 2
    if (length % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def get_mode(intlist):
    count = {}
    max_count = 0
    for num in intlist:
        count[num] = count.get(num, 0) + 1
    
    for key, value in count.items():
        if value > max_count:
            max_count = value
    
    if max_count == 1:
       return None
    else:
        return max(set(intlist), key=intlist.count)


def search():
    if len(GRADEBOOK) > 0:
        key = input("Enter the name of the student: ")
        if key in GRADEBOOK:
            homework = 'HW1: ' + str(GRADEBOOK[key][0]) + '\n\t HW2: ' +\
                    str(GRADEBOOK[key][1]) + '\n\t HW3: ' + str(GRADEBOOK[key][2])
            tests = 'Exam1: ' + str(GRADEBOOK[key][3]) + '\n\t Exam2: ' + str(GRADEBOOK[key][4])
            grade = 'Score: ' + str(GRADEBOOK[key][5]) + '\n\t Letter: ' + str(GRADEBOOK[key][6])
            print("\nStudent:\n\t", key)
            print("Homework:\n\t", homework)
            print("Tests:\n\t", tests)
            print("Grade:\n\t", grade)
        else:
            print("Student not found.")
    else:
        print('Gradebook is empty. Please read in data.')


def display_data():
    if len(GRADEBOOK) > 0:
        print('\n\033[4mName\t', 'HW1\t', 'HW2\t', 'HW3\t', 'Exam1\t', 'Exam2\t', 'Score\t', 'Grade\033[0m', '\n')
        for student in GRADEBOOK.keys():
            print(student + '\t' + print_list(GRADEBOOK[student], '\t'))
    else:
        print('Gradebook is empty. Please read in data.')

def gradebook_tostring(): 
    output = "" 
    for student in GRADEBOOK.keys():
        output = output + (student + '\t' + print_list(GRADEBOOK[student], '\t'))
    return output

def print_list(string_list, sep):
    strings = []
    for element in string_list:
        strings.append(str(element))
    return sep.join(strings)

def read_data():        
    scores = open('scores.txt', 'r')
    read=scores.readlines() 
    for line in read:
        name, scores=process_line(line) 
        GRADEBOOK[name]=scores 
    print('Read complete.')

def show_menu():
    exit = False
    while not exit:  # same as    quit == False
        print('\n', '1. Read Data  2. Save Data 3. Display Data 4. Display Stats 5.'
              ' Search by Name 6. Enter Data 7. Reset 8. Search by Grade 9. Exit.')
        choice = int(input())
        if choice == 1:
            read_data()
        elif choice == 2:
            save_data()
        elif choice == 3:
            display_data()
        elif choice == 4:
            display_stats()
        elif choice == 5:
            search()
        elif choice == 6:
            enter_data()
        elif choice == 7:
            reset()
        elif choice == 8:
            search_by_grade()
        elif choice == 9:
            exit = True


def save_data():
    if len(GRADEBOOK) > 0:
        text_file=open("grades1.txt","w")
        text_file.writelines(gradebook_tostring())
    else:
        print('Gradebook is empty. Please read in data.')

def display_stats():
    if len(GRADEBOOK) > 0:
        mean, std_dev, median, mode = compute_stats(FINALSCORES)
        print("Final scores:", print_list(FINALSCORES, ', '))
        print("Mean:", mean, "Standard Dev:", std_dev, "Median:", median, "Mode:", mode)
    else:
        print('Gradebook is empty. Please read in data.')

def enter_data():
    user_input = input("Enter Grades: ")
    name, scores = process_line(user_input)
    GRADEBOOK[name] = scores

def reset():
    if len(GRADEBOOK) > 0:
        GRADEBOOK.clear()
        FINALSCORES.clear()
        print('Reset complete')
    else:
        print('Gradebook already clear.')

def search_by_grade():
    if len(GRADEBOOK) > 0:
        user_input = input("Enter letter grade: ")
        students = []
        for key in GRADEBOOK:
            grade = GRADEBOOK[key][6]
            if grade == user_input:
                students.append(key)
        print("Student(s):", print_list(students, ', '))
    else:
        print('Gradebook is empty. Please read in data.')

show_menu()