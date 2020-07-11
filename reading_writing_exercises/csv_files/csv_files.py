import csv

exam_results = []

with open("exam_results.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
        exam_results.append(line) 

print(exam_results)


for student_results in exam_results:
    # print(f"{student_results[0]} got a score of {student_results[1]}")
    score = float(student_results[1])*100
    score = round(score,2)
    print(f"{student_results[0]:<20} {score}%")  
    #space of 20 characters and left align

with open("exam_results_output.csv","w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ",")
    for student_results in exam_results:
        score = float(student_results[1])*100
        score = round(score,2)
        csv_writer.writerow([student_results[0], f"{score}%"])

    