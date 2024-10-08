# Backend (Django + DjangoRestFramework)
Este es el backend para la aplicación Iot SmartSenses y está desarrollado con Django y DjangoRestFramework. 

## Tabla de Contenidos
1. [Instalación](#instalación)
2. [Uso](#uso)
3. [API](#API)

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/adolfojb2/SmartSenses.git
   ```

2. Navegar al directorio del proyecto:
    ```bash
    cd Backend/
    ```
    
3. Instalar dependencias a partir del archivo requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

## Uso
Para iniciar la aplicación, ejecuta:
   ```bash
   python manage.py runserver
   ```

## API
Puedes acceder a la API del proyecto con los siguientes enlaces:
```http://127.0.0.1:8000/api/v1/users/```
```http://127.0.0.1:8000/api/v1/devices/```
```http://127.0.0.1:8000/api/v1/readings/```
```http://127.0.0.1:8000/api/v1/alerts/```

Y a la documentación de la API en el siguiente enlace:
```http://127.0.0.1:8000/api/v1/docs/```
