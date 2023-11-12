# marcopetit
Personal website with Blog made in Django
Este es un sitio web personal hecho para presentar como proyecto final en el curso de Django de CoderHouse el cual se basa en un sitio web personal y un blog de uso personal.


En la carpeta documetns podràn encontrar el video explicativo y también cuun Diagrama entidad relacion en un xml que se puede abrir en draw.io

Esta web consta de las siguientes páginas:
- Inicio
- Sobre mi
- Blog
- Currículum
- Cursos
- Contacto
- Usuario
- Cerrar / Iniciar sesión

1. Inicio, Sobre mi, Currículum y Contacto:
Son páginas estáticas en HTML salvo contacto que tiene un formulario con PHP para enviar correos.

2. Aplicaciones:
- Las siguientes aplicaciones tienen un menú especial que sólo se muestra si el usuario ha iniciadio sesión.
- Solo se pueden editar y eliminar aquellos usuarios que estén autenticados, tanto para los modelos basados en vista como los tradicionales.
- se trabaja con la herencia de templates.
- se trabaja con una carpeta static que es común para todas las aplicaciones.
- requirements.txt actualizado al día.
- se cambió el lenguaje de django para que los errores de los formularios se muetren en español.

2. 1. Blog: 
- El modelo principal es Entrada el cual consta de categoría, título, subtítulo, contenido usando el editor de estilos, fecha, relación uno a uno con el usuario que creó la entrada y etiquetas.
- Los modelos secundarios son Categorías y Etiquetas. Las categorías se guardan con relación de uno a muchos y las etiquetas de muchos a muchos.   
- las categorías que están asociadas a una entreda, no se pueden eliminar porque tienen la condicio protected.
-  La pantalla mis escritos es un listado de todas las entradas, haciendo clic en ellas se puede ver el detalle de cada una. 
- En el menú que se muestra para esta app, se peueden crear entradas, etiquetas, categorìas y también hay un listado de las entradas donde se pueden editar y eliminar.
- se usan formularios tradicionales. 

2. 2. Cursos
- El modelo principal es Cursos el cual consta de Año, Mes, Nombre, Insituto, Lugar y cantidad horas.
-  La pantalla mis escritos es un listado de todos los cursos. 
- En el menú que se muestra para esta app, se peueden crear cursos, y ver el listado donde se pueden editar y eliminar.
- se usan clases basadas en vistas. 

2. 3. Cuentas
- TIene una página principal que es el perfil del usuario.
- Tiene opción para registrar nuevo usuario e iniciar sesión.
- Se pueden editar los datos del usuario.
- se puede cambiar la clave.
- Hay un modelo adicional que se llama cuentas que tiene dirección e imagen de avatar.
- Tiene el acceso a "Mis mensajes" que es el sistema de mensajería entre usuarios
- se usan clases basadas en vistas. 

2. 4. Cerrar / Iniciar sesión
- El modelo principal es "Mensajes" que tiene remitente, destinatario, contenido y fecha de creación.
- en la sección del destinatario se ven todos los usuarios excepto el que está logueado. 
- Tiene la sección principal "Mis mensajes" que es la bandeja de entrada que muestra únicamente los mensajes que recibió el usuario que está logueado.
- Tiene la sección "Mensajes enviados" que es la bandeja de dalida que muestra únicamente los mensajes que envió el usuario que está logueado.
- cada uno de los mensajes del listado se puede acceder al hacer clic sobre el
- todos los mensajes desde el listado tienen la opcion de ser eliminados.

Listado de tecnologías usadas:
- HTML
- CCS
- Jquery
- Python
- Django
- Boostrap


