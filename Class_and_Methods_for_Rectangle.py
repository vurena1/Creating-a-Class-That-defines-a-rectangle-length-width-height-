import time
class Rectangle: # this is the main class we are using to define the entire code 
    
    def __init__(self, length, width): # here we aredefining the legnth and width of the rectangle 
        self.length = length # defining length which is equal to length
        self.width = width # defnining width which is equal to width 
    
    def Perimeter(self): # defining perimeter and giving the return value a perimeter function  
        return 2*(self.length + self.width)
    
    def Area(self): # then we are going to define area with itself and also giving it a function to return the value of area 
        return self.length*self.width

    def Display(self): # the display function is going to be used to display our values and functions throughout the class, all we have to do is call back that method Display() with the rectangle class length and width
        print("The length of the rectangle is:", length)
        print("The wwidth of the rectangle is:", width)
        print("The perimeter of the rectangle is:", self.Perimeter())# here we use empty () in order to call the function above because it is referrering to self 
        print("The area of the rectangle is:", self.Area()) # here we use empty () in order to call the function above because it is referrering to self 

class Parrallelpiped(Rectangle): # here we are making a class that will hold the value of the volume of the rectangle by inheriting rectangle in the class we will be calling back rectangle and what is in it, length and width 
    def __init__(self, length, width, height): # we area defning what is in parrallelpiped
        super().__init__(length, width) # here all we are doing is getting back the length and width of the original class from up top which will basically use the same legnth and width so it is all 1 rectangle, Super indicates return funciton to parent class 
        self.height = height # we set height is equal to hight so that we can use it above in the def __init__ of the parrallelpiped 
    def Volume(self): # we def volume now under parrallelpiped in order to use the function below which will return the volume of the rectangle 
        return self.length*self.width*self.height # here we return the function
    def ParrallelpipedVolumeDisplay(self):# here is decided to call another method which will pretty much display the parrallelpiped volume such as we did above with length, width, area, perimeter
        print("This is the height of the rectangle:", self.height) ### decided to add height to the display because it will make it easier to calculate the volume to verify code is working correctly 
        print("volume of the parrallelpiped is:", self.Volume()) # all we are doing is giving the method a value to print out what is says and then implementing self.Volume() which returns the volume equation 


length = float(input("Enter length:")) # HERE IS WHERE WE PROMPT THE USER TO ENTER A SET OF LENGTH WIDTH AND HEIGHT
width = float(input("Enter width:"))
height = float(input("Enter height:"))
parrallelpiped = Parrallelpiped(length, width, height) # here we are giving value to the method __init__ under class parrallelpiped which are the length, width and height 
parrallelpiped.ParrallelpipedVolumeDisplay()# here is how we insert the values of parrallelpiped which are length, width, height into the the last method which includes the volume which includes those length width height. 
parrallelpiped.Display() ## here we call the display function in order to display every thing from the display method 


time.sleep(10) # did some research and ended up adding this so that the code will take 10 seconds to close after it is excuted becuase it was closing instantly on my command prompt portal 


#### PLEASE EXCUSE MY MISUNDERSTANDING OF THE ASSIGNMENT AND CONSIDER THIS AS MY FINAL DRAFT I DID NOT READ THE ASSIGNMENT CCORRRECTLY BUT I DO KNOW HOW TO PERFORM THE FUNCTION  
