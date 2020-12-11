groupmates = [
    {
        "name": "Мария",
        "surname": "Гуслякова",
        "exams": ["Философия","ИС","АиГ"],
        "marks": [4,3,3]
    },
    
    {
        "name": "Даниил",
        "surname": "Иванов",
        "exams": ["История","ИКТ","Физика"],
        "marks": [5,5,5]
    },
    
    {

        "name": "Максим",
        "surname": "Петров",
        "exams": ["КТП","ЭЭиС","Психология"],
        "marks": [4,5,5]
    },
    
    {
        "name": "Анастасия",
        "surname": "Сидорова",
        "exams": ["Информатика","АиГ","КТП"],
        "marks": [4,5,4]
    }]

def count_mark(students,mark):
    print (u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамен".ljust(20), u"Оценка".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(8), str(student["exams"]).ljust(8), str(student["marks"]).ljust(20))

need = int(input('Средний бал :'))

count_mark(groupmates,need)
