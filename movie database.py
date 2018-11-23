from selenium import webdriver
import time
import json
import tkinter as tk

key = '6a4a8c6f'
br = webdriver.Firefox(executable_path='geckodriver.exe')

def printDetails(info):
    print(info.find_element_by_id("/Title").text)
    print(info.find_element_by_id("/Year").text)
    print(info.find_element_by_id("/Rated").text)
    print(info.find_element_by_id("/Released").text)
    print(info.find_element_by_id("/Runtime").text)
    print(info.find_element_by_id("/Genre").text)
    print(info.find_element_by_id("/Director").text)

def addWish(name):
    file = open("wishlist.txt","a+")
    file.writelines(name+"\n")


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
            w = tk.Label(root, text=br.find_element_by_id("/Title").text)
            w.pack()
            w = tk.Label(root, text=br.find_element_by_id("/Year").text)
            w.pack()
            w = tk.Label(root, text=br.find_element_by_id("/Rated").text)
            w.pack()
            w = tk.Label(root, text=br.find_element_by_id("/Released").text)
            w.pack()
            w.mainloop()


def searchKnown2(name):
    end = False
    br.get('http://www.omdbapi.com/?t='+ name.replace(" ", "+")+'&plot=full&apikey='+ key)
    time.sleep(5)
    printDetails(br)
    yes = ["y","Y","yes","Yes"]
    while (end != True):
        wish = input("Would you like to add this film to your to your wish list (y|Y|yes|Yes for yes)\n")
        if (wish in yes):
            addWish(name)
        end = True

            
def search():
    end = False
    while (end != True):
        title = input("please input a title\n")
        br.get('http://www.omdbapi.com/?s='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        results = []
        for i in range(10):
            results.append(br.find_element_by_id("/Search/"+str(i)+"/Title").text[7:-1])
            print(str(i+1) +": "+results[i]+" ("+br.find_element_by_id("/Search/"+str(i)+"/Type").text[6:-1]+")")
        chose = False
        if (chose == False):
            option = input("which title woud you like information about?\n")
            if (int(option) in range(11)):
                name = results[int(option) - 1]
                searchKnown2(name)
                chose = True
        end = input("would you like to search another movie N for no\n")
        if (end == "N"):
            end = True

search()
