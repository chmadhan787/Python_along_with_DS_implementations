import numpy as np

teams = ['CSK','MI','RCB','SRH','KKR','RR','LSG','PBKS','DC','GT']
teams_to_be_played = list(input('Enter the Teams to be played today : ').split('vs'))

def toss(teams):
    tosses = dict()
    i = 0
    while i<2:
        print(teams[i],end = ' ')
        selected_toss = input('toss selection -> ')
        if selected_toss in ['Heads','Tails','heads','tails','H','T','h','t'] and selected_toss not in tosses.values():
            tosses[teams[i]] = selected_toss
            i+=1
        else:
            print('Please enter a valid toss')
    won_team = np.random.choice(teams_to_be_played)
    return won_team

win = toss(teams_to_be_played)
print(win,' Won the Toss')

def innings(win):
    print(win,end = " selects : ")
    inn = input()
    if inn in ['1','2']:
        print(inn,'st innings\n',) if inn == 1 else print(inn,'nd innings')
    else:
        print('enter valid innings')
innings(win)



number_of_overs = 20
score = 0
test_count = 0
target = int(input('Target : '))
for over in range(number_of_overs):
    # ball = input('enter the score : ')
    ball_count = 0
    while ball_count <6:
        test_count+=1
        print(over,".",ball_count,end = ' ->score hit by batter ')
        hit_score = input('')
        print('score updated to : ',end = '')
        if hit_score == '6':
            score+=int(hit_score)
            print(score)
        elif hit_score == '4':
            score+=int(hit_score)
            print(score)
        elif hit_score == '3':
            score+=int(hit_score)
            print(score)
        elif hit_score == '2':
            score+=int(hit_score)
            print(score)
        elif hit_score == '1':
            score+=int(hit_score)
            print(score)
        elif hit_score == '0':
            score+=int(hit_score)
            print(score)
        elif hit_score == 'wd':
            score+=1
            print(score)
            continue
        elif hit_score == 'nb':
            score+=1
            print(score)
            continue
        else:
            print('score invalid')
        if score == target:
            print('target reached...')
            break
        ball_count+=1
        print(target-score,'in',120-test_count,'balls')
    print()
