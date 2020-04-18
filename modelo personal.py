#constantes
c=30 #tiempo de comida
#variables
entre=[] #array de suma de entretenimiento
#variables de contador
e=0 #entretenimiento
uc=0 #cantidad de comida
#entradas
t=int(input('Tiempo de actividad en horas: '))
ti=int(input('Hora de incio de trabajo hrs: '))
x=int(input('Cantidad de entreteniminetos realiza: '))
#preguntar todas cabtidad de entretenimeinto
for i in range(x):
    xn=int(input('Timepo asignado a la actividad '+str(i+1)+': '))
    entre.append(xn)
d=int(input('Tiempo en descanso en minutos: '))
#calcular la cantidad de comida
horas=ti+t
for i in range(t+1):
    h=ti+i
    if(h==8 or h==12 or h==19):
        uc+=1
print(uc)
#sumar entretenimiento
for i in range(0,len(entre)):
    e+=entre[i]

r=e+d+c*uc
to=r/(t*60)
rt=1-to

if rt>0.77:
    print('Esta utilizando el tiempo adecuado de actividades')
    print('Timepo de inactividad del trabajo: ', r,' minutos')
    print('Timepo de inactividad del trabajo ', to*100, '%')
    print('Timepo de actividad del trabajo', rt*100, '%')
else:
    print('Esta utilizando más tiempo en otras actividades')
    print('Timepo de inactividad del trabajo: ', r,' minutos')
    print('Timepo de inactividad del trabajo ', to*100, '%')
    print('Timepo de actividad del trabajo', rt*100, '%')    