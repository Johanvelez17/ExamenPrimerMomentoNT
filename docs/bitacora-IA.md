# 📘 Bitácora de IA - Proyecto Examen Primer Momento

## 💡 ¿Cómo se usó ChatGPT en este proyecto?

### Durante el desarrollo de este proyecto se utilizó ChatGPT como asistente para:

- Explicar conceptos de Git y ramas (main, dev, feature/*).
- Resolver errores comunes en Python (e.g., conflictos con imports, errores de lectura de CSV).
- Apoyar en la validación de datos del CSV.
- Guiar paso a paso la organización del proyecto y estructura de carpetas.
- Redactar el README.md de manera clara y profesional.
- Configurar el repositorio en GitHub, incluyendo ramas protegidas y reglas.
- Simular conflictos y aprender cómo resolverlos manualmente.

### Este es el desglose de su ayuda activa en nuestra realización

## ¿Cómo nos asistió la IA?

### Durante el desarrollo del examen, usamos la IA como guía en los siguientes aspectos clave:

### 1. Planificación del Proyecto

La IA nos ayudó a entender qué pasos seguir una vez creado el repositorio y la estructura inicial del proyecto.

Recibimos orientación sobre cómo configurar correctamente ramas (main, dev, feature/*) y la estructura de carpetas (data, docs, etc.).

También nos ayudó a proteger la rama main mediante reglas en GitHub.

### 2. Creación de Issues y Etiquetas

Elaboramos 6 issues específicos, siguiendo recomendaciones sobre redacción, etiquetas (bug, enhancement, infra, documentation, etc.) y organización por prioridades.

La IA explicó el propósito de cada etiqueta y cómo vincular los issues a un tablero Kanban.

### 3. Organización con Kanban

Creamos un tablero tipo Kanban en GitHub Projects, con columnas como Por hacer, En progreso y Hecho, siguiendo el flujo recomendado.

La IA sugirió cómo mover los issues según el avance.

### 4. Manejo de Ramas y Commits

Aprendimos el concepto de ramas feature/*, su propósito, y cómo trabajar en paralelo sin afectar dev o main.

Se nos explicó cómo hacer commits pequeños y específicos, y luego integrarlos mediante pull requests.

### 5. Conflictos y Resolución

Provocamos un conflicto intencional en el archivo README.md y otros archivos (main.py, ComprasProyecto.csv) para cumplir con la parte del examen sobre resolución de conflictos.

La IA nos guió paso a paso para resolver los conflictos usando rebase, git add, git rebase --continue, y cerrar correctamente el flujo.

### 6. Pull Requests y Merge

Se nos asistió en la creación de pull requests desde las ramas feature/* hacia dev, y luego desde dev hacia main.

Además, aprendimos cómo usar GitHub para revisar, comparar y aprobar los cambios antes de hacer merge.

### 7. Documentación Final

Finalmente, la IA nos ayudó a redactar esta bitácora y a recuperar el contenido de archivos como main.py, ComprasProyecto.csv y bitacora-IA.md cuando se extraviaron por errores en Git.

También se nos recordó la importancia de mantener la documentación consistente en cada rama, especialmente en README.md.

## Nivel de intervención de la IA

 ChatGPT nos brindó sugerencias y estructuras base, pero las decisiones de implementación, pruebas y escritura final del código fueron realizadas por nosotros además de validar que la logica del código tanto en git como en visual estuvieran bien implementadas.


## Prompts utilizados
### Le pedimos a la IA que nos organizara los prompt utilizados durante el desarrollo con su respectiva temática o bloque a realizar

## Organización del proyecto y pasos del examen

"Estoy en la realización de un proyecto y esta es la estructura que me pidieron (ESTUCTURA DEL PROYECTO) vamos a desglosarla poco a poco y ayudame a entender los puntos del mismo"

#### (Nota: despues de desarrollar la primea parte de creacion de las ramas, estucturar los archivos, carpetas y tener toda esa parte organizada)

"vale y que mas sigue segun el examen?" 

#### Nota: (buscamos constantemente que la IA no nos dejara perder el hilo del documento pidiendole que nos diga en que parte del proyecto vamos y asi evitar estar cambiando de pagina constantemente)

"si ayudame a hacer toda esta parte paso a paso" 

"ahora si vamos con la ultima parte del examen, para los pull request, merge y solución de conflictos"

"ya tengo todo en main ahora que sigue segun la estructura de mi proyecto?"

#### Nota: (tuvimos un pequeño inconveniente con main dado que en la primera parte del proyecto hicimos un push a todas las ramas con lo cual a la hora de hacer el pull request tuvimos que eliminar con los comandos git rm --cached [nombre del archivo] los archivos que no nos sirvieran en las ramas para tener una estructura más limpia)

## Issues, etiquetas y ramas

"como debo crear tales issues con más detalle y que significan esas etiquetas"

#### Nota: (Queriamos saber con claridad que eran esas etiquetas y para que se usaban, porque github brinda una descripción pero es muy breve)


"como seria el issue para dev y para main y sus posibles etiquetas?"

#### Nota: (Dada la variedad de etiquetas queriamos saber más a profundidad como serían las etiquetas tanto para dev como para main porque el resultado anterioir solo nos mostró el resultado de una de las ramas pero no es lo mismo para el feature que para la rama principal o dev)

"que es la etiqueta infra?"

#### Nota: (Nos salió en para el resultado de main una etiqueta que no estaba en las predeterminadas de github con lo cual nos tocó crear etiquetas personalizadas para docs, para data y para infra la cual quiere decir 'infraestructura')

"y los issues deben de tener ese orden que me diste?"

#### Nota: (Aquí habiamos creado los issues en un orden diferente al algoritmo del proyecto del examen con lo cual le consultamos si el documento requería que llevaran un orden o si era indiferente, pero no nos convencio su respuesta asi que decidimos cerrar esos issue ya creados y crear otra vez desde el 6 hasta el 11)

"ya creé estos 6 issues con sus respectivas etiquetas: [...] son los que necesito para el examen verdad?"

#### NOTA: (Hicimos un pequeña validación para ver que todo estuviera en orden)

## Kanban / organización de tareas

"listo ya hice el tablero kanban ahora que sigue?"

#### Nota: (Creación del tablero kanban con sus 4 estados y de manera muy intuitiva desde la interfaz de github)

## Ramas y flujo de trabajo

"explicame bien eso del feature que es porque no lo entiendo"

"que es hacer merge o mergear?"

"cada rama debe tener un readme?"

#### Nota: (En esta parte hay pequeñas dudas que nos venian al momento de desarrollarlo para apropiarnos máas de los conceptos utilizados)

## Conflictos y final del examen

"creo que este era el punto de la creacion de un conflicto de manera intencional y de solucionarlo como dice el ejercicio"

#### Nota (Para este punto aún no sabiamos lo que era un conflicto, hasta que se nos presentó al querer hacer el segundo pull request por llevar un archivo con el mismo nombre donde github no sabe que archivo conservar, eliminar o sobreescribir)


"y en que parte del examen dice que debo borrar las feature? no las voy a borrar porque no es un item puntual del examen [...]"

#### Nota: (Aquí nos sugería que borraramos las ramas de reporte, estadistica y a de ingesta-datos para un manejo más limpio en el repositorio donde unicamente tuvieramos la rama main y opcional la rama dev pero decidimos dejarlas todas para tener la trazabilidad de lo desarrollado de una manera mas visual)


### AL final le pedimos que nos trajera todos los prompt utilizados en una pequeña lista y es lo que documentamos hasta aquí.

