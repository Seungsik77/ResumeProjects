import csv
from statistics import median
from math import isnan
from itertools import filterfalse
from statistics import mode
def total_hours(filename):#This function opens a file and adds all the values together
    stringsum = 0
    stringindex = 0
    with open(filename, 'r') as file:
            for lines in file:
                value = int(lines)
                stringsum += value
            return stringsum
    file.close()

if __name__ == '__main__':
    print(total_hours('employee1.txt')) #30
    print(total_hours('employee2.txt')) #22
    print(total_hours('employee3.txt')) #40




def label_days(filename):#This function appends the day of the week to each hour value
    weekday = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday",
    4:"Thursday", 5:"Friday", 6:"Saturday"}
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(lines)
        for i in range(len(lines)):
            lines[i] = weekday[i] +": "+ lines[i]

        with open('labeled_'+ filename, 'w') as fp_out:
            fp_out.writelines(lines)
        file.close()
if __name__ == '__main__':
    label_days('employee1.txt') 
    label_days('employee2.txt') 
    label_days('employee3.txt')




def stretch_model(fname_in, fname_out):#This function stretches the shape by 2 on the y axis
    try:
        with open(fname_in) as fp_in:
            vertices = 0
            lines = fp_in.read()
            lines = lines.split('\n')
        with open(fname_out, 'w') as fp_out:
            for i in range(len(lines)):
                if 'v' in lines[i]:
                    close = lines[i].split(' ')
                    close[2] = str(float(close[2])*2)
                    line = " ".join(close)
                    fp_out.write(line)
                    vertices += 1
                elif 'f' in lines[i]:
                    fp_out.write(line)

        return vertices
        file.close()
    except FileNotFoundError:
        return -1

if __name__ == '__main__':
    print(stretch_model('missing.obj', 'doesntmatter.obj')) #-1
    print(stretch_model('triforce.obj', 'triforce_stretched.obj')) #9
    print(stretch_model('teapot.obj', 'tall_teapot.obj')) #3644



def count_votes(district, office):
    winner = []
    votes = 0
    with open(district, 'r') as file:
        lines = file.readlines()
        district = district.split(',')
        
        major = ""
        for line in file:
            district.read()
            major = mode(line)
            votes += 1
            winner.append[major]
            winner.append[votes]
    return winner

if __name__ == '__main__':
    print()
    print(count_votes('district_0z.csv', 'Mayor'))
    #['Leslie Knope', 2]

    #print(count_votes('district_4b.csv', 'City Question 1'))
    #['YES', 10]

    #print(count_votes('district_60b.csv', 'County Commissioner District 4'))
    #['Angela Conley', 49]

