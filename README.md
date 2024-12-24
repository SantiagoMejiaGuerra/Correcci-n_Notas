# Sistema de Corrección de Notas Médicas con Inteligencia Artificial

Este repositorio contiene el desarrollo de un sistema basado en Inteligencia Artificial que asiste en la corrección y estructuración de notas médicas. La aplicación está diseñada para ayudar a los profesionales de la salud a optimizar su flujo de trabajo, garantizando textos más legibles y sin errores.

------------

## Tabla de contenido
- [Sistema de Corrección de Notas Médicas con Inteligencia Artificial](#sistema-de-corrección-de-notas-médicas-con-inteligencia-artificial)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Características Principales](#características-principales)
  - [Tecnologías Utilizadas](#tecnologías-utilizadas)
  - [Requisitos Previos](#requisitos-previos)
  - [Instalación](#instalación)
  - [Ejecución del Proyecto](#ejecución-del-proyecto)
  - [Contacto](#contacto)


------------

## Características Principales
- Corrección de errores gramaticales y ortográficos en tiempo real.

- Transformación de textos desordenados en versiones estructuradas y legibles.

- Interfaz de usuario intuitiva con visualización de texto corregido mediante una ventana emergente (modal).

- Conexión API que permite el intercambio de datos entre frontend y backend en formato JSON.

-------------

## Tecnologías Utilizadas

- **Backend:** Python con FastAPI

- **Procesamiento de texto:** Groq API utilizando el modelo llama-3.1-70b-versatile

- **Frontend:** HTML, CSS y JavaScript

- **Middleware:** Manejo de CORS para solicitudes entre dominios

------

## Requisitos Previos
1. Python (versión 3.9 o superior)
2. HTML, CSS y JavaScript (**OPCIONAL**, si deseas personalizar mejor el front puedes usar Node.js)
3. Una clave de acceso a la API de Groq (*Link del video explicativo-->* **https://www.youtube.com/watch?v=J8JkqTrNDjA&t=435s**)

--------

## Instalación

- **Clonar el repositorio**
  ```
  git clone https://github.com/tu-usuario/sistema-correccion-notas.git
  cd sistema-correccion-notas

- **Crear un entorno virtual e instalar dependencias**
  ```
  python -m venv env
  source env/bin/activate # En Windows: env\Scripts\activate
  pip install -r requirements.txt

## Ejecución del Proyecto

1. **Iniciar el backend:**
   ```
   uvicorn Notas:app --reload

2. **Abrir el frontend:** Abre el archivo *Prueba.html* en tu navegador para interactuar con la aplicación

## Contacto
Si tienes preguntas, comentarios, o deseas contribuir a este proyecto, no dudes en contactarme a santiagomejiag.smg@gmail.com. o ![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)(https://www.linkedin.com/in/santiago-mejia-guerr/)
