# -*- coding: utf-8 -*-

def celsius(temp):
    fahrenheit = temp*(9/5)+32
    return fahrenheit
    
def fahrenheit(temp):
    celsius = (temp-32)*5/9
    return celsius

choise = int(input('請選擇你的溫度單位,1為攝氏;2為華氏 :'))
if choise == 1:
    input_temp = float(input('請輸入溫度為攝氏幾度:'))
    print ('攝氏 %.2f 度= 華氏 %.2f 度' % (input_temp, celsius(input_temp)))
elif choise == 2:
    input_temp = float(input('請輸入溫度為華氏幾度:'))
    print ('華氏 %.2f 度= 攝氏 %.2f 度' % (input_temp, fahrenheit(input_temp)))

    


