# Nodo 3: CI/CD Pipeline con Jenkins y Docker

**Objetivo**

Implementar un CI/CD Pipeline con Jenkins y Docker para una API utilizando un lenguaje de backend.

**Descripción**

Crear un CI/CD Pipeline para la integración de la aplicación utilizando la aplicación [myticalmysfits](https://mythicalmysfits.com/) del Nodo 2.

En el Nodo 2 creamos los unit test que apoyan la validación de funcionamiento de nuestra API. Vamos a agregar el [jenkins file](https://github.com/aws-samples/amazon-eks-jenkins-terraform/blob/master/Jenkinsfile) basado en el ejemplo del laboratorio para asegurar el building de la aplicación.

[Dockerfile](https://github.com/joanux810/aws-modern-application-workshop/blob/java/module-2/app/Dockerfile)

Recordatorio: [terraform](https://github.com/aws-samples/amazon-eks-jenkins-terraform/tree/master/terraform) solo provisiona los recursos para el servidor de Jenkins.

**Tutorial**

[Spring Boot PetClinic Sample](https://github.com/aws-samples/amazon-eks-jenkins-terraform)

**Evidencia**
- Screenshot del pipeline en una instancia EC2
- Link al repositorio/fork donde esta el jenkinsfile.
  
**Rúbrica de evaluación**

| Indicador     | Ponderación |
| ------------- | ----------- |
| Sobresaliente | 1           |
| Satisfactoria | .8         |
| Medianamente  | .5          |
| No cumple     | 0           |
