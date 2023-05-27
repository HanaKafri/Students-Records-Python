# used to check if file exists
import os
from array import *
# used to open all files in the folder
import glob
# used for the plot
import matplotlib.pyplot as plt
2
class Course:
    def GetCourseInfo(self, nam, hour):
        self.__Cname = nam
        self.__hour = hour

    def printR(self):
        print(self.__Cname, ":", self.__hour)

    def getHours(self):
        return (self.__hour)

    def getCName(self):
        return (self.__Cname)

# data:
fileData = []
dataInAllFiles = []
semestersForEachFile = []
courses = []
semesterForAllFiles = []
grades = []
coursesTaken = []
remainCourses = []
semesterAvgG = []
hours = []
course = []

# temporary variables:
da = []
da1 = []
p = -1
temp = []
tempn = []

# works as counters:
numOfCouForFile = []
numOfLinesInFile = []
numOfCouForAllFiles = []
numOfHoursPerSemester = []
numOfHourForFiles = []

# get the data of courses 
# and add them to arrays of courses and hours using class inheritance
def get_courses():
    global courses
    global hours
    global course

    with open("E:\Hana uni\Projects Uni Y3S1\pythone_1190084_1192099\Code\Cources.txt",'r') as fileC:
        size =  sum(1 for _ in fileC)
    with open("E:\Hana uni\Projects Uni Y3S1\pythone_1190084_1192099\Code\Cources.txt",'r') as fileC:
        contentC = fileC.readlines()
    # get all coures with their hours
    for i in range(1, size):
        for wordsC in contentC[i].split('\n'):
            courses.append(wordsC.replace('\n', '').split(' '))
    
    # to delete the extra space at the begining
    a = len(courses) - 2
    while(a > 0):
        del(courses[a])
        a = a - 2

    # to add each course and its hour to an object (class inheretance)
    cours = Course()
    for i in range(0, len(courses)):
        # then add the course and hours to seperated arrays
        cours.GetCourseInfo(courses[i][0], courses[i][1])
        hour = cours.getHours()
        cour = cours.getCName()

        hours.append(hour)
        course.append(cour)


# to get the data of 1 file
def get_data(fileName):

    global p
    global fileData
    global da
    global semestersForEachFile
    global numOfCouForFile

    with open(fileName,'r') as file:
        size =  sum(1 for _ in file) # number of lines

    with open(fileName,'r') as file:
        content = file.readlines()

    # to read the file line by line, and split it
    for i in range(1, size):
        for words in content[i].split(';'):
            for word in words.split(','):
                # to count the number of courses in each semester
                p = p+1
                da.append(word.replace('\n', '').split(' '))
            # to delete extra space
            for l in range(1, len(da)):
                del(da[l][0])
        # array that has number of courses for each semester
        numOfCouForFile.append(p)
        p = -1

        #to add the first part of the line (semester) to semester array
        semestersForEachFile.append(da[0])
        del(da[0])

        #To add the courses and their hours to the array
        fileData.insert(i, da)

        da = []

# to get the data of all files
def get_All_data(fileName):
    global p
    global da1
    global semestersForEachFile 
    global numOfCouForFile
    global numOfLinesInFile
    global temp
    global dataInAllFiles
    global tempn
    global semesterForAllFiles
    semestersForEachFile = []
    d  = 0

    with open(fileName,'r') as file:
        size =  sum(1 for _ in file) # number of lines

    with open(fileName,'r') as file:
        content = file.readlines()

    for i in range(1, size):
        d = d + 1 # NUMBER OF LINES IN EACH FILE
        
        for words in content[i].split(';'):
            for word in words.split(','):
                p = p + 1
                da1.append(word.replace('\n', '').split(' '))
            for l in range(1, len(da1)):
                del(da1[l][0])
            
        semestersForEachFile.insert(i, da1[0])
        del(da1[0])
        
        # number of courses.
        tempn.append(p)
        p = -1
        # add the data of file in temp array
        temp.append(da1)
        da1 = []

    for t in range(0, len(semestersForEachFile)):
        del(semestersForEachFile[t][1])
    semesterForAllFiles.append(semestersForEachFile)
    semestersForEachFile = []
    # num of semesters
    numOfLinesInFile.append(d) 
    d = 0
    # add the data of temp array to another array, and empty temp, to get the data of all files in this array
    # this array contains array for each student, each student has array for each semester, each semester has array for all courses
    dataInAllFiles.append(temp)
    numOfCouForAllFiles.append(tempn)
    temp = []
    tempn = []

# USED IN:  Admin 1
def addNewStudent ():
    # here the program must ask to enter student ID.
    # The program must raise an error if the ID is not unique. 
    ID = input("Enter the student's ID : ")
    ###### check if ID number 
    result=all(i.isdigit() for i in ID)
    if result == False:
       print("erorr!, The ID must be a number")
    # to check if the file exists or not
    else:
      file = (ID + ".txt")
    # to check if the file exists or not
      if os.path.exists(file):
        raise FileExistsError('ID is not unique')
        # if it's found then it's not unique
      else:
        print("File created")
        new = open(file, "w")
        new.write("Year/Semester ; Course with grades\n")
        # create new file for that student

# USED IN: Admin 2
def addNewSemester():
    #here the program must ask 
    #to enter the required information (student ID, year/semester, courses and 
    # grades). The system must raise an error if there is missing information or the 
    # information in wrong format.
    global course
    get_courses()
    ID = input("Enter the student's ID : ")
    file = (ID + ".txt")
    
    # open the file
    if os.path.exists(file):
     f = open(file, "a") #append
     # e for error, if e = 0 error
     e = 1
     num_line=0
     N=True
     while(N==True):
      time = input("Enter year/semester : ")
      new_string = time.replace("-", "/")
      # save them in array after splitting
      list1 = new_string .split("/")
      # check if everything is digit
      result=all(i.isdigit() for i in list1)
      if result == False:
          # if the year/semester is not didit:
       print("erorr!")
       e=0
       break
    # if it is didgit
      else:
        # if there are not 3 digits in the list
       if len(list1) != 3:
          print("erorr") 
          e=0
          break
       else:
           # if the first year is not 4 digits
           if len(list1[0]) != 4 :
            print("erorr")
            e=0
            break
           else:
            # if the second year is not 4 digits
             if len (list1[1]) != 4:
               print("erorr!")
               e=0
               break
             else:
                # if the semester is 1 digits
               if len (list1[2]) < 2:
                 print("true input !")  
               else :
                print("erorr") 
                e=0
                break

      coursee = input("Enter each course with the grade with ',' between each course : ")
      t_course= (" " + coursee)
      # split and save each course in the array
      list2 = t_course .split(",")
      n=0
      lenlist2=len(list2)
      # to go through each course
      while lenlist2 > 0:
       sub_list2 = list2[0+n] .split(" ")
       for u in range(0, len(course)):
           # to check if the entered course is found in the courses file
         if(sub_list2[1] == course[u]):
             # e = 1 not error
            e=1
            # if it is found leave
            break
         else:
             continue
        # if course not found, error
       if(sub_list2[1] != course[u]):
        e=0
        # array must have 3 parts, if not, error
       if len(sub_list2) != 3:
        print ("error!")
        e=0
        break
       else:
           # if the first part is not "", then error
         if "" in sub_list2[0]==False :
            print ("error!!")
            e=0
            break
         else:
             # check if the 3rd part (grade) is all numbers
           result1=all(i.isdigit() for i in sub_list2[2])
           if result1 == False:
            print("erorr!!!")
            e=0
            break
           else:
            # the grade must not be more than 2 digits
             if len(sub_list2[2]) > 2:
                print("erorr!!!!")
                e=0
        # to go to the next course
       lenlist2=lenlist2-1
       n=n+1

    # if there is no error, write the new data on the file
      if(e != 0):
         fileDataa = (time + " ; " + coursee)
         f.write("\n")
         f.write(fileDataa)
         num_line=num_line+1

      ask= input("Do you want to add another year? please enter 1 if you want to add more:  ")
     
      if ask == '1':
        e=1
        N=True
      else:
         N=False  
         f.close()
         
      #with open(file, "r") as ext_file:
         #for line in ext_file:
           #fileDataa = line.split(',')
           #print(fileDataa)

    # if it's not found, error
    else:
        raise FileExistsError('ID not found')
        # create new file for that student


# Admin 3
def update():

    student_id = input("please enter the student id : ")
    result=all(i.isdigit() for i in  student_id )
    #student id must be digit
    if result == False:
      print("erorr! student id must be digit ")
      return
    else:
       file1 = (student_id  + ".txt")
       #to check if file exist
       if os.path.exists(file1):
          print("id found")
          course = input("please enter the name of the course to update: ")
          course = course.upper()  # make the letters capital
          grades = input(" please enter the new grade of this course: ")
          # grade must be number
          resl=all(i.isdigit() for i in  grades )

          if resl == False:
           print("erorr! grades must be digit ")
           return
          else:
              # grade must be less than 2 digits
              if len(grades)>2:
                 print("erorr! ")
                 return  

            # read courses from the courses file
              fo = open('Cources.txt', "r")

              content1 = fo.read()
              if course in content1:
                f = open(file1, "r")  
                content = f.read()
                I= course
                res =content.split(I, maxsplit=1)[-1]\
                         .split(maxsplit=1)[0]
                search_word = ","         
                if(search_word in res):
                  grades= (grades + ",")
                  content = content.replace(res, grades)
                else:
                 # Replace the target string
                
                 content = content.replace(res, grades)
                # Write the file out again
                with open(file1, 'w') as file:
                 file.write(content)          

                 print("TRUE!")

       else:
            print("not found")
            return


# USED IN: Admin 4 && Student 1
def hours_and_courses(filename, k):

    global numOfHoursPerSemester 
    global fileData
    global numOfHourForFiles
    global coursesTaken
    global remainCourses
    global semesterAvgG

    global course
    global hours

    dd = []
    sum = 0
    tempN = 0
    q = 0
    nn = []
    co = []
    rc = []
    coursesTaken= []
    ch = []
    gradeS = 0
    gradeSum = 0
    numl = 0

    for i in range(0,len(semestersForEachFile)):
        del(semestersForEachFile[i][1])

    # to get the courses he got
    for o in range(0, len(fileData)):
        #print(semestersForEachFile[o])
        for i in range(0,len(course)):
            for j in range(0,numOfCouForAllFiles[k][o]):
                if (fileData[o][j][0] == course[i]):
                    # o is number of students
                    # j is number of courses for each student
                    if(fileData[o][j][0] not in dd):
                        # to get the index of the taken courses
                        co.append(i)
                        # get the sum of the taken hours, for all semesters
                        sum = sum + int(hours[i])

                        # to not repeat the courses if they're repeated while getting the number of taken hours
                        dd.append(fileData[o][j][0])
                        
                        # to get the number of taken hours, for each semester
                        tempN = tempN + int(hours[i])

                        # to get the grade of each course (grade * hours of the course)
                        gradeS = int(hours[i]) * int(fileData[o][j][1])
                        gradeSum = gradeSum + gradeS

                        # to get the sum of the hours to use it in calculating the avg
                        numl = numl + int(hours[i])

                        break


        # finding the avg grades of each semester
        gradeAvg = gradeSum / numl
        numl=0
        gradeSum=0

        # to add the avg grades of a semester to an array
        ch.append(gradeAvg)
        
        # to add the number of taken hours for each semester alone in an array
        q = tempN
        tempN = 0
        nn.append(q)

        dd = []

    # to add the array of avg grades to another array, so each semester, and student will have a different index
    # this array will have the avg of each semester for each student
    semesterAvgG.append(ch)
    ch = []

    # to add the array of the index of taken courses in an another array, so each semester, and student has a different index 
    coursesTaken.append(co)
    co = []

    # to add the array of the number of taken hours in an another array, so each semester, and student has a different index
    numOfHoursPerSemester.append(nn)
    nn = []

    # to add the sum of taken hours to an another array, so each semester has a different index
    numOfHourForFiles.append(sum)
    sum = 0

    # empty the data of the file, to add the next file's data in it
    fileData = []
    dd = []

    # go throgh all courses, and check the courses that are not in coursesTaken which contains the indexes of taken courses
    # by checking the 2 indexes. if the index of a course is not in the array, then add it to an array which has all remaining courses for a student
    for i in range(0, len(course)):
        if i not in coursesTaken[0]:
            rc.append(course[i])
         
    # add the array that has the remaining courses to another array, so that each student has a different index.
    remainCourses.append(rc)
   


# USED IN: Admin 5 && Student 2
def overallAvg():
    AvgSum = 0
    AvgStudent = 0
    numberOfStudents = 0
    for i in range(0, len(grades)):
        AvgSum = AvgSum + grades[i]
        numberOfStudents = numberOfStudents + 1

    AvgStudent = AvgSum / numberOfStudents

    return AvgStudent



# USED IN: Admin 5 && Student 2
def avgHoursPerSemester():

    global semester
    allSemester = []
    m = 0
    sumPerSemester = 0
    sumPerS = []
    numberOfstudents = []
    avgHourPerSemester = []
    avgh = 0

    allSemester.append(semesterForAllFiles[0][0])

    # to get all semesters and add them in an array
    for i in range(0, len(semesterForAllFiles)):
        for j in range(0, len(numOfCouForAllFiles[i])):
            if(semesterForAllFiles[i][j] not in allSemester):
                allSemester.append(semesterForAllFiles[i][j])
                
    # to get the number of hours for each semester
    for l in range(0, len(allSemester)):
        # go throgh each semester in each file
        for i in range(0, len(semesterForAllFiles)):
            for j in range(0, len(numOfCouForAllFiles[i])):
                # get the hours for all similar semesters togather
                if (semesterForAllFiles[i][j] == allSemester[l]):
                    sumPerSemester = sumPerSemester + numOfHoursPerSemester[i][j]
                    m = m +1
        # add the number of hours for each semester to an array, and each semester will have a different index
        sumPerS.append(sumPerSemester)
        sumPerSemester = 0

        # get the number of students that studied in each semester and add them to an array
        numberOfstudents.append(m)
        m = 0

    # get the avg hours for each semester, and add it to an array
    for i in range(0, len(allSemester)):
        avgh = sumPerS[i] / numberOfstudents[i]
        avgHourPerSemester.append(avgh)
        avgh = 0
        print(allSemester[i], ": ", avgHourPerSemester[i])




# USED IN: Admin 4 & 5 & 6 && Student 1 & 2  
def get_grades():
    global fileData
    global grades

    grade = 0
    y = 0
    gavg = 0
    dd = []

    for i in range(0,len(dataInAllFiles)):
        for k in range(0,len(course)):
            for l in range(0, numOfLinesInFile[i]):
                for j in range(0, numOfCouForAllFiles[i][l]):
                    if (dataInAllFiles[i][l][j][0] == course[k]):
                        if(dataInAllFiles[i][l][j][0] not in dd):

                            dd.append(dataInAllFiles[i][l][j][0])
                            y = int(hours[k]) * int(dataInAllFiles[i][l][j][1])
                            grade = grade + int(y)
                            break
        dd = []       
        gavg = grade / numOfHourForFiles[i]
        grades.append(gavg)
        grade = 0
        y = 0




print('LOGIN as:')
print('1. Admin')
print('2. Student')
user = input('Choose a number \n')

get_courses()

if(user == '1'): #Admin
    print('1. Add a new record')
    print('2. Add a new semester with student course and grades')
    print('3. Update')
    print('4. Student statistics')
    print('5. Global statistics')
    print('6. Search')

    funcA = input('choose from the list. \n')


    #1. Add a new record
    if(funcA == '1'):

        addNewStudent()
        


    #2. Add a new semester
    elif(funcA == '2'):
        # Add a new semester with student course and grades

        addNewSemester()



    #3. Update
    elif(funcA == '3'):
        # here the system must ask for student ID and the name of the course to 
        #be change and the new grade

        update()




    #4. Student statistics
    elif(funcA == '4'):
        # first the program must ask for student ID. The program will print information such as 
        # number of taken hours, remaining courses, average per semester, overall average

        file = []
        o = 0
        number_of_file = 0
        # to get through all files in the folder
        for filename in glob.glob('*.txt'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in read only mode
                # to not read Courses, because it's not a student file
                if (filename != "Cources.txt"):
                    text = f.read()

                    # to add all files in an array
                    file.append(filename.replace('.txt', '')) # to add the name of the file to the array, without .txt, to be the ID of the student
                    number_of_file = number_of_file + 1

                    get_All_data(filename)
                    get_data(filename)

                    hours_and_courses(filename, o)
                    
                    o = o + 1

        get_grades()
        ID = input("Enter Student's ID: ")
        fileName = ID + ".txt"
        print(fileName)

        # check if the file exists
        if os.path.exists(fileName):
            # for all parts:
            # search for the file and get its data from the arrays that have the information of all files and print it

            print("Numbers of taken hours")
            for i in range(0, len(file)):
                if (ID == file[i]):
                    print(numOfHourForFiles[i])

            print("Remaining courses: ")
            for i in range(0, len(file)):
                for j in range(0, len(remainCourses[i])):
                    if (ID == file[i]):
                        print(remainCourses[i][j])
            
            print('Average per semester: ')
            for i in range(0, len(file)):
                for j in range(0, len(semesterAvgG[i])):
                    if (ID == file[i]):
                        print(semesterForAllFiles[i][j], " :", semesterAvgG[i][j])

            print('Overall avg: ')
            for i in range(0, len(file)):
                if (ID == file[i]):
                    print(grades[i])

        else:
            raise FileExistsError('ID not found')



    #5. Global statistics
    elif(funcA == '5'):
        #here the program must print information regarding all student 
        # such as overall students average, average hours per semester, plot the 
        # distribution of their grades (histogram)

        file = []
        o = 0
        number_of_file = 0
         # to get read all files in teh folder
        for filename in glob.glob('*.txt'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
                if (filename != "Cources.txt"):
                    text = f.read()
                    file.append(filename.replace('.txt', '')) # to add the name of the file to the array, without .txt, to be the ID of the student
                    number_of_file = number_of_file + 1
                    get_All_data(filename)
                    get_data(filename)

                    hours_and_courses(filename, o)
                    o = o + 1

        print('Overall Student avg: ')

        get_grades()
        print(overallAvg())
            
        print(end = "\n")

        print("Average hours per semester: ")
        avgHoursPerSemester()
       
        plt.hist(grades)
        plt.show()




    #6. Search
    elif(funcA == '6'):
    # here the system must retrieve the ID of the students that satisfy the 
    # given criteria. Here you can search for the following: 
    # based on average, taken hours

        file = []
        o = 0
         # to get read all files in teh folder
        for filename in glob.glob('*.txt'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            # do your stuff
                if (filename != "Cources.txt"):
                    text = f.read()
                    get_All_data(filename)
                    get_data(filename)
                    file.append(filename.replace('.txt', '')) # to add the name of the file to the array, without .txt, to be the ID of the student
    
                    hours_and_courses(filename, o)
                    o = o + 1

        print("1. search depending on taken hours")
        print("2. Search depending on average")
        depend = input("choose a number: ")

        f = 1
        n = 0
        # search depending on taken hours:
        if (depend == '1'):
            print("Number of hours for each student: ", numOfHourForFiles)

            searchHour = input("Enter number of hours: ")

            print("1. Less than: ")
            print("2. Greater than ")
            print("3. Equal ")
            print("4. Less than or equal: ")
            print("5. greater than or equal: ")
            way = input("Choose a number: ")

            if(way == '1'):
                for i in range(0, len(numOfHourForFiles)):
                    if(numOfHourForFiles[i] < int(searchHour)):
                        print(file[i], ": ", numOfHourForFiles[i])
                        n = n + 1
                if(n == 0):
                    f = 0
                    
            elif(way == '2'):
                for i in range(0, len(numOfHourForFiles)):
                    if(numOfHourForFiles[i] > int(searchHour)):
                        print(file[i], ": ", numOfHourForFiles[i])
                        n = n + 1
                if(n == 0):
                    f = 0

            elif(way == '3'):
                for i in range(0, len(numOfHourForFiles)):
                    if(numOfHourForFiles[i] == int(searchHour)):
                        print("yes")
                        print(file[i], ": ", numOfHourForFiles[i])
                        n = n + 1
                if(n == 0):
                    f = 0
            
            elif(way == '4'):
                for i in range(0, len(numOfHourForFiles)):
                    if(numOfHourForFiles[i] <= int(searchHour)):
                        print(file[i], ": ", numOfHourForFiles[i])
                        n = n + 1
                if(n == 0):
                    f = 0

            elif(way == '5'):
                for i in range(0, len(numOfHourForFiles)):
                    if(numOfHourForFiles[i] >= int(searchHour)):
                        print(file[i], ": ", numOfHourForFiles[i])
                        n = n + 1
                if(n == 0):
                    f = 0
            
            else:
                print("Please choose a number from the list")

            if (f == 0):
                print("Not Found")


        # search depending on avg
        elif(depend == '2'):
            get_grades()
            print("Avgerage grade for each student: ", grades)

            searchAvg = input("Enter a number: ")

            print("1. Less than: ")
            print("2. Greater than ")
            print("3. Equal ")
            print("4. Less than or equal: ")
            print("5. greater than or equal: ")
            way = input("Choose a number: ")

            if(way == '1'):
                for i in range(0, len(grades)):
                    if(grades[i] < int(searchAvg)):
                        print(file[i], ": ", grades[i])
                        n = n + 1
                if(n == 0):
                    f = 0

            elif(way == '2'):
                for i in range(0, len(grades)):
                    if(grades[i] > int(searchAvg)):
                        print(file[i], ": ", grades[i])
                        n = n + 1
                if(n == 0):
                    f = 0

            elif(way == '3'):
                for i in range(0, len(grades)):
                    if(grades[i] == int(searchAvg)):
                        print(file[i], ": ", grades[i])
                        n = n + 1
                if(n == 0):
                    f = 0
            
            elif(way == '4'):
                for i in range(0, len(grades)):
                    if(grades[i] <= int(searchAvg)):
                        print(file[i], ": ", grades[i])
                        n = n + 1
                if(n == 0):
                    f = 0

            elif(way == '5'):
                for i in range(0, len(grades)):
                    if(grades[i] >= int(searchAvg)):
                        print(file[i], ": ", grades[i])
                        n = n + 1
                if(n == 0):
                    f = 0
            
            else:
                print("Please choose a number from the list")

            if (f == 0):
                print("Not Found")

        else:
            print("Please choose a number from the list")





elif(user == '2'): #Student

    get_courses()
    ID = input("Enter Student's ID: ")
    fileName = ID + ".txt"
    print(fileName)

    if os.path.exists(fileName):

        print('1. Student statistics')
        print('2. Global statistics')

        funcS = input('choose from the list')


        #1. Student statistics
        if(funcS == '1'):
            #here the program must print information such as number of 
            #taken hours, remaining courses, average per semester, overall average
            
            file = []
            o = 0
            number_of_file = 0
            # to get through all files in the folder and read it
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in read only mode
                    # to not read Courses, because it's not a student file
                    if (filename != "Cources.txt"):
                        text = f.read()

                        # to add all files in an array
                        file.append(filename.replace('.txt', '')) # to add the name of the file to the array, without .txt, to be the ID of the student
                        number_of_file = number_of_file + 1

                        get_All_data(filename)
                        
                        get_data(filename)

                        hours_and_courses(filename, o)
                        o = o + 1

            get_grades()

            # for all parts:
            # search for the file and get its data from the arrays that have the information of all files and print it

            print("numbers of taken hours")
            for i in range(0, len(file)):
                if (ID == file[i]):
                    print(numOfHourForFiles[i])

            print("Remaining courses: ")
            for i in range(0, len(file)):
                for j in range(0, len(remainCourses[i])):
                    if (ID == file[i]):
                        print(remainCourses[i][j])
            
            print('Average per semester: ')
            for i in range(0, len(file)):
                for j in range(0, len(semesterAvgG[i])):
                    if (ID == file[i]):
                        print(semesterForAllFiles[i][j], " :", semesterAvgG[i][j])

            print('Overall avg: ')
            for i in range(0, len(file)):
                if (ID == file[i]):
                    print(grades[i])
    

        #2. Global statistics
        elif(funcS == '2'):
            #here the program must print information regarding all student 
            # such as overall average, average hours per semester, 
            # plot the distribution of their grades

            file = []
            o = 0
            number_of_file = 0

            # to read all files in the folder, and get their data
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
                    if (filename != "Cources.txt"):
                        text = f.read()
                        file.append(filename.replace('.txt', '')) # to add the name of the file to the array, without .txt, to be the ID of the student
                        number_of_file = number_of_file + 1
                        get_All_data(filename)
                        get_data(filename)

                        hours_and_courses(filename, o)
                        o = o + 1

            print('Overall Student avg: ')
            get_grades()
            print(overallAvg())
        
            print(end = "\n")
                
            print("Average hours per semester: ")
            avgHoursPerSemester()

    else:
        raise FileExistsError('ID not found')
