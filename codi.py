uc=0
t=int(input('Tiempo de actividad en horas: '))
ti=int(input('Hora de incio de trabajo hrs: '))
horas=ti+t
for i in range(t+1):
    h=ti+i
    if(h==8 or h==12 or h==19):
        uc+=1
print(uc)