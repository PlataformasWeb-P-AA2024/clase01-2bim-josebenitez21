from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import datetime
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
clubs = session.query(Club).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Clubs")
for s in clubs:
    print("---------")
    print("%s" % (s))
    print("Anios de vida: %d" % (s.obtener_anios_vida()))
    print("Dorsales:%s" %(s.obtener_dorsales_jugadores()))
    print("Dorsales:%s" %(s.obtener_suma_dorsales))
 #   for i in s.jugadores:
 #       print("Dorsales: %s" %(i.obtener_dorsal_jugador()))

   # print("---------")
   # 


