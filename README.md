# Codigos echos en la UEA(materia) de Estructuras de Datos No Lineales en la Universidad Autónoma Metropolitana Unidad Cuajimalpa(UAM-C)
### //author: Christopher Xavier Sanchez Duran
### //UAMC



## Proyecto TORCSEn el achivo Drivers.py hay varios conductores implementados como clases. El método importante es el método “drive” el cual se invoca automáticamente desde el método “process” que está en el archivo Torcs.py cada que el cliente va a mandar al servidor la respuesta para controlar el auto.

Ahora, lo importante es que en la implementación del cliente de Python, la información que reciben del servidor (los valores de sensores) y la información que ustedes enviarán (valores actuadores) está guardada en un objeto de tipo Diccionario de Python. 

Es decir, el parámetro “sensors” que tiene el método “drive” es un diccionario (recomiendo buscar la clase dictionary en Python si no están familiarizados) que se ve más o menos así:
{'angle': [-0.0054],
 'trackPos': [-0.33],
 'track': [7.33, 7.57, 8.4, ..., 3.66],
 ...
 'gear': [2]}

Arriba puse una versión abreviada y con valores ficticios del diccionario porque en realidad tiene como 50 elementos (i.e., los sensores del auto descritos en el manual PDF de TORCS) y cada vez llegarán los valores reales de la carrera.

Recuerden que para obtener el campo de un diccionario, simplemente deben indexar con la clave de la entrada. También noten que el valor de cada entrada es una lista, aunque sea solamente un valor. Por ejemplo:

print("El auto está en la posición del ancho de la pista: ", sensors['trackPos'][0])

Lo cual imprimirá el mensaje mostrando "-0.33" al final. sensors['trackPos'] nos regresa el contenido del campo 'trackPos', y para acceder al 1er y único elemento de la lista usé el [0].

Importante: arriba del método “process” del archivo Torcs.py está un comentario que muestra todos los campos tanto del mensaje con los valores de los sensores (“income” dice en el código). Allí aparecen los nombres de los campos que tiene el diccionario sensors.

 


// author: Christopher Xavier Sanchez Duran
// Github: https://github.com/cxavier23
// Portafolio: https://cxavier23.github.io/


