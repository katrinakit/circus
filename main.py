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






print("katrīnas Lauras Terentjevas spēle cirks")
print("sākam spēli, vēlu veiksmi!")
print("player 1 met kauliņu, un iet uz priekšu")
import random 
x = (random.randint(1, 6))
print(x)
print("player 2 met kauliņu, un iet uz priekšu")
import random
q = (random.randint(1, 6)) 
print (q)
print("player 1 met kauliņu, un iet uz priekšu")
import random
y = (random.randint(1, 6))
print(y)
w = (x + y)
print("player 1 atrašanās vieta ir", w)
print("player 2 met kauliņu, un iet uz priekšu")
import random
e = (random.randint(1, 6))
print(e)
r = (q + e)
print("player 2 atrašanās vieta ir", r)
print("player 1 met kauliņu, un iet uz priekšu")
import random
t = (random.randint(1, 6))
print(t)
u = (t + w)
if u == 15:
     print("jūs ejat pa sarkanajām trepēm uz 24")
if not u == 15: 
     print ("player 1 atrašanās vita ir", u)
print("player 2 met kauliņu, un iet uz priekšu")
import random
i = (random.randint(1, 6))
print(i)
o = (i + r)
if o == 15:
     print("jūs ejat pa sarkanajām trepēm uz 24")
if not o == 15: 
     print ("player 2 atrašanās vita ir", o)
print("player 1 met kauliņu, un iet uz priekšu")
import random
p = (random.randint(1, 6))
print(p)
a = (u + p)
if a == 15:
     print("jūs ejat pa sarkanajām trepēm uz 24")
if a == 18:
     print("jūs ejat pa zilajām trepēm atpakaļ uz 7")
if not a == 15 or a == 18: 
     print ("player 1 atrašanās vieta ir", a)
     print("player 2 met kauliņu, un iet uz priekšu")
import random
s = (random.randint(1, 6))
print(s)
d = (o + s)
if d == 15:
     print("jūs ejat pa sarkanajām trepēm uz 24")
if d == 18:
     print("jūs ejat pa zilajām trepēm atpakaļ uz 7")
if not d == 15 or d == 18: 
     print ("player 2 atrašanās vieta ir", d)
     print("player 1 met kauliņu, un iet uz priekšu")
import random
f = (random.randint(1, 6))
print(f)
g = (a + f)
if g == 15:
     print("jūs ejat pa sarkanajām trepēm uz 24")
if g == 18:
     print("jūs ejat pa zilajām trepēm atpakaļ uz 7")
if not g == 15 or g == 18: 
     print ("player 1 atrašanās vieta ir", g)
     



