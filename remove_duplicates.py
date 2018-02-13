def remove_duplicates(x):
  result =[]
  for i in x:
    if i not in result:
      result.append(i)
  return result

print remove_duplicates([4,8,4,9,6,6,4,8,1,2,3,2])
