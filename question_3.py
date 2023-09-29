'''
*****************************************************************************************
*
*        		===============================================
*           		e-Yantra School Robotics Competition (eYSRC 2023)
*        		===============================================
*
*  This script is to be used to implement Mini Assignment titled- 'Drawing Maurer Rose using Turtle'.
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*  
*  e-Yantra - A MOE project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         question_3.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################
import math
##############################################################



####################### Write your code here #######################
import math
# Sample student data
student_data = {
    'Ram': [50,60,70,80,90],
    'Shaam': [60,70,65,90,80],
    'Rohan': [90,89,76,78,65],
    'Rahul': [45,34,43,34,54]
}

pass_threshold = 50 # Set the passing threshold here


# Calculate and print the average marks for each student
def checkifpass(pass_thresold, student_data):
    for key, val in student_data.items():
        total=sum(val)/len(val)
        if total > pass_threshold:
            print(key,"- PASS")
        else:
            print(key,"- FAIL")

checkifpass(pass_threshold, student_data)