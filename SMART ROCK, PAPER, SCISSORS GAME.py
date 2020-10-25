#!/usr/bin/env python
# coding: utf-8

# In[46]:


''' EXPLANATON OF CODE: THIS IS A ROCK, PAPER, SCISSORS GAME WITH IN TURKISH. BASIC CODE, YES, BUT ITS SPECIAL QUALITY IS;
 YOU CAN ENTER YOUR MOVE HOW EVER YOU WANT IT. FOR EX: PAPER MEANS KAĞIT IN TURKISH AND THERE IS 128 WAY TO
 TYPE IT IN YOUR KEYBOARD, AND THIS PROGRAM ACCEPTS ALL OF THEM. THIS IS SAME FOR OTHERS TOO.
 
 ROCK --> TAŞ , PAPER --> KAĞIT , SCISSORS --> MAKAS
 
 SO LET'S START TO PLAY.
 

'''


print('Taş kağıt makas oyununa hoşgeldiniz.\nHareketinizi giriniz.\n')

user1_move = input('PLAYER 1 hareketinizi giriniz\n')

user1_move = list(user1_move.lower())


user2_move = input('PLAYER 2 hareketinizi giriniz\n')

user2_move = list(user2_move.lower())



t = list("taş".lower())

k = list("kağıt".lower())

m = list("makas".lower())

if user1_move[0] is t[0] and user1_move[1] is t[1]:
   if user2_move is k:
       print("PLAYER 2 KAZANDI!\n")
       
   elif user2_move[0] is t[0] and user2_move[1] is t[1]:
       print("BERABERE!\n") 
       
   else:
       print("PLAYER 1 KAZANDI!\n")
       
elif user1_move[0] is k[0] and user1_move[1] is k[1] and user1_move[-1] is k[-1]:
   if user2_move is m:
       print("PLAYER 2 KAZANDI!\n")
       
   elif user2_move[0] is k[0] and user2_move[1] is k[1] and user2_move[-1] is k[-1]:
       print("BERABERE!\n")
       
   else:
       print("PLAYER 1 KAZANDI!\n")
       
elif user1_move == m:
   if user2_move is t:
       print("PLAYER 2 KAZANDI!\n")
       
   elif user2_move == m:
       print("BERABERE!\n")
       
   else:
       print("PLAYER 1 KAZANDI!\n")
       

print("TEBRIKLER OYUN BITTI\n\n\n")
print("coded by Oğuzhan Şanlıtürk\n")
print("for my linkedin click https://www.linkedin.com/in/oguzhanlt\n")

