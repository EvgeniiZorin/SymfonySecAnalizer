# SymfonySecAnalizer

Este script en Python es un Proof of Concept (POC) para identificar vulnerabilidades comunes en aplicaciones web basadas en el framework Symfony (**Symfony Vulnerability POC**). El script prueba configuraciones inseguras y archivos expuestos en entornos donde el modo de depuración o profiler de Symfony está activado, permitiendo al usuario identificar rápidamente potenciales fallos de seguridad.

Email de contacto: m10sec@proton.me

## Características

- Detecta rutas expuestas que pueden revelar configuraciones sensibles.
- Intenta identificar la versión de Symfony mediante headers HTTP.
- Verifica si el profiler y el modo de depuración están habilitados.
- Busca archivos críticos como `.env` y `parameters.yml` que contienen datos sensibles.
- Incluye pruebas basadas en las indicaciones de Rahad Chowdhury para detectar múltiples vulnerabilidades en el profiler.

## Pruebas de Vulnerabilidades

Este POC realiza pruebas en las siguientes rutas y archivos comunes en Symfony:

- **`.env`**: Archivo de configuración expuesto.
- **`config.php`**: Archivo de configuración.
- **`vendor/autoload.php`**: Archivos del autoloading de Symfony.
- **`/_profiler`**: Ruta del profiler.
- **`app_dev.php`**: Archivo de entorno de desarrollo.
- **`_profiler/phpinfo`**: Página de `phpinfo`.
- **`_profiler/open?file=...`**: Intentos de acceso a archivos específicos (como `parameters.yml`) mediante la función `open` del profiler en modo de depuración.

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca `requests` ejecutando el siguiente comando:
   ```bash
   pip install requests
   ```
3. Cambia la URL en `SymfonySecAnalizer.py`
   ```py
   target_url = "http://example.com"  # Cambia esta URL al sitio objetivo
   ```
4. Ejecuta en command line:
   ```bash
   python3 SymfonySecAnalizer.py -u https://example.com
   ```

Ejemplo de salida:

```bash
Target is reachable.
Symfony Version Detected: 4.4.19

[+] exposed_env_file found at http://example.com/.env
[-] exposed_config not found at http://example.com/config.php
[+] console_route found at http://example.com/_profiler
[+] profiler_debug found at http://example.com/app_dev.php/_profiler
[+] file_open found at http://example.com/app_dev.php/_profiler/open?file=app/config/parameters.yml

Test Results:
exposed_env_file: http://example.com/.env
console_route: http://example.com/_profiler
profiler_debug: http://example.com/app_dev.php/_profiler
file_open: http://example.com/app_dev.php/_profiler/open?file=app/config/parameters.yml
```

## Advertencia

Este script debe utilizarse únicamente con fines de prueba y en entornos autorizados o controlados. El uso de este POC en sistemas de terceros sin permiso explícito puede ser ilegal y está prohibido.
