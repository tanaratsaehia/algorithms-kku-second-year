import os
import json
from tabulate import tabulate

class GradingStudent:
    def __init__(self) -> None:
        self.std_data = {}
        self.main_manu_list = ['1.show student data', '2.add or edit student data', '3.export student data to json file', '4.exit']
        self.sub_menu_2 = ['1.add new student', '2.edit student data', '3.add subject data', '4.delete subject', '5.back to main menu']    
    
    def show_data(self, std_name=None, show_grade=True) -> None:
        """show student data default is all or select by student name"""
        if len(self.std_data) > 0:
            if std_name:
                if std_name in self.std_data:
                    total_score = 0
                    total_credit = 0
                    print(f'\nStudent name: {std_name}')
                    table = [['Subject Name', 'Credit', 'Grade']]
                    if self.std_data[std_name]:
                        for subject, credit, grade in self.std_data[std_name]:
                            table.append([subject, credit, grade])
                            total_score += credit * grade
                            total_credit += credit
                        if show_grade:
                            if total_credit > 0:
                                gpa = total_score / total_credit
                                table.append(['GPA', '', f'{gpa:.2f}'])
                            else:
                                table.append(['GPA', '', '0.00'])
                    else:
                        table.append([])
                    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
                    print()
                else:
                    print('student name "'+std_name+'" not found')
            else:
                for student, subjects in self.std_data.items():
                    total_score = 0
                    total_credit = 0
                    print(f'\nStudent name: {student}')
                    table = [['Subject Name', 'Credit', 'Grade']]
                    for subject, credit, grade in subjects:
                        table.append([subject, credit, grade])
                        total_score += credit * grade
                        total_credit += credit
                    if show_grade:
                        if total_credit > 0:
                            gpa = total_score / total_credit
                            table.append(['GPA', '', f'{gpa:.2f}'])
                        else:
                            table.append(['GPA', '', '0.00'])
                    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
                    print()
        else:
            print('No data to process!')
    
    def subject_exists(self, student, subject_name) -> bool:
        if student not in self.std_data:
            return False
        if self.std_data[student]:
            for subject, _, _ in self.std_data[student]:
                if subject == subject_name:
                    return True
        return False
    
    def add_student(self, std_name, data=None) -> None:
        """just fill student name"""
        if std_name not in self.std_data:
            if data:
                self.std_data[std_name] = [data]
            else:
                self.std_data[std_name] = []
            print(f'student "{std_name}" added')
        else:
            print('student "'+std_name+'" already exists')
    
    def add_subject(self, std_name, data) -> None:
        """ example data ['subj_name', credit, grade] """
        # print('here1111')
        if not self.subject_exists(std_name, data[0]):
            self.std_data[std_name].append(data)
            self.show_data(std_name)
        else:
            print('student "'+std_name+'" already have subject "'+data[0]+'"')
            con = input('you want to replace with '+data+' type yes(y) or no(n) : ')
            if con == 'y' or con == 'yes':
                for i, (subject, _, _) in enumerate(self.std_data[std_name]):
                    if subject == data[0]:
                        self.std_data[std_name][i] = data
                # for i in range(len(self.std_data[std_name])):
                #     if self.std_data[std_name][i][0] == data[0]:
                #         self.std_data[std_name][i] = data
                print('change data success')
            elif con == 'n' or con == 'no':
                print('not change skip....')
            else:
                print('invalid commad nothing change skip....')
    
    def edit_subject(self, std_name, data) -> None:
        """edit subject iden by subject name input same name this func replace it with new data"""
        if std_name in self.std_data:
            if self.subject_exists(std_name, data[0]):
                for i, (subject, _, _) in enumerate(self.std_data[std_name]):
                    if subject == data[0]:
                        self.std_data[std_name][i] = data
                # for i in range(len(self.std_data[std_name])):
                #     if self.std_data[std_name][i][0] == data[0]:
                #         self.std_data[std_name][i] = data
                print('data saved')
                self.show_data(std_name)
            else:
                print('student "'+std_name+'" not have subject "'+data[0]+'"')
    
    def delete_subject(self, std_name, subject_name) -> None:
        if std_name not in self.std_data:
            print(f'Student "{std_name}" does not exist.')
            return
        for i, (subject, _, _) in enumerate(self.std_data[std_name]):
            if subject == subject_name:
                del self.std_data[std_name][i]
                print(f'Subject "{subject_name}" removed for student "{std_name}".')
                self.show_data(std_name)
                return
        print(f'Subject "{subject_name}" not found for student "{std_name}".')
    
    def get_std_name(self) -> list:
        std_name = []
        if len(self.std_data) > 0:
            for i in self.std_data:
                std_name.append(i)
            return std_name
        else:
            return None
    
    def to_json(self) -> None:
        with open('student_data.json', 'w') as file:
            json.dump(self.std_data, file, indent=4)
        print('data saved at', os.getcwd()+'\student_data.json')

data = {}
data['oil'] = [['math', 2, 3.5], ['com pro', 3, 3.5], ['test', 2, 3.5], ['test2', 2, 3.5]]
# data['oil'].append(['test2', 2, 3.5])
data['test'] = [['math', 2, 3], ['com pro', 3, 1.5], ['test', 2, 3]]
data['ttt'] = []

gd = GradingStudent()
gd.std_data = data


while True:
    print('select menu')
    print('\t' + '\n\t'.join(gd.main_manu_list))
    try:
        selected_menu = int(input(f'please select number of menu (1-4) : '))
        if selected_menu == 4:
            break
        elif selected_menu not in [1, 2, 3, 4]:
            print('----------------------------------\ninvalid menu pls try again\n----------------------------------')
            continue
    except:
        print('----------------------------------\ninvalid menu pls try again\n----------------------------------')
        continue
    
    # show student data
    if selected_menu == 1:
        print('type student name or not type for show all student data')
        std_name = str(input('type here: '))
        gd.show_data(std_name)
    
    # add or edit student data
    elif selected_menu == 2:
        while True:
            print('\nselect option')
            print('\t'+'\n\t'.join(gd.sub_menu_2))
            try:
                selected_op = int(input('please select number of option (1-5) : '))
                if selected_menu == 5:
                    break
                elif selected_menu not in [1, 2, 3, 4, 5]:
                    print('----------------------------------\ninvalid menu pls try again\n----------------------------------')
                    continue
            except:
                print('----------------------------------\ninvalid option pls try again\n----------------------------------')
            
            # 1.add student
            if selected_op == 1:
                print(f'you should option {gd.sub_menu_2[selected_op-1]} ')
                std_name = str(input('input new student name : '))
                gd.add_student(std_name)
            
            # 2.edit student data
            elif selected_op == 2:
                print(f'you should option {gd.sub_menu_2[selected_op-1]} ')
                while True:
                    std_name = gd.get_std_name()
                    print('All student name')
                    for i in range(len(std_name)):
                        print(f'\t{i+1}.{std_name[i]}')
                    std_name = str(input('input student name for edit data or ("e" for exit to main menu) : '))
                    if std_name in gd.std_data:
                        gd.show_data(std_name)
                        print('input data identify by subject name')
                        print('\tformat data is subject_name, credit, grade')
                        print('\tlike math, 3, 3.5')
                        new_data = str(input('input new data : '))
                        new_data = new_data.split(',')
                        if len(new_data) == 3:
                            try:
                                new_data[1] = int(new_data[1])
                                new_data[2] = float(new_data[2])
                                gd.edit_subject(std_name, new_data)
                            except:
                                print('wrong data pls try again')
                                continue
                    elif std_name == 'e':
                        break
                    else:
                        print(f'student "{std_name}" not found')
            
            # 3.add subject
            elif selected_op == 3:
                print(f'you should option {gd.sub_menu_2[selected_op-1]} ')
                while True:
                    std_name = gd.get_std_name()
                    print('All student name')
                    for i in range(len(std_name)):
                        print(f'\t{i+1}.{std_name[i]}')
                    std_name = str(input('input student name for add subject or ("e" for exit to main menu) : '))
                    if std_name in gd.std_data:
                        gd.show_data(std_name)
                        print('input new data')
                        print('\tformat data is subject_name, credit, grade')
                        print('\tlike math, 3, 3.5')
                        new_data = str(input('input new data : '))
                        new_data = new_data.split(',')
                        if len(new_data) == 3:
                            try:
                                new_data[1] = int(new_data[1])
                                new_data[2] = float(new_data[2])
                                # print(new_data)
                                gd.add_subject(std_name, new_data)
                            except:
                                print('wrong data pls try again')
                                continue
                    elif std_name == 'e':
                        break
                    else:
                        print(f'student "{std_name}" not found')
            
            # 4.delete subject
            elif selected_op == 4:
                print(f'you should option {gd.sub_menu_2[selected_op-1]} ')
                while True:
                    std_name = gd.get_std_name()
                    print('All student name')
                    for i in range(len(std_name)):
                        print(f'\t{i+1}.{std_name[i]}')
                    std_name = str(input('input student name for delete subject or ("e" for exit to main menu) : '))
                    if std_name in gd.std_data:
                        gd.show_data(std_name)
                        subj_name = str(input('input subject name for delete : '))
                        gd.delete_subject(std_name, subj_name)
                    elif std_name == 'e':
                        break
                    else:
                        print(f'student "{std_name}" not found')
            
            # 5.back to main menu
            elif selected_op == 5:
                print(f'you should option {gd.sub_menu_2[selected_op-1]} ')
                break
    
    # 3.export student data to json file
    elif selected_menu == 3:
        gd.to_json()

# testing
    # main menu 1 passed
    # main menu 2 passed
        # case 1 passed
        # case 2 passed
        # case 3 passed
        # case 4 passed
        # case 5 passed
    # main menu 3 passed