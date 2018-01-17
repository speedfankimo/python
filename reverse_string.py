# my way
def reverse(string):
  x = len(string)-1
  new_word = ''
  while x >= 0:
    new_word += string[x] #new_word = new_word + string[x]
    x -=1
  return new_word
    
print reverse("!nohtyP")


# Codecademy's Guidance
def reverse2(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
print reverse2('text')
