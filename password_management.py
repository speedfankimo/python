# -*- coding: utf-8 -*-
import os
import ast

# =============================================================================
# Main page
# =============================================================================

def openPage():
    os.system("cls")
    print ("   帳號/密碼管理系統")
    print ("1. 輸入 帳號、密碼")
    print ("2. 顯示 帳號、密碼")
    print ("3. 修改 帳號、密碼")
    print ("4. 刪除 帳號、密碼")
    print ("0. 結  束  程  式")
    print ("------------------------------------")

# =============================================================================
# input  username / password function
# =============================================================================

def createUser():  
    n = 0
    account = {}
    while n != 1:
        user = input('請輸入帳號 : ')
        password = input('請輸入密碼 : ')
        oneUser = {user: password}
        account.update(oneUser)
        n = int(input('如需繼續輸入(按0)，跳出(按1)'))
    print (account)
    f = open("memberinfo.txt", "a", encoding='UTF-8')
    list = f.write(str(account) + "\n")
    f.close()

# =============================================================================
# convert the string data to dictionary
# =============================================================================

def readData():   
    with open("memberinfo.txt", "r", encoding="UTF-8-sig") as f:
        filedata = f.readlines()              #讀一列
#        print (filedata)
        if filedata != "":  
            data = {} 
            for line in filedata:
                line = ast.literal_eval(line)  # 資料轉換成dictionary                
                data.update(line)
            return data
        else:
            return dict()

# =============================================================================
# display all account information  
# =============================================================================
      
def dispAccount():          
    print ("帳號\t密碼")
    print ("----------------------")
    for key in readData():
        print ("{}\t{}" .format(key,readData()[key]))
    print ("----------------------")
        
# =============================================================================
# alter the password       
# =============================================================================
        
def editAccount():
    while True:
       user = input('請輸入帳號 (ENTER跳出): ') 
       if user == "" :
           break
       if not user in readData():
           print ("{},此帳號並不存在".format(user))
           continue
       print ("原來的密碼為 : {}" .format(readData()[user]))
       password = input('請輸入新密碼 : ')  
       newData={}
       newData.update(readData())
       newData[user] = password
       with open("memberinfo.txt", "w", encoding="UTF-8-sig") as f:
           f.write(str(newData))
           break
       
# =============================================================================
# delete the account        
# =============================================================================
        
def delAccount():        
    while True:
        user = input('請輸入帳號 (ENTER跳出): ')
        if user == "":
            break
        if not user in readData():
            print ("{},此帳號並不存在".format(user))
            continue
        comment = input ("請確認是否刪除帳號:{} (Y/N)" .format(user))
        if (comment == "Y" or comment == "y"):
            newData={}
            newData.update(readData())
            del newData[user]
            with open("memberinfo.txt", "w", encoding="UTF-8-sig") as f:
                f.write(str(newData))
                break
        else:
            break
        

# =============================================================================
#  主程式
# =============================================================================
      
        
data = {}
data = readData()  #讀取文件表格的Dictionary

while True:
    openPage()
    choice = int(input ("請輸入您的選擇 :"))
    if choice ==1:
        createUser()
    elif choice ==2:
        dispAccount()
    elif choice ==3:
        editAccount()
    elif choice == 4:
        delAccount()
    else:
        break
        
