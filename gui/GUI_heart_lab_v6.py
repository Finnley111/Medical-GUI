# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:08:09 2022

@author: finnl
"""


# Load packages
import matplotlib.pyplot as plt
import pandas as pd
import os 
import random
import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure



from platform import python_version
 
 
print("Current Python Version-", python_version())


#tracks whether a case file is opened
CASE_SELECTED = False
#font styles
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 15)
  

#the start page of the GUI
def StartPage():
     
    #creates the window for the start page
    root=Tk()

    root.title('Main Window')
    
 
    
    global label1
    label1 = ttk.Label(root, text ="Select a Case", font = LARGEFONT)
      
    label1.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    #makes the font size of the open case button bigger
    s = ttk.Style()
    s.configure('my.TButton', font=('Verdana', 15))
    button1 = ttk.Button(root, text ="Open Case", width= 10, style='my.TButton',
    command = lambda : openCase())
 
    button1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky='ns',)
    
    
    global label2
    label2 = ttk.Label(root, text ="Process", font = MEDIUMFONT)
     
    label2.grid(row = 1, column = 2, padx = 10, pady = 10)
    
    global label3
    label3 = ttk.Label(root, text ="Display", font = MEDIUMFONT)
     
    label3.grid(row = 1, column = 3, padx = 10, pady = 10)
    
    
    global label4
    label4 = ttk.Label(root, text ="Zero", font = MEDIUMFONT)
     
    label4.grid(row = 2, column = 0, padx = 10, pady = 10)
    
    button2 = ttk.Button(root, text ="X",
    command = lambda : process())
 
    button2.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    button3 = ttk.Button(root, text ="X",
    command = lambda : display('Zero'))
 
    button3.grid(row = 2, column = 3, padx = 10, pady = 10)
    
    
    global label5
    label5 = ttk.Label(root, text ="Calibration", font = MEDIUMFONT)
     
    label5.grid(row = 3, column = 0, padx = 10, pady = 10)
    
    button4 = ttk.Button(root, text ="X",
    command = lambda : process())
 
    button4.grid(row = 3, column = 2, padx = 10, pady = 10)
    
    button5 = ttk.Button(root, text ="X",
    command = lambda : display('Calibration'))
 
    button5.grid(row = 3, column = 3, padx = 10, pady = 10)
    
    
    global label6
    label6 = ttk.Label(root, text ="Baseline", font = MEDIUMFONT)
     
    label6.grid(row = 4, column = 0, padx = 10, pady = 10)
    
    button6 = ttk.Button(root, text ="X",
    command = lambda : process())
 
    button6.grid(row = 4, column = 2, padx = 10, pady = 10)
    
    button7 = ttk.Button(root, text ="X",
    command = lambda : display('Baseline'))
 
    button7.grid(row = 4, column = 3, padx = 10, pady = 10)
    
    
    
    global label7
    label7 = ttk.Label(root, text ="Stage 1", font = MEDIUMFONT)
     
    label7.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    button8 = ttk.Button(root, text ="X",
    command = lambda : process())
 
    button8.grid(row = 5, column = 2, padx = 10, pady = 10)
    
    button9 = ttk.Button(root, text ="X",
    command = lambda : display('Stage 1'))
 
    button9.grid(row = 5, column = 3, padx = 10, pady = 10)
    
    
    global label8
    label8 = ttk.Label(root, text ="Stage 2", font = MEDIUMFONT)
     
    label8.grid(row = 6, column = 0, padx = 10, pady = 10)
    
    button10 = ttk.Button(root, text ="X",
    command = lambda : process())
 
    button10.grid(row = 6, column = 2, padx = 10, pady = 10)
    
    button11 = ttk.Button(root, text ="X",
    command = lambda : display('Stage 2'))
 
    button11.grid(row = 6, column = 3, padx = 10, pady = 10)
    
    
    #Complete column
    label9 = ttk.Label(root, text ="Labview", font = MEDIUMFONT)
    label9.grid(row = 1, column = 1, padx = 10, pady = 40) #increased pady so open case button could be bigger
    
    global label10
    label10 = ttk.Label(root, text ="-", font = MEDIUMFONT)
    label10.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    global label11
    label11 = ttk.Label(root, text ="-", font = MEDIUMFONT)
    label11.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    global label12
    label12 = ttk.Label(root, text ="-", font = MEDIUMFONT)
    label12.grid(row = 4, column = 1, padx = 10, pady = 10)
    
    global label13
    label13 = ttk.Label(root, text ="-", font = MEDIUMFONT)
    label13.grid(row = 5, column = 1, padx = 10, pady = 10)
    
    global label14
    label14 = ttk.Label(root, text ="-", font = MEDIUMFONT)
    label14.grid(row = 6, column = 1, padx = 10, pady = 10)
    
    root.mainloop()
    
    
    
    

def openCase():
    '''
    This function opens the file explorer and lets the user select a case file for analysis. Once the file is selected,
    CASE_SELECTED = True and the filepath is recorded.

    Returns
    -------
    None.

    '''
    
    global fp  #make fp global so display method can access
    #########################################################################################################
    #NOTE: THE FILE PATHS MIGHT NEED TO BE CHANGED ON A DIFFERENT COMPUTER
    #########################################################################################################
    fp = askopenfilename(initialdir = "C:\\Mount Sinai\\Final\\gui\\User Folder\\") # show an "Open" dialog box and return the path to the selected file
    case = pd.read_csv(fp, names=['Stage', 'Labview', 'Postprocessing', 'Process_Display'])
    process_display = case.loc[1:, "Process_Display"].to_numpy() # list of str that contains LabVIEW completion info from case file
    # changes the display of the gui to show the LabVIEW completion if a case was selected
    if (fp != ''):
        global CASE_SELECTED
        CASE_SELECTED = True
    changeDisplay(fp, process_display)


def changeDisplay(fp, process_display):
    '''
    Updates the StartPage widgets to display information from the selected case

    Parameters
    ----------
    fp : str
        the file path of the case file that was selected.
    process_display : numpy.ndarray of str
        Array that contains either Complete or Incomplete which shows if the labview analysis is complete for each stage.

    Returns
    -------
    None.

    '''
    # splices fp to get the name of the case file to display to the user
    filename = os.path.basename(fp).split('.')
    filename = str(filename[0])
    title = str('File Selected:' + filename)
    label1.config(text = title)
    stages = ['Zero', 'Calibration', 'Baseline', 'Stage 1', 'Stage 2']
    
    # loops through all labels in the LabVIEW column and changes them to their status from 
    # process_display at their respected indices
    for i in range(5):
        updateDisplay = 'label' + str(10 + i) + '.config(text = process_display[i])'
        exec(updateDisplay)
             
def process():
    '''
    Dummy page for when a process button is clicked   *Add more to it later

    Returns
    -------
    None.

    '''
    if CASE_SELECTED:
        DisplayPage('Process')
    else:
        print("Select a case file")
        openCase()
        
        
def display(phase):
    '''
    Displays a second window or figure depending on the phase

    Parameters
    ----------
    phase : str
        the phase of the analysis.

    Returns
    -------
    None.

    '''
    if CASE_SELECTED:
        filename = os.path.basename(fp).split('.')
        filename = str(filename[0])
        #########################################################################################################
        #NOTE: THE FILE PATHS MIGHT NEED TO BE CHANGED ON A DIFFERENT COMPUTER
        #########################################################################################################
        #if phase is 'Zero' a figure will be displayed of the zeros from the file explorer
        if phase == 'Zero':
            display = str("C:\\Mount Sinai\\Final\\Analysis 1 uz\\" +filename+ "\\figures " +filename+"\\" +filename+ "_6.png")
            os.startfile(display)
        #if phase is 'Calibration' a figure will be displayed of the calibration
        elif phase =='Calibration':
            display = str("C:\\Mount Sinai\\Final\\Analysis 1 uz\\" +filename+ "\\figures " +filename+"\\" +filename+ "_7.png")
            os.startfile(display)
        #if else a new page will be displayed instead
        else:
            DisplayPage(phase)
            
    else:
        print('Select a case file')
        openCase()
  

    
    

          



  
# second window frame page1
def DisplayPage(phase):
    '''
    Dummy page for when a display page is clicked

    Parameters
    ----------
    phase : str
        the phase of the analysis.

    Returns
    -------
    None.

    '''
    dp=Tk()

    dp.title(phase)
    
    
    # creating a container that stores the graphs in one row
    container = ttk.Frame(dp) 
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    
    # creating a container that stores the table in one row
    table_frame = ttk.Frame(dp)
    
    #The new graph button creates a new graph when it is clicked
    buttonGraph = ttk.Button(dp, text = 'New Graph',
                         command = lambda: placeHolderGraph(list(range(0,10,1)), random.sample(range(0, 10), 10), 0, container, phase))
    buttonGraph.grid(row = 2, column = 0)

    #creates three randomly generated graphs and places them in the container
    graph1 = placeHolderGraph(list(range(0,10,1)), random.sample(range(0, 10), 10), 0, container, phase)
    graph2 = placeHolderGraph(list(range(0,10,1)), random.sample(range(0, 10), 10), 1, container, phase)
    graph3 = placeHolderGraph(list(range(0,10,1)), random.sample(range(0, 10), 10), 2, container, phase)
    container.grid(row = 0, column = 0)

    #create the table
    table = placeHolderTable(4,20,table_frame)
    table_frame.grid(row = 1, column = 0)
    
    
def placeHolderGraph(x, y, position, window, phase):
    '''
    Parameters
    ----------
    x : list
        list of the x values that will be plotted.
    y : list
        list of the y values that will be plotted.
    position : int
        an integer that determines the postion of the graph in the GUI. 0 is the most left position, ints that are greater will be placed to the right.
    window : Tk()
        the window that the graph will be drawn on.
    phase : str
        phase that is being displayed

    Returns
    -------
    None.

    '''
    fig = plt.Figure(figsize=(5,4), dpi=100)
    
    
    a = fig.add_subplot(111)
    a.plot(x, y, color = 'k')
    a.set_title(phase + ' Graph ' + str(position + 1))
    
    
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.LEFT)
  

def placeHolderTable(rows, columns, window):
    '''
    Creates a table with number of rows and columns that is specified in the arguments

    Parameters
    ----------
    rows : int
        number of rows.
    columns : int
        number of columns.
    window : ttk.Frame
        the frame the table will be in.

    Returns
    -------
    None.

    '''
    for i in range(rows):
        for j in range(columns):
               
            e = tk.Entry(window, width=7, 
                             font=('Arial',16,'bold'))
               
            e.grid(row=i+1, column=j)
            e.insert(tk.END, 0)
    
  


        



# Driver Code
#opens the first page when the code is run
app = StartPage()
