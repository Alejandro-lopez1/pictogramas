# Arquitectura del sistema

## Objetivo

Aplicación PWA para creación de material visual basado en pictogramas de CAA (Comunicación Aumentativa y Alternativa).

El sistema permitirá buscar pictogramas, construir plantillas visuales y exportar material imprimible.

## Arquitectura general

Arquitectura cliente-servidor:

- Frontend: React + TypeScript + Vite
- Backend: Django + Django REST Framework
- Base de datos: PostgreSQL
- Contenedores: Docker

## Frontend

Responsabilidades:

- Editor visual de materiales.
- Gestión del lienzo.
- Inserción y manipulación de pictogramas.
- Interacción con API.

Tecnologías:

- React
- TypeScript
- Konva.js
- Tailwind CSS
- PWA

## Backend

Responsabilidades:

- Gestión de usuarios.
- Gestión de proyectos.
- Integración con ARASAAC.
- Persistencia de diseños.
- Generación de exportaciones.

Tecnologías:

- Python
- Django
- Django REST Framework

## Integraciones

### ARASAAC

Fuente externa de pictogramas.

Flujo:

Usuario busca palabra.
↓
Backend consulta ARASAAC API.
↓
Frontend muestra resultados.
↓
Usuario agrega pictograma al diseño.

## Principios

- Código modular.
- Separación de responsabilidades.
- Diseño orientado a dominio.
- Desarrollo incremental.
