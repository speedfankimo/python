#coding =utf8
def save_transaction(price, cread_card, description):
    with open("transactions_.txt",'a') as file:
        file.write('%016d\t%07d\t%s' % (cread_card, price[choice - 1]*100, item[choice - 1]))


item = ['Coffee', 'Latte', 'Sandwich', 'Buger', 'Tea']
price = [1.70, 2.20, 2.80, 3.20, 1.80]
running = True

while running:
    option = 1
    for choice in item:
        print (str(option) + '. ' + choice)
        option += 1
    print (str(option) + '. Quit')
    
    choice = input('Choose an option')
    if choice == option:
        running = False
    else:
        cread_card = input('what\'s the cread card ID')
        save_transaction(price, cread_card, item)
        

