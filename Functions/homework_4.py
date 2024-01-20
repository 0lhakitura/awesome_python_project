from collections import Counter
import pandas as pd


# TASK 1: sorted names write in a new file
def sort_names_and_write_in_a_new_file(filepath_unsorted_names, filepath_sorted_names):
    with open(filepath_unsorted_names) as unsorted_names, open(filepath_sorted_names, 'w') as sorted_names:
        content = []
        for line in unsorted_names:
            content.append(line)
        unsorted_names.close()
        sorted_content = sorted(content)
        for name in sorted_content:
            sorted_names.write(name)


# TASK 2: Implement a function which search for most common words in the file.
def most_common_words(filepath, number_of_words=3):
    with open(filepath) as in_file:
        content_in_file = in_file.readlines()
    list_content = []
    for line in content_in_file:
        if line != "\n":
            list_content.append(line.lower().replace(',', '').replace('.', '').split(" "))
    counter_tuple = ()
    for word in list_content:
        counter_tuple = counter_tuple + tuple(word)
    counter_list = Counter(counter_tuple)
    return counter_list.most_common(number_of_words)


# TASK 3 PART 1
def get_top_performers(file_path, number_of_top_students=5):
    students = pd.read_csv(file_path)
    return students.sort_values(by=['average mark'], ascending=False)['student name'].head(number_of_top_students)


# TASK 3 PART 2
def write_student_info_in_desc_order_of_age(file_path):
    students = pd.read_csv(file_path)
    sorted_students = students.sort_values(by=['age'], ascending=False)
    sorted_students.to_csv('sorted_students.csv')


if __name__ == '__main__':
    source_file_path = 'data/students.csv'
    destination_file_path = 'students_new.csv'