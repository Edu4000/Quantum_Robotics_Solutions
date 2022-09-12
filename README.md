# Quantum_Robotics_Solutions
Here I will be uploading my solution approaches to the different challeges for Quantum Robotics.

## English Explanation
From the description of the challenge, it can be broken down into four specific functions that work together:
- __Create new interest points__ <br>
The first function has the intention of creating a list of random direction vectors (coordinates) of interest points located within an arbitrary range from our initial approximate goal point. <br>
__Note: All the points are treated as numpy arrays to help with some calculations__

- __Next movement__ <br>
In order to move from one point to the other two things will happen. The rover will need to turn in order to face towards the direction of the next point and then advance. <br>
For the first task the program makes a difference of vectors to get the direction vector for our next movement.<br>
With this vector and the help of trigonometry, we can find the angle at which we need to face in order to go to the next point. We then proceed to take the difference of our current orientation with our result to get the number of radians we need to turn. <br>
![Steps to find the direction to turn](/img/Diagrama.png "Steps to find the direction to turn") <br>
Finally, after having the correct orientation we move forward to the next point with a loop that goes from 0 to the length of our direction vector (we also use the module of the direction vector to know how much we need to advance).

- __Find the best path__ <Br> 
To find the best path there exist two approaches, the first one could be a greedy algorithm that finds the total distance the rover would need to cover in order to visit all the possible points. The second one (the one implemented in the solution) has a geometric approach, where given a set of points, the shortest path is the one that forms a geometric figure between all the points. <Br> <Br>
In order to achieve the geometric approach I only looked for the nearest vertex (interest point) at any given vertex, advance to it, and repeat after for all the remaining vertex. At the end, the result is a geometric figure that has each of the interest points as vertex. <Br> <Br>

There also exist algorithms such as Dijkstra's Algorithm, but it fails at the time of not having a defined goal. <Br> <Br>

## Explicacion en Español
Por la descripcion del reto, este se puede romper en tres funciones que trabajan en conjunto:
- __Crear nuevos puntos de interes__ <br>
La primera funcion tiene la tarea de crear una lista de vectores direccion aleatorios (coordenadas) de los puntos de interes que se localizan en un rango arbitrario desde nuestro punto de destino aproximado.<br>
__Nota: Todos los puntos son manejados como numpy arrays para facilitar algunas calculos mas adelante__

- __Siguiente movimiento__ <br>
Para moverse de un punto a otro, dos cosas debe suceder. El rover debe cambiar de direccion hacia el siguiente punto y despues avanzar. <br>
Para la primera tarea, el programa calcula la el vector direccion de nuestro movimiento. <br>
Con este vector y la ayuda de trigonometria, podemos encontrar el angulo al que debemos apuntar para ir hacia el siguiente punto. Despues obtenemos la diferencia entre este angulo y nuestra orientacion actual para saber cuanto debemos de girar.
<br>
![Serie de pasos para encontrar la direccion de giro](/img/Diagrama.png "Serie de pasos para encontrar la direccion de giro") <br>
Fianlmente, despues de tener la orientacion correcta, avanzamos hacia el siguiente punto con un loop que va desde 0 hasta la longitud de nuestro vector direccion (tambien se usa el modulo del vector direccion para saber la distancia a avanzar).

- __Find the best path__ <Br> 
Para encontrar el mejor camino exiten dos aproximaciones. La primera es usar un algoritmo de busqueda avara que encuentre la distancia total que el rover debera conduxir para visitar todos los puntos. La segunda (y la cual se implemento en la solucion) tiene una aproximacion geometrica, donde, dados un grupo de puntos, el camino mas corto es aquel que forma una figura geometrica entre ellos. <Br> <Br>
Para lograr esta aproximacion geometrica, solo se busco por el vertice mas cercano (punto de interes) en un punto dado, avanzar hacia el, y repetir por el resto de los vertices. Al final, el resultado es una figura geometrica que tiene a cada punto de interes como un vertice. <Br> <Br>

Tambien existen algoritmos como el Algoritmo de Dijkstra para encontrar la ruta mas optima, pero este falla al no tener una meta definida. <Br> <Br>

# Running Examples
![Test 1](/img/Test1.png "Test 1") <br>
![Test 2](/img/Test2.png "Test 2") <br>
![Test 3](/img/Test3.png "Test 3") <br>