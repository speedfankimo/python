#偶數 Even
def purify(numbers):
  result = []
  for number in numbers:
    if number%2 == 0:
      result.append(number) # 貼上的方式
      #print result
  return result
print purify([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print 
#其數 Odd
def purify(numbers):
  result = []
  for number in numbers:
    if number%2 == 1:
      result.append(number) # 貼上的方式
      #print result
  return result
print purify([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
