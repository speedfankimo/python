def censor(X,Y):
  x=str.lower(X) #normailze字串(變成小寫)
  y=str.lower(Y) #normailze字串(變成小寫)
  text = x.split() #把字串變成array
  print text
  if y in text:
    new_text = x.replace(y,"*"*len(y))
    return new_text
print censor("I love You","you")
