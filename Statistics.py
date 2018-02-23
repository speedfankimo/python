grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    X = grade
    print X ,
print print_grades(grades)

#總數
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
print "sum =" + "%.2f" %(grades_sum(grades))
print grades_sum(grades)

#平均數    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average
print "average =" + "%.2f" %(grades_average(grades))
print grades_average(grades)

# 變異數
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores :
    variance += (average - score) ** 2
  return variance / float(len(scores))
print "variance =" + "%.2f" % (grades_variance(grades))
print grades_variance(grades)

# 標準差
def grades_std_deviation(variance):
  return variance ** 0.5
variance = grades_variance(grades)
print  "std_deviation ="+ "%.2f" % (grades_std_deviation(variance))
print grades_std_deviation(variance)

# my way 標準差
#def grades_std_deviation(scores):
#  variance = grades_variance(scores)
#  return float(variance ** 0.5)
#print  "%.3f" % (grades_std_deviation(grades))
