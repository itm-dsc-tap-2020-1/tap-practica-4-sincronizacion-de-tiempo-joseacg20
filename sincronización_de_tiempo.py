import os
import ntplib
import datetime
from time import ctime
from time import strftime

print('\nHora de inicio de la petición')
t1 = datetime.datetime.now()
horaInicio = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]
print ('%s' % horaInicio)

servidor_de_tiempo = "0.europe.pool.ntp.org"
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.dest_time), "%a %b %d %H:%M:%S %Y")

print('Hora de llegada de la petición')
t2 = datetime.datetime.now()
horaFin = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]
print ('%s' % horaFin)

print("\n***** Obteniendo la hora del servidor NTP *****")
print("Respuesta del servidor " + servidor_de_tiempo +  ": " + str(hora_actual) + "\n")

print('Ajuste de Retraso')
ajuste = ((t2 - t1) / 2)
print(ajuste)

print ("\nFecha y Hora Actual del Equipo")
fechaHora = datetime.datetime.now()
print ("%s" % fechaHora)

print ("\nFecha y Hora del Servidor mas el Ajuste de Retraso")
horaConAjuste = hora_actual + ajuste
print (horaConAjuste)

print("\nAjustando tiempo del equipo")
horaActualizar = horaConAjuste.strftime('%m%d%H%M%Y %f')[:-6]
os.system('sudo date -u ' + horaActualizar)