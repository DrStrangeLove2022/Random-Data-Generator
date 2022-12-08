import arcpy
import random
from random import randrange
from random import randint
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2010 12:01 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/31/2020 11:59 PM', '%m/%d/%Y %I:%M %p')

# You can replace this with really anything you want. I did crime since I had a large dataset from the City of Chicago.
def random_crime():
    my_crimes = ['BATTERY', 'THEFT', 'NARCOTICS', 'ASSAULT', 'BURGLARY', 'ROBBERY', 'DECEPTIVE PRACTICE', 
                 'OTHER OFFENSE', 'CRIMINAL DAMAGE', 'WEAPONS VIOLATION', 'CRIMINAL TRESPASS', 'MOTOR VEHICLE THEFT', 
                 'SEX OFFENSE', 'INTERFERENCE WITH PUBLIC OFFICER', 'OFFENSE INVOLVING CHILDREN', 'PUBLIC PEACE VIOLATION', 
                 'PROSTITUTION', 'GAMBLING', 'CRIM SEXUAL ASSAULT', 'LIQUOR LAW VIOLATION', 'CRIMINAL SEXUAL ASSAULT', 
                 'ARSON', 'STALKING', 'KIDNAPPING', 'INTIMIDATION', 'CONCEALED CARRY LICENSE VIOLATION', 
                 'NON - CRIMINAL', 'HUMAN TRAFFICKING', 'OBSCENITY', 'PUBLIC INDECENCY', 'OTHER NARCOTIC VIOLATION', 
                 'NON-CRIMINAL', 'HOMICIDE', 'NON-CRIMINAL (SUBJECT SPECIFIED)', 'RITUALISM', 'DOMESTIC VIOLENCE']
    return random.choice(my_crimes)

# My end goal for this was to be able to bring it into ArcGIS Insights to simulate a large dataset.
# I wanted to simulate the precient that was making the arrest. Since the data is random, it isn't accurate to real world mesaurment.
# A potential solution would be to add the police areas of responsibility and then extrat that once the data is created.
def unit_generator():
    my_units = ['10th Esri Police', '11th Esri Police', '12th Esri Police', '13th Esri Police', '14th Esri Police']
    return random.choice(my_units)

# Like before this was just an added field to generate a random number so that I could build a offender, victim count.
def random_num():
    value = random.randint(1,10)
    return value
    
# Here is where you point to your geodatabase
outGDB = "C:\Chicago\Chicago Project.gdb"
# The name of the future class that will be created during this process
outName = "random_chicago_crime"
# This is the boundry that the point will be created. You don't have to have one, but if you want to focus on an area then you can point to it here.
conFC = "C:\Chicago\Chicago Project.gdb\City_of_Chicago_Limits"
# How many random data points you want created.
points = 300000
# This is the spaceing of the points, you can make it as large or small as you choose.
min_Distance = ".5 Inch"

arcpy.CreateRandomPoints_management(outGDB, outName, conFC, "", points, min_Distance)

arcpy.env.workspace = "C:\Chicago\Chicago Project.gdb"

crime = "crime"
date = "date"
unit = "unit"
offender = "offender"

arcpy.AddField_management(outName, crime, "TEXT")
arcpy.AddField_management(outName, date, "DATE")
arcpy.AddField_management(outName, unit, "TEXT")
arcpy.AddField_management(outName, offender, "DOUBLE")

with arcpy.da.UpdateCursor(outName, [crime, date, unit, offender])as cursor:
    for row in cursor:
        row[0] = random_crime()
        row[1] = random_date(d1, d2)
        row[2] = unit_generator()
        row[3] = random_num()
        cursor.updateRow(row)
