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
# Filename:         question_2.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]




####################### Write your code here #######################

def is_prime(number):

    '''
    
    
        Write the function for checking prime number


    '''

# Input from the user
a=int(input("Enter a number: "))
flag=False
if(a>1):
    for i in range(2,a):
        if(a%1)==0:
            flag=True
            break
if flag==True:
    print(a,"is not a prime number")
else:
    print(a,"is a prime number")            
# Print whether the number is prime number or not


