marry = {
    "name":"Marry",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
    }

john = {
    "name": "John",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
    }

kyle = {
    "name": "Klye",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
    }

def average(numbers):
    total = sum(numbers)
    float(total)
    avg = total / float(len(numbers))
    #print avg
    return avg

#average([20,30])

def student_avg(students):
    homework = average(students["homework"]) * 0.1
    quizzes = average(students["quizzes"]) * 0.3
    tests = average(students["tests"]) * 0.6
    student_score = homework + quizzes + tests
    #print student_score
    return student_score

def student_class(score):
    if score > 90:
        return 'A'
    elif score >80:
        return 'B'
    elif score >70:
        return 'C'
    elif score >60:
        return 'D'
    else:
        return 'F'
    
def total_class(classes):
    result = []
    for member in classes:
        result.append(student_avg(member))
        #print result
    return result
    
        

members = [john,kyle,marry]
for member in members:
    print "%s's average score = %s" %(member["name"] ,str(student_avg(member)))
    print "Level = %s" % (str(student_class(student_avg(member))))
    print

print "This class's average score = %.2f " % (average(total_class(members)))
print "Level = %s" % (student_class(average(total_class(members))))

        
