# ProyectoFinal

Se trata de un blog a traves del cual se describen 2 pruebas deportivas y se permite la inscripción de competidores para las mismas.

## Organización:
El mismo está organizado en distintas secciones:

- 010-Indice
En esta sección de inicio hay una breve descrición de quienes somos, que hacemos y nuestra propuesta para este verano.
Esta seccion para nosotros seria un ListView

- 020-3islas
En esta sección se describen las características detalladas de esta prueba.
También existe la posibilidad de descargar un folleto(archivo pdf) de la prueba.
Esto seria para nosotros un DetailView.

- 030-Moreno
En esta sección se describen las características detalladas de esta prueba.
También existe la posibilidad de descargar un folleto(archivo pdf) de la prueba.
Esto seria para nosotros un DetailView

- 040-Inscripción
Esta sección es para registrar a los inscriptos.
Tambien podemos hacer el login desde aca.

- 041-Inscripción - Lista de competidores
En esta subsección se pueden visualizar a los inscriptos

- 042-Inscripción - Alta de competidores y Modificación de competidores
En esta subsección se pueden dar de alta nuevos competidores y modificar los existentes (por el admin).

- 043-Inscripción - Reserva
Por ahora dejamos vacio

- 044-Inscripción - Baja de competidores
En esta subsección se pueden dar de baja a los competidores


## Navegación:
Se puede navegar el blog a traves de distintas secciones y con la siguiente convención:
- (Origen-->Destino1,Destino2)

### Secciones:
- 010 --> 020,030,040
- 020 --> 010,040
- 030 --> 010,040
- 040 --> 041,042,043,044,010
- 041 --> 040
- 042 --> 040
- 043 --> 040
- 044 --> 040
