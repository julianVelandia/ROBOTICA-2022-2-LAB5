# Laboratorio 5.
## Robótica - Universidad Nacional De Colombia - Sede Bogotá.
### Sebastian Cubides - Julián Velandia.
***
### Cinemática inversa:

* Videos del Funcionamiento:

[![Alt text](https://img.youtube.com/vi/oTT9XLO5B0g/0.jpg)](https://www.youtube.com/watch?v=oTT9XLO5B0g)

Se realizó una descripción geométrica del robot como se ve en la siguiente imagen.


<img width="665" alt="image" src="https://user-images.githubusercontent.com/52173621/200097539-2f8f3151-aa3c-41e4-8f75-1cd7c45355a8.png">

<img width="672" alt="image" src="https://user-images.githubusercontent.com/52173621/200097544-f6d76122-1f98-4805-81e5-a933447f0d72.png">

De este análisis se concluyen las siguiente ecuaciones para las diferentes variables de articulación.

<img width="195" alt="image" src="https://user-images.githubusercontent.com/52173621/200097115-ab379c74-4130-4cdb-94de-2d1a2950e628.png">

<img width="288" alt="image" src="https://user-images.githubusercontent.com/52173621/200097134-9a6145b3-93eb-4891-a2cb-cd94c9aea808.png">

    q5 se mantiene fija en pi/2 si se quiere que el gripper esté cerrado.


Por último se realizó la comprobación de la cinemática usando el toolbox de Peter Corke en Matlab, disponible en el archivo DH.m

<img width="288" alt="image" src="sim.gif">

***

### Descripción de la solución planteada:
Se diseño un script en python, el cuál le solicita al usuario indicar una posición preestablecida o la figura que desee dibujar.
Se programaron las trayectorias usando la cinemática inversa previamente hallada, para dibujar el espacio de trabajo, un triángulo, un círculo, tres líneas paralelas, 5 puntos y una letra.
Adicionalmente el usuario puede llevar al robot a la posición de Home y a una posición especial para la colocación de la herramienta que contiene al marcador.

El programa consiste en 3 archivos .py y un archivo .csv. El archivo .csv contiene todos los puntos x,y,z para cada una de las figuras y trayectorias; En los scripts de python tenemos uno que se encarga de leer estos puntos del archivo .csv, aplicarles la cinemática inversa y retornar un vector con los valores de todas las variables articulares para el punto. Otro de los archivos de python se encarga de recibir este vector de variables articulares y mediante ela función JointTrayectoryPoint(), se publica está información para que el robot pueda leerla y ejecutarla. Finalmente el último archivo de python es main.py, que se encarga de instanciar el robot y llamar a todos los demás 

***

### Verificación Dimensional:
Durante el procedimiento de escritura se evidenció que los ejes x e y interpretados por el robot, eran distintos a los planteados originalmente.
La diferencia radicaba en qué la orientación del sistema real no coincidía con lo esperado, por lo cual fue necesario rehacer las coordenadas para los puntos de cada una de las figuras plateadas.
Se evidenció ademas un error de al rededor de 1cm.

***

### Evidencia de la solución realizada:

En los siguientes videos e imágenes se evidencia el funcionamiento del programa implementando.

![WhatsApp Image 2022-11-04 at 4 38 03 PM](https://user-images.githubusercontent.com/52173621/200097007-b4f6e0fa-d166-4304-8a0d-af7ed1bba29a.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 48 PM (1)](https://user-images.githubusercontent.com/52173621/200097008-9176aa51-12de-4dc7-8166-0e78ea097584.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 48 PM](https://user-images.githubusercontent.com/52173621/200097009-60236d84-3743-48d0-8e97-89f6a5172f21.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 47 PM (2)](https://user-images.githubusercontent.com/52173621/200097011-4c84ad79-c83c-44bd-8afc-fec96eda8a0b.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 47 PM (1)](https://user-images.githubusercontent.com/52173621/200097013-c3fdb26e-19be-4c5d-bc21-a698791d6a1e.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 47 PM](https://user-images.githubusercontent.com/52173621/200097014-be89f5d1-d18a-4861-b95b-3653d4dad5bc.jpeg)
![WhatsApp Image 2022-11-04 at 4 37 46 PM](https://user-images.githubusercontent.com/52173621/200097015-e807f972-3f11-4d84-af16-b78a1527c88a.jpeg)
