# SYSC 1005 A Fall 2017 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

def menu():
    """(none)-> none
    
    Opens a menu for the user to select images and apply filters
    to them.
    
    >>>menu()
    
    """
    
    done = False
    image = False
    
    while not done:
        print ("L)oad Image")
        print ("N)egative   G)rayscale   X)treme contrast   S)epia tint   E)dge detect")
        print ("Q)uit")
        
        command = input(": ")
        
        if command == "L":
            img = get_image()
            show(img)
            image = True
       
        elif command == "N":
            if image == True:
                negative(img)
                show(img)
            else:
                print ("No image loaded")
        
        elif command == "G":
            if image == True:
                weighted_grayscale(img)
                show(img)  
            else:
                print("No image loaded")
       
        elif command == "X":
            if image == True:
                extreme_contrast(img)
                show(img)   
            else:
                print("No image loaded")
        
        elif command == "S":
            if image == True:
                sepia_tint(img)
                show(img)   
            else:
                print("No image loaded")
       
        elif command == "E":
            if image == True:
                thershold = input("Thershold?: ")
                thershold = float (thershold)
                detect_edges_better(img,thershold)
                show(img) 
            else:
                print ("No image loaded")
       
        elif command == "Q":
            sys.exit("File Open cancelled, exiting program")
        
        else:
            print ("No such command")
            

# First part read by program
if __name__ == "__main__": 
    menu()

