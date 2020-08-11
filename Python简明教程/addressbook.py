#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: xiekai
import pickle
import sys
import os


class Person():
    def __init__(self, name, phoneNum, addr):
        self.name = name
        self.phoneNum = phoneNum
        self.addr = addr

    def getname(self):
        return self.name

    def getphoneNum(self):
        return self.phoneNum

    def getaddr(self):
        return self.addr


class addrBook:

    def __init__(self, option='add'):
        self.addressBook = {}
        self.addressBookFile = 'Address.data'
        if os.path.exists('Address.data'):
            self.addrFile = open(self.addressBookFile, 'rb')
        else:
            print('file not exists, then creat it')
            self.addrFile = open(self.addressBookFile, 'w')
        try:
            self.addressBook = pickle.load(self.addrFile)
        except(Exception):
            if option == 'add':  # 3 is add
                pass
            else:
                print('This addr is Empty')
                self.addrFile.close()
                sys.exit()
        finally:
            self.addrFile.close()

    def addPerson(self, name, phoneNum, addr):
        try:
            somePerson = Person(name, phoneNum, addr)
            if name in self.addressBook:
                print('User %s already added to the addressbook' % name)
            else:
                self.addressBook[name] = somePerson
                print('Add person {} Success'.format(name))
        except EOFError:
            print('There are some exceptions in add person')

    def searchPerson(self, name):
        try:
            for nameFromBook, personFromBook in self.addressBook.items():
                if nameFromBook == name:
                    print('The address and phoneNumber of %s are %s and %s \
                    ' % (name, personFromBook.getaddr(), personFromBook.getphoneNum()))
                    return
            print('there are no user of {}'.format(name))
        except(Exception):
            print('There are some exception in search person')

    def delPerson(self, name):
        try:
            if name in self.addressBook:
                del self.addressBook[name]
            else:
                print('There is no user of %s' % name)
        except(Exception):
            print('There are some exception in del person')

    def __del__(self):
        try:
            self.addrFile = open(self.addressBookFile, 'wb')
            if not self.addressBook:
                pass
            else:
                pickle.dump(self.addressBook, self.addrFile)
        except(Exception):
            print('Some exception occur when write data to file')
        finally:
            self.addrFile.close()

    def ListAllPerson(self):
        try:
            for nameFromBook, personFromBook in self.addressBook.items():
                print('The address and phoneNumber of %s are %s and %s'
                      % (nameFromBook, personFromBook.getaddr(), personFromBook.getphoneNum()))
        except(Exception):
            print('There are some exception in listing person ')


helpDoc = ''' All the Command as follow:
    1.--help    :show help
    2.--version :show version
    3.--add     :add user to addrbook
    4.--del     :del user form addrbook
    5.--search  :search user from addrbook
    6.--list    :list the all number in the addrbook'''


def main():
    # if len(sys.argv) < 2:
    #     print('No Action Occur.')
    #     print(helpDoc)
    #     sys.exit()

    # if sys.argv[1].startswith('--'):
    #     option = sys.argv[1][2:]

    while True:
        select = input('''Pleset select you want to funtion:
        1. help
        2. version
        3. add
        4. del
        5. search
        6. list all
        x. exit
        ''')
        function = {'1': 'help', '2': 'version', '3': 'add', '4': 'del',
                    '5': 'search', '6': 'list', 'x': 'exit'}
        if select in function:
            option = function[select]    
            print('you select function:{}'.format(option))
            break
        else:
            print('Do not chose a function, please try again!')

    if select == 'x':
        sys.exit()
    elif option == 'help':
        print(helpDoc)
        sys.exit()
    elif option == 'version':
        print("Version 0.0.1")
        sys.exit()

    addrBookInst = addrBook(option)
    if option == 'add':
        try:
            name = input('Please input you want to add name:')
            x = len(name)
            while(x == 0):
                name = input('Input name is null, please input again:')
                x = len(name)
            phoneNum = input('Please input the phone number:')
            addr = input('Please input the address:')
        except EOFError:
            sys.exit()
        except KeyboardInterrupt:
            print('stop from keyboard!')
        except(Exception):
            print('input value error!')

        addrBookInst.addPerson(name, phoneNum, addr)
    elif option == 'del':
        name = input('Please input the name you want to del:')
        addrBookInst.delPerson(name)
    elif option == 'search':
        name = input('Please input the name you want to search：')
        addrBookInst.searchPerson(name)
    elif option == 'list':
        addrBookInst.ListAllPerson()
    else:
        print('Parameter wrong, please check with help.')
    sys.exit()


if __name__ == "__main__":
    main()
