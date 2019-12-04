# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Tic Tac Toe game

from random import randint 
# Pick Player names
def player_names():
    playera=input("Player A Name: ")
    playerb=input("Player B Name: ")
    return [playera,playerb] 
# Pick Player Order 
def toss_up(*args):
    first_player=''
    Second_player=''
    r=randint(0,1)
    t_A=int(input("Pick either 0 or 1: "))
        
    while abs(t_A) > 1:
        print ("Invalid Input")
        t_A=int(input("Pick either 0 or 1: "))
        
    if t_A == r:
        print("{} goes first and plays X".format (names[0]))
        first_player=names[0]
        Second_player=names[1]

    else:
        print("{} goes first and plays X ".format(names[1]))
        first_player=names[1]
        Second_player=names[0]
    players=[ first_player,Second_player]
        
    return players

# Play the actual  game, i.e, by using a dictionary as the argument, and print out all the items (which is blank for now) to print the layout
def player_turns(**k): 
    
    print("| {} | {} | {} |\n------------- \n| {} | {} | {} |\n------------- \n| {} | {} | {} |" 
          .format(k['a1'],k['a2'],k['a3'],k['b1'],k['b2'],k['b3'],k['c1'],k['c2'],k['c3']))
    


locations={'a1':'','a2':'','a3':'','b1':'','b2':'','b3':'','c1':'','c2':'','c3':''}
names = player_names()
print(names)
player_order=toss_up(*names)
print("The Grid \n")
print("| a1 | a2 | a3 |\n------------- \n| b1 | b2 | b3 |\n------------- \n| c1 | c2 | c3 |" )
order = True 
Exit = False
for i in list(range(1,6)):
      valid_a = True
      valid_b = True
      if Exit:
          break
      while order:
          
          
          while valid_a: # ensures that the input is valid
              l =str(input("Next move location : "))
            
              if l != 'a1' and l != 'a2'and l != 'a3' and l != 'b1' and  l != 'b2' and l != 'b3'and l != 'c1' and l != 'c2' and l!='c3':
               print("Invalid Input")
              else:
               valid_a=False
            
          locations[l]='X' #inserts the X or O into the locations by rewriting the items in the dictionary
          player_turns(**locations)
          #The if statement below contains all the possibilities for someone to win 
          if locations['a1']==locations['a2']==locations['a3']=='X' or locations['b1']==locations['b2']==locations['b3']=='X' or locations['c1']==locations['c2']==locations['c3']=='X' or locations['a1']==locations['b2']==locations['c3']=='X' or locations['a3']==locations['b2']==locations['c1']=='X' or locations['a1']==locations['b1']==locations['c1']=='X' or locations['a2']==locations['b2']==locations['c2']=='X' or locations['a3']==locations['b3']==locations['c3']=='X': 
                  print("\n {} is the WINNER!!".format(player_order[0]))
                  Exit=True # Used to Exit the for loop after exiting this while loop
                  break #To exit the while
          
          if i ==5: #ensures that only 9 valid turns are played, because i is increased every 2 turns, so it will be 10 turns before we can exit the for loop naturally  
              print("It'S A TIE!, WE ALL WIN!")
              break   
          print("It's {}'s turn".format(player_order[1]))
          order = False # So we can immediately move on to the next while loop

          

      while not order:
          
          while valid_b:
              l =str(input("Next move location : "))
              if l != 'a1' and l != 'a2'and l != 'a3' and l != 'b1' and  l != 'b2' and l != 'b3'and l != 'c1' and l != 'c2' and l!='c3':
               print("Invalid Input")
              else:
               valid_b=False
          
          locations[l]='O'
          player_turns(**locations)
          
          if locations['a1']==locations['a2']==locations['a3']=='X' or locations['b1']==locations['b2']==locations['b3']=='X' or locations['c1']==locations['c2']==locations['c3']=='X' or locations['a1']==locations['b2']==locations['c3']=='X' or locations['a3']==locations['b2']==locations['c1']=='X'  or locations['a1']==locations['b1']==locations['c1']=='X' or locations['a2']==locations['b2']==locations['c2']=='X' or locations['a3']==locations['b3']==locations['c3']=='X': 
    
                  print("{} is the WINNER!!".format(player_order[0]))
                  Exit=True
                  break
          print("\n It's {}'s turn".format(player_order[0]))
          order = True
print("END OF GAME")
     
       
     
         
    
                   
    

