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

#Aleksandrs Ļinovs
player_location = 1
ai_location = 1
import random
def player_move():
    global player_location
    print("Your turn throw cube")
    metiens=input ()
    if metiens == "mest":
        kaulins = random.randint(1 , 6)
        print("Tu uzmetāt:", kaulins)
        player_location = player_location + kaulins
        if player_location == 18:
            player_location = 7
            print("Unlucky,you go to 7")
        elif player_location == 67:
            player_location = 46
            print("Unlucky,you go to 46")
        elif player_location == 74:
            player_location = 63
            print("Unlucky,you go to 63") 
        elif player_location == 80:
            player_location = 69
            print("Unlucky,you go to 69")
        
        elif player_location == 15:
            player_location = 24
            print("Ļucky,you go to 24")
        elif player_location == 39:
            player_location = 48
            print("Ļucky,you go to 48")
        elif player_location == 33:
            player_location = 52
            print("Ļucky,you go to 52")
        elif player_location == 87:
            player_location = 96
            print("Ļucky,you go to 96")
        else:
            print("Jus atrodaties uz ", player_location, ". lauciņa")
    else:
        print("mistake")
        
def ai_move():
    global ai_location
    print("opponent's attack")
    kaulins = random.randint(1 , 6)
    print("opponent uzmetāt:", kaulins)
    ai_location = ai_location + kaulins
    if ai_location == 18:
            ai_location = 7
            print("Unlucky ai, go to 7")
    elif ai_location == 67:
            ai_location = 46
            print("Unlucky ai, go to 46")
    elif ai_location == 74:
            ai_location = 63
            print("Unlucky ai, go to 63") 
    elif ai_location == 80:
            ai_location = 69
            print("Unlucky ai, go to 69")
        
    elif ai_location == 15:
            ai_location = 24
            print("Ļucky ai, go to 24")
    elif ai_location == 39:
            ai_location = 48
            print("Ļucky ai, go to 48")
    elif ai_location == 33:
            ai_location = 52
            print("Ļucky ai, go to 52")
    elif ai_location == 87:
            ai_location = 96
            print("Ļucky ai, go to 96")
    else:
            print("ai atrodaties uz ", ai_location, ". lauciņa")


