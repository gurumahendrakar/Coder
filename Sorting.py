
# # class Sort:
# #     def __call__(self, *args, **kwargs):
# #         print('Orginal List : {}'.format(args))
# #         def Sort(args):
# #             for integers in range(len(args)):
# #                 for intss in range(integers,len(args)):
# #                     if args[intss]<args[integers]:
# #                         args[integers],args[intss] = args[intss],args[integers]
                   
# #                 print(args)

                
# #             return args
# #         return Sort(*args)
        
# # Sorte = Sort()
# # print(Sorte([1,3,2,5,888,9999,3,2,1,4,9,5]))



# # items_greater = []
# # items_lower = []
# # a = [1,6,8,2,1]
# # def quick_sort(sequence):
# #     length = len(sequence)
# #     if length<=1:
# #         return sequence
# #     else:
# #         pivot = sequence.pop()

    

# #     for item in sequence:
# #         print(item)
# #         if item>pivot:
# #             items_greater.append(item)
# #         else:
# #             items_lower.append(item)
# #     return quick_sort(items_lower)+[pivot] + quick_sort(items_greater)
# # print(quick_sort(list((8,7,2,1,6,8,9))))


# # star_patter = 0 
# # while star_patter<8:
# #     colums_couting = 0 
# #     while colums_couting<star_patter+1:
# #         print("*"*(colums_couting+1))
# #         colums_couting+=1
# #     print()
# #     star_patter+=1 

# # from multiprocessing.sharedctypes import Value


# Times_Play = 0
# Computer_Points = 0 
# My_Points = 0
# over = True
# class Projects:
#     Access = False
#     while not Access:
#         Name = input("Please Enter The Name Only Alphabets) ").replace(" ","")
#         if Name.isalpha()and len(Name)>=4:
#             print("Thanks For Play : {0} ".format(Name.capitalize()))
#             Access = True
#         else:
#             print("          Cannot Play Type Name       ")
#             Name = input(" Please Enter The Name Only Alphabests ")
#     if Access:
#         class Games:
#             if __name__ == "__main__":
#                 import random
            
#             @staticmethod
#             def Choiceing_GameOvering():
#                 import random
#                 Computer = ["Rock","Paper","Sezeers"]
#                 random.shuffle(Computer)
#                 Computer = random.choice(Computer)
#                 print(      " Computer Is  : {} ".format(Computer))
                
#                 User = input("1:Rock\n2:Paper\n:3:Sezeer\t : ").capitalize()
#                 if type(User)==int or User not in ['Rock',"Paper","Sezeer"]:
#                     print("Invalid Try Again Brother")
#                     User = input("1:Rock\n2:Paper\n:3:Sezeer\t : ").capitalize()
                    
                
            
#                 if Projects.Games.Winner(Computer,User):
#                     print("        You Are The Win Brother         ")
#                     global Computer_Points
#                     global My_Points
#                     My_Points+=1 
                    
#                     if Projects.Games.Main_board():
#                         Projects.Games.GameBoard()

                
#                 else:
#                     Computer_Points+= 1
#                     if over:  
#                         if Projects.Games.Main_board():
#                             Projects.Games.GameBoard()

               
#             @staticmethod
#             def GameBoard():
#                 try:
#                     Game_Player_Board = int(input(" 1 : Rock_Paper -> \t"))
#                     if Game_Player_Board==1:
#                         Projects.Games.Choiceing_GameOvering()
            
#                     if Game_Player_Board>1:
#                         raise ValueError("Madarchod Rules Phadle:  1 : Rock_Paper  ")

#                 except Exception as e:
#                     print(e)
#                     Projects.Games.GameBoard()
                

#             @classmethod
#             def Winner(cls,Computer,User):
#                 print(" Computer Is : {} User Is : {} ".format(Computer,User))
#                 if Computer==User:
#                     print(" ITS DRAW BROTHER")
#                     if Projects.Games.Main_board():
#                         Projects.Games.GameBoard()
                
#                 if User=="Rock" and Computer=='Sezeers' or User=="Paper" and Computer=='Rock' or User=="Sezeer" and Computer=='Paper':
#                     return True

#             @classmethod
#             def Main_board(cls):
#                 global over
#                 Gameover = False
#                 while not Gameover:
#                     if  not Gameover:
#                         Player = int(input(" 1 : Yes   2: NO    : "))
#                     else:
#                         return False
#                     if Player==1:
#                         print("     Play Agained        ")  
#                         return True     
                    
#                     else:
#                         if Computer_Points>My_Points:
#                             Gameover = True
#                             over = False
#                             print("Computer Is Win Brother")
#                         elif Computer_Points==My_Points:
#                             print("Match Is Die Brother")
#                             Gameover = True
#                             over = False
#                         else:
#                             print(         "YOu Are The win Brother {0}      ".format(Projects.Name))
#                             Gameover = True
#                             over = False

        
        
        
# Gamess = Projects()
# Gamess.Games().GameBoard()

