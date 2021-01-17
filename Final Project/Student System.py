# -*- coding: utf-8 -*-

#This is a student graduation control system.
#This program gives the student a graduation certificate as "Graduate Certificate.txt".
#If you have taken less than 3 courses, you will remain in the class.
#You cannot take more than 5 courses.
#Admin user can add a student or course.

def readUserData(): #This function reads User data
    f= open("userData.txt", "r", encoding="utf-8-sig")
    dataList = [line.strip() for line in f]
    f.close()
    #print (dataList)
    return(dataList)

DataList= readUserData() #We have assigned user data

def readCourseData(): #This function reads Course data
    f= open("courseData.txt", "r", encoding="utf-8-sig")
    courseList = [line.strip() for line in f]
    f.close()
    #print (courseList)
    return(courseList)

CourseList = readCourseData() #We have assigned course data

def student(name): #This function is the student user interface
    f=True #The flag variable for the while loop
    while (f):
        try: 
            nbrCrs= int(input ("How many courses did you take this semester? ")) #"nbrCsr" mean is Number of taken courses 
            if(nbrCrs>5): 
                print("You cannot take more than 5 courses")
            else: f=False
        except ValueError:
            f=True
            print("Please Enter a Integer!")
    if (nbrCrs<3):
            print("You failed in class.")
            return
    else:
        file= open("Graduate Certificate.txt","w",encoding="utf-8-sig") #We creat a graduate certificate
        file.write("-----Graduate Certificate-----\n\n"+"Student Name & Surname: "+name+"\n") #write to the file
        selected=[] #Create a empty list for selected courses
        for j in range (nbrCrs):
            f=True #The flag variable for the while loop
            while (f): 
               try:
                   print (f"Choice your {j+1}. course: ")
                   for i in range (len(CourseList)): #Loop for Course selection menu
                       print(f"[{i+1}] {CourseList[i]}")
                   choice = (int(input("Please Do Your Choice: ")))-1 #Choice variable for course selection
                   if (searchCourse(choice)==0):continue #We checking the selected course is exist
                   s=False #A flag variable for checking if the selected course has been selected
                   try:
                       for k in range (len(selected)): 
                           if (CourseList[choice]==selected[k]): 
                               print("This course has already been selected") 
                               s=True
                               break
                       if(s):continue
                       else:
                           selected.append(CourseList[choice]) #If selected course is not selected before, we add this course to "selected" list
                           #print(selected)
                   except IndexError:
                       continue
                   #Entering grades and writing on graduation certificate
                   while(True):
                       midterm = int(input(f"Please Enter {searchCourse(choice)} Midterm: "))
                       if (midterm<0 or midterm>100): 
                           print("Please enter a value between 100 and 0")
                       else: 
                           file.write("\n{} Course;\n".format(searchCourse(choice)))
                           file.write("\nMidterm: {}".format(midterm))
                           break
                   while(True):
                       final = int(input(f"Please Enter {searchCourse(choice)} Final: "))
                       if (final<0 or final>100): 
                           print("Please enter a integer value between 100 and 0")
                       else: 
                           file.write("\nFinal: {}".format(final))
                           break
                   while(True):
                       project = int(input(f"Please Enter {searchCourse(choice)} Project: "))
                       if (project<0 or project>100): 
                           print("Please enter a value between 100 and 0")
                       else: 
                           file.write("\nProject: {}".format(project))
                           break
                   exams={ #A dictionary for holding the exam notes
                       "Midterm":midterm,
                       "Final":final,
                       "Project":project,
                       "Default":"Wrong Selection"
                       }
                   #Calculation, assignment and write on file of average graduation grade [grdAvg]
                   grdAvg= round((int(exams["Midterm"])*30/100)+(int(exams["Final"])*50/100)+(int(exams["Project"])*20/100),2)
                   if (grdAvg>90): grd= "AA" 
                   elif (grdAvg<=90 and grdAvg>70): grd= "BB"
                   elif (grdAvg<=70 and grdAvg>50): grd= "CC"
                   elif (grdAvg<=50 and grdAvg>30): grd= "DD"
                   elif (grdAvg<=30): grd= "FF"
                   print ("Your {} Grade: {} ({})".format(searchCourse(choice),grd,grdAvg))
                   file.write("\nGrade: {} ({})".format(grd,grdAvg))
                   if (grd=="FF"):
                       print("You failed")
                       file.write(" failed\n")
                   else:
                       print("Passed")
                       file.write(" Passed\n")
                   f=False
               except ValueError:
                   print("Please enter a integer value") 
                   try:
                       selected.remove(searchCourse(choice)) #If an error occurred during grade entry, the selected course will be deleted from the selected list.
                   except ValueError:
                       continue
                   except UnboundLocalError:
                       continue

def root(): #This function is the admin interface
    print("Welcome Sir")
    f=True #The flag variable for the while loop
    while(f):
        c=True #A flag variable for checking if already exist thing to be added
        print("[1] Add a Student\n[2] Add a Course\n[3] Exit")
        try:
            choice= int(input("Do Your Choice: ")) #Choice variable for menu selection
            if (choice==1): 
                newname= input("Please Enter New Student\'s name: ")
                for i in range (len(DataList)): #this loop checking for if already exist the student to be added
                    if (DataList[i]==newname): 
                        print("This student has already been added")
                        c=False
                        break
                if (c): #Adding the new student
                    f = open("userData.txt", "a",encoding="utf-8-sig") 
                    f.write("\n"+newname)   
                    f.close() 
                    print("Added")
            elif (choice==2):
                newcourse= input("Please Enter New Course\'s name: ")
                for i in range (len(CourseList)): #this loop checking for if already exist the course to be added
                    if (CourseList[i]==newcourse): 
                        print("This course has already been added")
                        c=False
                        break
                if (c): #Adding the new course
                    f = open("courseData.txt", "a",encoding="utf-8-sig")
                    f.write("\n"+newcourse)
                    f.close() 
                    print("Added")
            elif (choice==3):
                f=False
            else: print ("Wrong Selection")
        except ValueError:
            print("Your Selection Value is Not a Integer") 

def searchUser(name): #This function checks the user information entered
    for i in range (len(DataList)):
        if (name=="Admin"):
            return("Root")
        elif (name == DataList[i]):
            return(True)
    return(0)

def searchCourse(choice): #This function checks the course information entered
    try:
        for i in range (len(CourseList)):
            if (CourseList[choice]==CourseList[i]):
                return(CourseList[i])
    except IndexError:
        print("Wrong Selection")
        return(0)

def main(): #main function for input interface
    for i in range (3):
        name = input("Please Enter Your Name: ")
        if (searchUser(name)=="Root"): 
            root() 
            break 
        elif (searchUser(name)): 
            print ("Welcome "+ name) 
            student(name) 
            break 
        else: 
            print ("Wrong Name! You have {} right to try".format(3-(i+1)))

main()