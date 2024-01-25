# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


import random 
print ("Katrīnas Lauras Terentjevas cirka spēlē")
round_position=1
player1_position=1 #parāda spēlētājusākuma poziciju
player2_position=1 #parāda spēlētāja sākuma poziciju
print("Spiediet Enter lai spēlētu, vēlu veiksmi!")
while True: # strādās līdz break
     print ("player 1 atrodas pozicijā numur", player1_position)
     input ("player1 met kauliņu")
     player1_position = player1_position + random.randint(1, 6) #dabū jauno poziciju
     print ("player 1 atrodas pozicijā numur", player1_position) #pārbauda kurā pozicijā atrodas spēlētājs 1
     if (player1_position == 18): #novēro vai spēlētājs 1 kāps pa/nokāps no kāpnēm
          player1_position = 7
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 7")
     if (player1_position == 67):
          player1_position = 46
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 46")
     if (player1_position == 80):
          player1_position = 69
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 69")
     if (player1_position == 74):
          player1_position = 63
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 63")
     if (player1_position == 15):
          player1_position = 24
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 24")
     if (player1_position == 39):
          player1_position = 48
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 48")
     if (player1_position == 33):
          player1_position = 52
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 52")
     if (player1_position == 87):
          player1_position = 96
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 96")
     if (player1_position >=100): #pārbauda vai spēlētajs nr 1 uzvar
          print ("Apsveicam, jūs uzvarējāt spēli!!!")
          break #pārtrauc 
     print ("player 2 atrodas pozicijā numur", player2_position) #pārbauda kurā pozicijā atrodas spēlētājs 2
     input ("player2 met kauliņu")
     player2_position = player2_position + random.randint(1, 6) #dabū jauno poziciju
     print ("player 2 atrodas pozicijā numur", player2_position)
     if (player2_position == 18): #novēro vai spēlētājs 2 kāps pa/nokāps no kāpnēm
          player2_position = 7
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 7")
     if (player2_position == 67):
          player2_position = 46
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 46")
     if (player2_position == 80):
          player2_position = 69
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 69")
     if (player2_position == 74):
          player2_position = 63
          print ("jūs uzkāpāt uz zilām kapnēm, parvietojam jūs atpakaļ uz 63")
     if (player2_position == 15):
          player2_position = 24
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 24")
     if (player2_position == 39):
          player2_position = 48
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 48")
     if (player2_position == 33):
          player2_position = 52
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 52")
     if (player2_position == 87):
          player2_position = 96
          print ("jūs uzkāpāt uz sarkanajām kapnēm, parvietojam jūs uz augšu līdz 96")
     if (player2_position >=100): #pārbauda vai spēlētājs nr 2 uzvar
          print ("Apsveicam, jūs uzvarējāt spēli!!!")
          break 
     round_position = round_position + 1 #Dabū jauno round
     print("Raunds nr. ", round_position) #pārbauda kurš raunds ir
     if (round_position == 25):  #pārbauda vai beidzās 25 rounds
          print ("Spēle beidzās! cik žēl, bet neizķirts un to var skaitīt ka uzvaru abiem spēlētājiem!")
          break 

