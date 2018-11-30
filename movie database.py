from selenium import webdriver
import time
import json
from functools import partial
from PyQt5.QtWidgets import *

key = '6a4a8c6f'
br = webdriver.Firefox(executable_path='geckodriver.exe')
app = QApplication([])
window = QWidget()
window.setWindowTitle("Movie information client")
layout = QVBoxLayout()

class numb():
    num = 0

def printDetails(info):
    details = []
    ##print(info.find_element_by_id("/Title").text)
    details.append(info.find_element_by_id("/Title").text)
    ##print(info.find_element_by_id("/Year").text)
    details.append(info.find_element_by_id("/Year").text)
    ##print(info.find_element_by_id("/Rated").text)
    details.append(info.find_element_by_id("/Rated").text)
    ##print(info.find_element_by_id("/Released").text)
    details.append(info.find_element_by_id("/Released").text)
    ##print(info.find_element_by_id("/Runtime").text)
    details.append(info.find_element_by_id("/Runtime").text)
    ##print(info.find_element_by_id("/Genre").text)
    details.append(info.find_element_by_id("/Genre").text)
    ##print(info.find_element_by_id("/Director").text)
    details.append(info.find_element_by_id("/Director").text)
    for each in range(len(label)):
        label[each].setText(details[each])
        label[each].show()

def addWish():
    file = open("wishlist.txt","a+")
    print(str(num.num))
    file.writelines(names[num.num].name+"\n")
    wishlist.hide()
    file.close()


#make menu for if know spelling or not
def searchKnown():
    root = tk.Tk()
    end = False
    while (end != True):
        title = input("please input a title\n")
        br.get('http://www.omdbapi.com/?t='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        printDetails(br)
        end = input("would you like to search another movie N for no\n")
        if (end == "N"):
            end = True
        


def searchKnown2(name):
    ##current = name
    end = False
    ##print("here i am")
    br.get('http://www.omdbapi.com/?t='+ name.replace(" ", "+")+'&plot=full&apikey='+ key)
    time.sleep(5)
    printDetails(br)
    wishlist.show()
    end = True
##    yes = ["y","Y","yes","Yes"]
##    while (end != True):
##        wish = input("Would you like to add this film to your to your wish list (y|Y|yes|Yes for yes)\n")
##        if (wish in yes):
##            addWish(name)
##        end = True


class searchButton():
    name= "toy story"
    button = None
    def searcher():
##        print("in class funct")
        searchKnown2(name)


def search():
    end = False
    while (end != True):
        ##title = input("please input a title\n")
        title = str(lineEdit.text())
        br.get('http://www.omdbapi.com/?s='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        results = []
        for i in range(10):
            results.append(br.find_element_by_id("/Search/"+str(i)+"/Title").text[7:-1])
            ##print(str(i+1) +": "+results[i]+" ("+br.find_element_by_id("/Search/"+str(i)+"/Type").text[6:-1]+")")
            names[i].name = results[i]
            names[i].button.setText(results[i])
            names[i].button.show()
            window.setLayout(layout)
            window.show()
        end = True
##        chose = False
##        if (chose == False):
##            option = input("which title woud you like information about?\n")
##            if (int(option) in range(11)):
##                name = results[int(option) - 1]
##                ##searchKnown2(name)
##                chose = True
##                end = True
##        ##end = input("would you like to search another movie N for no\n")
##        ##if (end == "N"):
##            ##end = True

def b0():
    current = names[0].name
    num.num = 0
    searchKnown2(names[0].name)

def b1():
    current = names[1].name
    num.num = 1
    searchKnown2(names[1].name)

def b2():
    current = names[2].name
    num.num = 2
    searchKnown2(names[2].name)

def b3():
    current = names[3].name
    num.num = 3
    searchKnown2(names[3].name)

def b4():
    current = names[4].name
    num.num = 4
    searchKnown2(names[4].name)

def b5():
    current = names[5].name
    num,num = 5
    searchKnown2(names[5].name)

def b6():
    current = names[6].name
    num.num = 6
    searchKnown2(names[6].name)

def b7():
    current = names[7].name
    num.num = 7
    searchKnown2(names[7].name)

def b8():
    current = names[8].name
    num.num = 8
    searchKnown2(names[8].name)

def b9():
    current = names[9].name
    num.num = 9
    searchKnown2(names[9].name)

num = numb()
current = ""
lineEdit = QLineEdit(window)
layout.addWidget(lineEdit)
button = QPushButton('Search', window)
layout.addWidget(button) 
names = [searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton()]
label = ["name","year", "rated", "released","run time", "genre", "director"]
button.clicked.connect(search)
for each in range(10):
    names[each].button = QPushButton(str(each), window)
    layout.addWidget(names[each].button)
    names[each].button.hide()
for each in range(len(label)):
    label[each] = QLabel("test")
    layout.addWidget(label[each])
    label[each].hide()
wishlist = QPushButton('Add to wishlist', window)
layout.addWidget(wishlist)
wishlist.clicked.connect(addWish)
wishlist.hide()
names[0].button.clicked.connect(b0)
names[1].button.clicked.connect(b1)
names[2].button.clicked.connect(b2)
names[3].button.clicked.connect(b3)
names[4].button.clicked.connect(b4)
names[5].button.clicked.connect(b5)
names[6].button.clicked.connect(b6)
names[7].button.clicked.connect(b7)
names[8].button.clicked.connect(b8)
names[9].button.clicked.connect(b9)
window.setLayout(layout)
window.show()
app.exec_()
##search()
