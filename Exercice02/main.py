students = {
     'Alice': {
          'Mathematiques': 90,
          'Francais': 80,
          'Histoire': 95
          },
     'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
     },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

student_name = input("Entrez le nom de l'étudiant : ")

if student_name in students.keys():
     print(f"Notes de {student_name} : ")
     average = 0

     for subject in students[student_name]:
          grade = students[student_name][subject]
          average += grade
          print(f"{subject} : {grade}")

     average = round(average / len(students[student_name]), 2)
     print(f"Moyenne de {student_name} : {average}")

else:
     print(f"L'étudiant {student_name} n'existe pas dans la liste.")
