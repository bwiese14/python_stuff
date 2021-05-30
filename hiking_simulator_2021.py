"""
File: adventure_game.py
Author: Ben Wiese

Purpose: Adventure game using if/else statements and loops.
"""
import time

print('Hiking Simulator 2021 \n')
time.sleep(4)
print('"DAAAAAAAAAD! How much looooonger do we have to climb this stupid hill?')
time.sleep(4)
print('My feet HURT. My back is SWEATY. And I WANT to go HOME!"' '\n')
time.sleep(4)
print('"Um well, Br... Ca... Sa...?....."')
time.sleep(4)
print('(I was never good with names. What\'s his name again?)' '\n' '1. Brian' '\n' '2. Casey'
'\n' '3. Sandra' '\n' '4. Anna')

kid = int(input('Enter kid (1-4): ' '\n'))

if kid == 1:
    kid = 'Brian'
elif kid == 2:
    kid = 'Casey'
elif kid == 3:
    kid = 'Sandra'
else:
    kid = 'Anna'
print(kid)

if kid == 'Brian' or kid == 'Casey':
    print(f' {kid}! My little rockstar, we\'re almost to the top of the hill, '
    'c\'mon I\'ll carry ya!' '\n')
    time.sleep(4)
    print(f'A few minutes pass and {kid} is sound asleep on his father\'s back' '\n')
    print(f'(Hmm... Wouldn\'t now be the perfect time to practice my rendition of "Despacito"?)')
    dad_type = int(input('(1. No, out of my head, satan)\n (2. Oh no, oh no (oh), hey yeah) '
    '\n' 'Make a selection (1-2): '))
    if dad_type == 1:
        print(f'(No I shouldn\'t wake {kid}, and I can just hum it instead)')
        time.sleep(3)
    else:
        print('"DES"')
        time.sleep(1)
        print('"PA"')
        time.sleep(1)
        print('"CITO"')
        time.sleep(1)
        print('"Quiero Taco Bell en mi cuerpo, ay bonito"')
        time.sleep(2)
        print('"Deja que te dime besos cuando mijo sueñecito"')
        time.sleep(2)
        print('"Para que tu accordion si no esta conmigo"')
        time.sleep(2)
        print('"DES"')
        time.sleep(1)
        print('"PA"')
        time.sleep(1)
        print('"CITOOOO')
        print('OOOOOOOO')
        time.sleep(2)
        print('OOOOOOOO')
        time.sleep(2)
        print('OOOOOOOO"')
        time.sleep(2)
        print('....."DAD! Why do you do THIS to ME? You don\'t ever do THIS to DAVID!"' '\n')
        time.sleep(5)

else:
    print('(Wait, I have a daughter?)' '\n')
    time.sleep(4)
    print('"Quiet, ' + kid + '. We still have to find dinner, some '
    'rabbit or something gotta be here."' '\n')
    time.sleep(4)
    print('"DAD! You know I have a pet rabbit at home. Why do you always say these '
    'things? It\'s like you WANT me to be miserable!"')
    time.sleep(6)

    dad_type = int(input('(1. Oh ' + kid + '! I\'m sorry...) \n(2. What did YOU just say to me? '
    'I never wanted a daughter...) \n Make a selection (1-2): '))

if dad_type == 1:
    dad_type = 'good'
else:
    dad_type = 'bad'

if dad_type == 'good' and kid == 'Sandra' or dad_type == 'good' and kid == 'Anna':
    print(f'Oh {kid}! I\'m sorry... Here, I\'ll carry you and we can sing "Despacito" together!')
    time.sleep(4)
    print('"DES"')
    time.sleep(1)
    print('"PA"')
    time.sleep(1)
    print('"CITO"')
    time.sleep(1)
    print('"Quiero Taco Bell en mi cuerpo, ay bonito"')
    time.sleep(2)
    print('"Deja que te dime besos cuando mijo sueñecito"')
    time.sleep(2)
    print('"Para que tu accordion si no esta conmigo"')
    time.sleep(2)
    print('"DES"')
    time.sleep(1)
    print('"PA"')
    time.sleep(1)
    print('"CITOOOO')
    print('OOOOOOOO')
    time.sleep(2)
    print('OOOOOOOO')
    time.sleep(2)
    print('OOOOOOOO"')
    time.sleep(2)
    print()

if dad_type == 'good':
    print('MT. CLEESE \n 14,433 FEET \n VIEW --------------->')
    print(f'"Oh wow {kid}, look at the view! You can see MT. IDLE and MT. CHAPMAN off to the north')
    time.sleep(4)
    print('And look at that, the sun is setting right by MT. JONES to the west"')
    time.sleep(4)
    print('"Wow, dad, I\'m glad you finally woke me up!')
    time.sleep(4)
    print('And noooow it\'s time for me to wake youuuu upppp"')
    time.sleep(2)
    print('~~~DES~~~~~~~~````PA``````~~~CITOOOOO~~~~')
    time.sleep(5)
    print(f'"Huh, {kid}, what was that?"')
    time.sleep(3)
    print(f'{kid} walks in from the other room. "EWWW DAD? You peed yourself again')
    time.sleep(3)
    print('Stop drinking so much water before you go into a Cheeto-coma on the couch watching Tennis"')
    time.sleep(3)
    print('"Gotta stay hydrated, baby!"')
    time.sleep(3)
    print('BEST ENDING')
else:
    print('"What did YOU just say to me? ')
    time.sleep(1)
    print('I never wanted you.')
    time.sleep(3)
    print('You know what? Let\'s just go home."')
    time.sleep(3)
    print('~~BUT~~')
    time.sleep(2)
    print('~~WE~~')
    time.sleep(2)
    print('~~ARE~~')
    time.sleep(2)
    print('~~HOME~~')
    time.sleep(5)
    print('"What?"')
    time.sleep(2)
    print('At this time, you recognize that you lost on the first level of the easiest year of '
    'Hiking Simulator.')
    time.sleep(5)
    print('Maybe you\'re not ready for kids')
    print('WORST ENDING')

stubborn = 0
rate = int(input('Please rate the Hiking Simulator 2021 tutorial from 0-5: '))

if rate == 5:
    print('Thank you, play again soon!')
else:
    print(str(rate) + '? That can\'t be right')
    while rate < 5:

        rate = int(input('Please rate the Hiking Simulator 2021 tutorial from 0-5: '))
        stubborn = stubborn + 1

        if rate == 5:
            print('Thank you, play again soon!')
        elif stubborn > 10:
            print('Ok, fine. I admit it. This game was a gimmick of a story with awkward time spacing')
            print('YOU WIN')
            break
        elif stubborn > 7:
            print('You\'re going to be here for a while. You can\'t win that easily')
        elif stubborn > 5:
            print('Yeah, how about you just press the number "5" and be done with it?')
        elif stubborn > 3:
            print('No, that\'s still not right. Try again')
        else:
            print('Whoops, I think you meant to give it a "5". No problem, Hiking Simulator 2021 '
            'deals with problems')

