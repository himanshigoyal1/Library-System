# def books():
#     print("Press 1 for 101 book details")
#     print("Press 2 for 102 book details")
#     print("Press 3 for 103 book details")
#     print("Press 4 for 104 book details")
#     a=int(input("Enter your choice:"))
#     if(a==1):
#      print("PYTHON")
#      print("Author name: Guido Van Rossum")
#      print("Price: ₹499")
#      print("Launch date= 1991")
#      print("Description: It is a interpreter based programming language book")
#      b=int(input("If you want to continue then press 1 otherwise press 2="))
#      if (b==1):
#         books()
#      else:
#         print("Thanks for visiting")
#     elif(a==2):
#      print("Programming in Java")
#      print("Author: James Gosling")
#      print("Price:₹599")
#      print("Launch Date: 1996")
#      print("Description:This comprehensive guide covers every aspect of Java, from basic syntax and semantics to advanced topics")
#      b=int(input("If you want to continue then Press 1 otherise Press 2="))
#      if (b==1):
#          books()
#      else:
#          print("Thanks for visiting") 
#     elif(a==3):
#      print("Programming in C")
#      print("Author name: Dennis Ritchie")
#      print("Price: ₹399")
#      print("Launch date: 1970")
#      print("Description: With clear explanations and a balanced approach, this book covers all the essential aspects of C programming.")
#      b=int(input("If you want to continue then Press 1 otherise Press 2="))
#      if(b==1):
#         books()
#      else:
#         print("Thanks for visiting")
#     elif(a==4):
#      print("Effective C++")
#      print("Author: Bjarne Stroustrup")
#      print("Price:₹699")
#      print("Launch date: 1985")
#      print("Description: This book provides 55 specific suggestions to help improve your programs and designs.")
#      b=int(input("If you want to continue then Press 1 otherwise Press 2="))
#      if (b==1):
#          books()
#      else:
#          print("Thanks for visiting")


# books()

#Project using functions with less time and space complexity:-


    
def One():
     print("PYTHON")
     print("Author name: Guido Van Rossum")
     print("Price: ₹499")
     print("Launch date= 1991")
     print("Description: It is a interpreter based programming language book")
     again()

        
def Two():
     print("Programming in Java")
     print("Author: James Gosling")
     print("Price:₹599")
     print("Launch Date: 1996")
     print("Description:This comprehensive guide covers every aspect of Java, from basic syntax and semantics to advanced topics")
     again()

def Three():
     print("Programming in C")
     print("Author name: Dennis Ritchie")
     print("Price: ₹399")
     print("Launch date: 1970")
     print("Description: With clear explanations and a balanced approach, this book covers all the essential aspects of C programming.")
     again()
        
def Four():
     print("Effective C++")
     print("Author: Bjarne Stroustrup")
     print("Price:₹699")
     print("Launch date: 1985")
     print("Description: This book provides 55 specific suggestions to help improve your programs and designs.")
     again()  
         



def again():
    b=int(input("If you want to continue then press 1 otherwise press 2="))
    if (b==1):
        books()
    else:
        print("Thanks for visiting")
        
def  books():
    print("Press 1 for 101 book info")
    print("Press 2 for 102 book info")
    print("Press 3 for 103 book info")
    print("Press 4 for 104 book info")
    a=int(input("Which book details do u want to access:"))
    if(a==1):
        One()
    elif(a==2):
        Two()
    elif(a==3):
        Three()
    elif(a==4):
        Four()


            
books()


    
            