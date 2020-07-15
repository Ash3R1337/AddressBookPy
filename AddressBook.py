import os
import codecs

def NewContact():
    Name_Contact = input('Имя:\n')
    Num_Contact = input('Номер:\n')
    Email_Contact = input('Почта:\n')
    Contact =  [Name_Contact, Num_Contact, Email_Contact]
    f = codecs.open('contacts.txt', 'a+', 'utf-8')
    for item in Contact:
        f.write("%s\n" % item)
    print('\n Создан новый контакт: Имя: {0}, Номер: {1}, Почта: {2}\n'.format(Name_Contact, Num_Contact, Email_Contact))
    f.close()
    Else()

def Else():
    print('Добавьте новый контакт или прочитайте существующие.')
    print('Новый контакт: NEW, Посмотреть список: CHECK, Очистить список: CLEAR\n')
    user = input()
    user = user.lower()
    if (user == 'new'):
        NewContact()
    elif (user == 'check'):
        f = codecs.open('contacts.txt', 'r+', 'utf-8')
        print('\n', f.read())
        f.close()
    elif (user == 'clear'):
        f = open('contacts.txt', 'w')
        print('\n Список был успешно очищен.')
        print('У вас нет контактов, запишите...\n')
        NewContact()
    else:
        print('Команда введена неправильно, повторите попытку...')
    Else()

if os.path.exists('contacts.txt'):
    f = codecs.open('contacts.txt', 'r+', 'utf-8')
else:
    f = codecs.open('contacts.txt', 'w', 'utf-8')
    print('У вас нет контактов, запишите...\n')
    NewContact()
num = len(f.read())
if (num == 0):
    print('У вас нет контактов, запишите...\n')
    NewContact()
else:
    Else()