# Laboratorio 5.
## Robótica - Universidad Nacional De Colombia - Sede Bogotá.
### Sebastian Cubides - Julián Velandia.
***
### Cinemática inversa:

Se realizó una descripción geométrica del robot como se ve en la siguiente imagen.

FOTO

De este análisis se concluyen las siguiente ecuaciones para las diferentes variables de articulación.

ECUACUONES

Por último se realizó la comprobación de la cinemática usando el toolbox de Peter Corke en Matlab.

SIMULACIÓN


### Descripción de la solución planteada:
Se diseño un script en python, el cuál le solicita al usuario indicar una posición preestablecida o la figura que desee dibujar.
Se programaron las trayectorias usando la cinemática inversa previamente hallada, para dibujar el espacio de trabajo, un triángulo, un círculo, tres líneas paralelas, 5 puntos y una letra.
Adicionalmente el usuario puede llevar al robot a la posición de Home y a una posición especial para la colocación de la herramienta que contiene al marcador.

### Verificación Dimensional:
Durante el procedimiento de escritura se evidenció que los ejes x e y interpretados por el robot, eran distintos a los planteados originalmente.
La diferencia radicaba en qué la orientación del sistema real no coincidía con lo esperado, por lo cual fue necesario rehacer las coordenadas para los puntos de cada una de las figuras plateadas.
Se evidenció ademas un error de al rededor de 1cm.

### Evidencia de la solución realizada:

En los siguientes videos e imágenes se evidencia el funcionamiento del programa implementando.
