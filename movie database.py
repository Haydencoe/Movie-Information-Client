from selenium import webdriver
import time
import json
import tkinter as tk

key = '6a4a8c6f'
br = webdriver.Firefox(executable_path='geckodriver.exe')

def printDetails(info,window):
    print(info.find_element_by_id("/Title").text)
    print(info.find_element_by_id("/Year").text)
    print(info.find_element_by_id("/Rated").text)
    print(info.find_element_by_id("/Released").text)
    print(info.find_element_by_id("/Runtime").text)
    print(info.find_element_by_id("/Genre").text)
    print(info.find_element_by_id("/Director").text)




#make menu for if know spelling or not
def searchKnown():
    root = tk.Tk()
    ##br.get('http://www.omdbapi.com/?t=toy+story&plot=full&apikey='+ key)
    ##time.sleep(5)
    ##printDetails(br)
    end = False
    while (end != True):
        title = input("please input a title\n")
        br.get('http://www.omdbapi.com/?t='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        printDetails(br,root)
    ##    w = tk.Label(root, text=br.find_element_by_id("/Title").text)
    ##    w.pack()
    ##    w = tk.Label(root, text=br.find_element_by_id("/Year").text)
    ##    w.pack()
    ##    w = tk.Label(root, text=br.find_element_by_id("/Rated").text)
    ##    w.pack()
    ##    w = tk.Label(root, text=br.find_element_by_id("/Released").text)
    ##    w.pack()
    ##    w.mainloop()
        end = input("would you like to search another movie N for no\n")
        if (end == "N"):
            end = True
    

def search():
    end = False
    while (end != True):
        title = input("please input a title\n")
        br.get('http://www.omdbapi.com/?s='+ title.replace(" ", "+")+'&plot=full&apikey='+ key)
        time.sleep(5)
        results = []
        for i in range(10):
            results.append(br.find_element_by_id("/Search/5/Title").text[5:-1])
            print(results[i])



search()
searchKnown()    
