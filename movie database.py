from selenium import webdriver
import time
import json
import random
from functools import partial
from PyQt5.QtWidgets import *

key = '6a4a8c6f'
br = webdriver.Firefox(executable_path='geckodriver.exe')
app = QApplication([])
window = QWidget()
window.setWindowTitle("Movie information client")
layout = QGridLayout()

class numb():
    num = 0

class Gbool():
    second = False

def printDetails(info):
    details = []
    details.append(info.find_element_by_id("/Title").text)
    details.append(info.find_element_by_id("/Year").text)
    details.append(info.find_element_by_id("/Rated").text)
    details.append(info.find_element_by_id("/Released").text)
    details.append(info.find_element_by_id("/Runtime").text)
    details.append(info.find_element_by_id("/Genre").text)
    details.append(info.find_element_by_id("/Director").text)
    for each in range(len(label)):
        label[each].setText(details[each])
        label[each].show()

def printDetails2(info):
    details = []
    details.append(info.find_element_by_id("/title").text)
    details.append(info.find_element_by_id("/release_date").text)
    details.append(info.find_element_by_id("/runtime").text)
    details.append("production company:")
    details.append(info.find_element_by_id("/production_companies/0/name").text)
    details.append(info.find_element_by_id("/production_companies/0/origin_country").text)
    details.append(info.find_element_by_id("/budget").text)
    for each in range(len(label)):
        label[each].setText(details[each])
        label[each].show()

def addWish():
    file = open("wishlist.txt","a+")
    file.writelines(names[num.num].name+"\n")
    wishlist.hide()
    file.close()


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
    end = False
    if(secondSearch.second != True):
        br.get('http://www.omdbapi.com/?t='+ name.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        printDetails(br)
    elif(secondSearch.second == True):
        br.get('https://api.themoviedb.org/3/search/movie?api_key=daff3ba38ac6d2788715a25a34d24d03&query='+ name.replace(" ", "+"))
        time.sleep(5)
        idMovie = br.find_element_by_id("/results/0/id").text
        br.get("https://api.themoviedb.org/3/movie/"+idMovie[-3:len(idMovie)]+"?api_key=daff3ba38ac6d2788715a25a34d24d03")
        printDetails2(br)
    wishlist.show()
    end = True


class searchButton():
    name= "toy story"
    button = None
    def searcher():
        searchKnown2(name)


def search():
    end = False
    while (end != True):
        title = str(lineEdit.text())
        br.get('http://www.omdbapi.com/?s='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        results = []
        for i in range(10):
            results.append(br.find_element_by_id("/Search/"+str(i)+"/Title").text[7:-1])
            names[i].name = results[i]
            names[i].button.setText(results[i])
            names[i].button.show()
            window.setLayout(layout)
            window.show()
        end = True

def randomS():
    end = False
    while(end == False):
        movieID = ""
        for i in range(7):
            movieID += str(random.randint(0,9))
        br.get('http://www.omdbapi.com/?i=tt'+ str(movieID)+'&plot=full&apikey='+ key)
        time.sleep(5)
        if(br.find_element_by_id("/Response").text == 'Response "True"'):
            end = True
    printDetails(br)
    wishlist.show()

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
    num.num = 5
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

def showWish():
    file = open("wishlist.txt","r")
    wishlistitems.clear()
    wishlistitemstrue.clear()
    for movie in file:
        wishlistitems.append(movie[0:-1])
        wishlistitemstrue.append(movie)
    counter = 0
    for i in range(10):
        if (i <len(wishlistitems)):
            if (counter<=9):
                wishB[i].button.setText(wishlistitems[i])
                wishB[i].button.show()
            counter +=1
        else:
            wishB[i].button.hide()
    window.setLayout(layout)
    window.show()

def delWish():
    file = open("wishlist.txt","w")
    indexf = 0
    for each in wishlistitemstrue:
        if (indexf != wishNum.num):
            file.write(each)
        indexf+=1
    file.close()


def w0():
    wishNum.num = 0
    delWish()
    showWish()

def w1():
    wishNum.num = 1
    delWish()
    showWish()

def w2():
    wishNum.num = 2
    delWish()
    showWish()

def w3():
    wishNum.num = 3
    delWish()
    showWish()

def w4():
    wishNum.num = 4
    delWish()
    showWish()

def w5():
    wishNum.num = 5
    delWish()
    showWish()

def w6():
    wishNum.num = 6
    delWish()
    showWish()

def w7():
    wishNum.num = 7
    delWish()
    showWish()

def w8():
    wishNum.num = 8
    delWish()
    showWish()

def w9():
    wishNum.num = 9
    delWish()
    showWish()

def search2():
    secondSearch.second = True
    search()

def search1():
    secondSearch.second = False
    search()


secondSearch = Gbool()
num = numb()
wishNum = numb() 
current = ""
lineEdit = QLineEdit(window)
layout.addWidget(lineEdit,1,1)
button = QPushButton('Search OMDB', window)
layout.addWidget(button,2,1)
buttonS2 = QPushButton('Search TMDB', window)
layout.addWidget(buttonS2,3,1)
buttonS3 = QPushButton('Search Random Movie', window)
layout.addWidget(buttonS3,4,1)
buttonS3.clicked.connect(randomS)
wishlistshow = QPushButton('Show wishlist', window)
buttonS2.clicked.connect(search2)
layout.addWidget(wishlistshow,1,4)
wishlistshow.clicked.connect(showWish)
names = [searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton()]
label = ["name","year", "rated", "released","run time", "genre", "director"]
label2 = ["name","year", "rated", "released","run time", "genre", "director"]
wishlistitems = []
wishlistitemstrue = []
button.clicked.connect(search1)
for each in range(10):
    names[each].button = QPushButton(str(each), window)
    layout.addWidget(names[each].button,each+5,1)
    names[each].button.hide()
for each in range(len(label)):
    label[each] = QLabel("test")
    layout.addWidget(label[each],each+1,2)
    label[each].hide()
wishlist = QPushButton('Add to wishlist', window)
layout.addWidget(wishlist)
wishlist.clicked.connect(addWish,1,12)
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
label1=  QLabel("Wish List:")
layout.addWidget(label1,2,4)
wishB =[searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton(),searchButton()]
for each in range(len(wishB)):
    wishB[each].button = QPushButton("this is default and shouldn't be shown", window)
    layout.addWidget(wishB[each].button,each+3,4)
    wishB[each].button.hide()
wishB[0].button.clicked.connect(w0)
wishB[1].button.clicked.connect(w1)
wishB[2].button.clicked.connect(w2)
wishB[3].button.clicked.connect(w3)
wishB[4].button.clicked.connect(w4)
wishB[5].button.clicked.connect(w5)
wishB[6].button.clicked.connect(w6)
wishB[7].button.clicked.connect(w7)
wishB[8].button.clicked.connect(w8)
wishB[9].button.clicked.connect(w9)
window.setLayout(layout)
window.show()
app.exec_()
##search()
