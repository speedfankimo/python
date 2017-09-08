# -*- coding: utf-8 -*-
Math = 80
English = 60
if not Math <79 or (Math >=60 and English >=60):
    print  u"you are qualify 我"
else :
    print "Sorry! you are not qualify!"

"""if not Math >=60 :
    #print "You should learn more"""


# -*- coding: utf8 -*-
msg = u'今天天氣真好'
encoded = msg.encode('utf8')
print repr(encoded)

# -*- coding: utf8 -*-
encoded = '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa4\xa9\xe6\xb0\xa3\xe7\x9c\x9f\xe5\xa5\xbd'
msg = encoded.decode('utf8')
print msg

string = u'你好我叫陳世彬'
encode = string.encode('utf8')
print repr(encode)

code = '\xe4\xbd\xa0\xe5\xa5\xbd\xe6\x88\x91\xe5\x8f\xab\xe9\x99\xb3\xe4\xb8\x96\xe5\xbd\xac'
decode = code.decode('utf8')
print decode
