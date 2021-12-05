from random import choice

num_prey=4
prey=range(0, num_prey)
x_max=100
y_max=100
x_prey=[]
y_prey=[]
for n in prey:
    x_prey.append(choice(range(0, x_max)))
    y_prey.append(choice(range(0, y_max)))
x_pred=[choice(range(0, x_max))]
y_pred=[choice(range(0, y_max))]
num_steps=1000
for step in range(0, num_steps):
    x_chge=choice([1, -1])
    y_chge=choice([1, -1])
    x=x_pred[-1] + x_chge
    y=y_pred[-1] + y_chge
    x_pred.append(x)
    y_pred.append(y)

for xpred in y_pred:
    if xpred in x_prey:
            with open('f_prob.txt', 'a') as a:
                a.write('1\n')
    else:
        with open('f_prob.txt', 'a') as a:
            a.write('0\n')
