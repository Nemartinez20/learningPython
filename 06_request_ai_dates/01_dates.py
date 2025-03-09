# Trabajando confechas y horas en python

# 1. importar modulos para trabajar con fechas
from datetime import datetime, timedelta

# importar lenguaje de fechas
import locale
locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')


#2 Obtener fecha y hora actual

now = datetime.now()
print(f'fecha y hora actual: {now}')

# 3. Para crear una fecha especifica
especific_date = datetime(1996,5,12,14,30,20)
print(f'fecha y hora especifica: {especific_date}')


year1 = now - especific_date;
print(f'tienes: {year1} años')

#4. Formatear fechas
# Metodo strftime() para formatear fechas
# pasarle el objeto datetime y el objeto espesificado
# Formato:
formato_especificado = now.strftime('%A %B %Y %H:%M:%S')
print(f'Fecha formateada: {formato_especificado}')


# 5. Operaciones con fechas (sumar/restar dias, minutos, horas , meses)
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)

one_hour_after =  datetime.now() + timedelta(hours=1)
print(f'One hour after: {one_hour_after}')

# 6. obtener los componentes individuales  ed una fecha

year = now.year
print(f'año: {year}')


#7. Calcular la diferencia entre 2 fechas

date1 = datetime.now()
date2 = datetime(1996,5,12)
print(f'diferencia: {(date1- date2)/365}')

