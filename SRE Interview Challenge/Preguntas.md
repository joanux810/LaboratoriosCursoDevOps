# SRE INTERVIEW CHALLENGE

Las siguientes preguntas están diseñadas para conoce el enfoque de devops de un candidato en proyectos de software a un nivel intermedio. Así mismo, se enlistan las respuestas correctas, no limitadas, que demuestran que el candidato es correcto para una posición de SRE en una compañía de producto o de servicios.

1. ¿Me puedes compartir tu definición de DevOps?
    
Aquí esperamos que el candidato nos de una respuesta abierta de cómo aplica DevOps de manera personal y no es necesario qué nos explique el producto por conflicto de confidencialidad, pero si pasos y herramientas implicadas.
Posibles respuestas:
- Es una metodología de desarrollo donde los desarrolladores conocen sobre el despliegue de la aplicación y están involucrados en servir en software hasta el usuario final
- Filosofía de trabajo donde no hay equipo de operaciones y donde los desarrolladores codifican y liberan el software a los ambientes reales

2. ¿Cómo has aplicado DevOps en un proyecto de software en tu vida profesional? 

Aquí esperamos que el candidato nos dé una respuesta abierta de como implemento DevOps en un proyecto de software real, las best practices, roadblockers  y challenges durante la implementación.

3. Tenemos un código legacy qué expone una API donde la respuesta es un xml. Por necesidad del negocio, tenemos qué exponer ese misma respuesta pero en formato json. ¿Cual sería tu estrategia para asegurar que esta funcionalidad  y además el nuevo requerimiento estén funcionando ? 

Aquí esperamos que el candidato nos comparta una estrategia de branching, testing y comunicación. Primero se espera que mencione  el testing ya sea :
- unit test,
- integración
para asegurar que los nuevos cambios no rompan la funcionalidad ya existente, es decir que la API siga devolviendo los mismos XML antes de agregar el nuevo feature, e integrar nuevos que aseguren la funcionalidad del nuevo endpoint a json.

A partir de ese  branch de prueba , se puede crear un nuevo branch de para el nuevo requerimiento. Si el candidato lo sugiere, podríamos indagar en el nombrado de los branches.

4. ¿Me puedes describir tu estrategia para llevar la funcionalidad descrita en la pregunta anterior a  producción? (Como se comunico con el equipo, como convenció al equipo de liderazgo, como se desplego)

Esperamos que nos explique su estrategia ante desastres y alta disponibilidad, es posible mencionar un cloud provider y los servicios que le ayudarán a completar el despliegue en producción. Se le puede sugerir un diagrama.

5. ¿Que es un Content Delivery Network?
   
6. ¿Que es un Load Balancer?
   
7. ¿Cuál es tu recomendación para añadir Load Balancers a la infraestructura de una aplicación?



