kindergarden = {
    'Krosh':
    {
        'cartoon':'kikoriki',
        'form':'circle',
        'color':'blue',
        'age':16
    },
    'Gadget':
    {
        'cartoon':'inspector Gadget',
        'form':'human',
        'color':'white',
        'age':37
    },
    'Winnie-the-Puh':
    {
        'cartoon':'adventures of Winnie-the-Puh',
        'form':'bear',
        'color':'yellow',
        'age':99
    },
}

name1 = input("Enter name: ")
flag = True

for search_kinder in kindergarden:
    if search_kinder == name1:
        print(kindergarden[search_kinder])
        flag = False

if flag:
    print('No such kinder')
    

#Enter name: Gadget
#{'cartoon': 'inspector Gadget', 'form': 'human', 'color': 'white', 'age': 37}