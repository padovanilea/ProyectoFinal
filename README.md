# ProyectoFinal
Repositorio para el proyecto final

Primera entrega de proyecto final
En este instructivo se indican las funcionalidades y el orden de ejecución de las mismas

Descripción:
El aplicativo consiste en la carga de una base de datos con los nombres de los familiares, la cual puede ser accedida para carga y consulta desde una web.
Los formularios alta_familiar.html, buscar.html y actualizar_familiar, heredan de base.html.
Hay 3 campos en el formulario de familiares: Nombre, dirección y pasaporte.

Procedimiento:
1- Cargar la base de datos: para esto hay que dar de alta a cada familiar completando los datos correspondientes por medio de http://127.0.0.1:8000/mi-familia/alta
2- Consultar la base de datos: para esto se ejecuta http://127.0.0.1:8000/mi-familia/
3- Búsqueda específica: se puede hacer una búsqueda particular por medio de http://127.0.0.1:8000/mi-familia/buscar
4- Para modificar un familiar: hay dos maneras de hacerlo. 
4.1- La primera manera es hacerlo con el pulsador correspondiente desde http://127.0.0.1:8000/mi-familia/
4.2- La otra manera es mediante http://127.0.0.1:8000/mi-familia/actualizar/id, donde id es el identificador único de cada integrande y corresponde al orden en el cual fueron ingresados a la base de datos.



