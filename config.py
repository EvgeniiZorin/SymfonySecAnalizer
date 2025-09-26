"""
Es un config file, que contiene 
la lista de pruebas para detectar problemas comunes 
en Symfony, incluyendo profiler y archivos confidenciales.
"""
tests = {
    "exposed_env_file": "/.env",
    "exposed_config": "/config.php",
    "exposed_vendor": "/vendor/autoload.php",
    "error_log": "/error_log",
    "console_route": "/_profiler",
    "app_dev": "/app_dev.php",
    "profiler_debug": "/app_dev.php/_profiler",  # Acceso directo al profiler en modo debug
    "phpinfo": "/app_dev.php/_profiler/phpinfo",  # Página de phpinfo en profiler
    "file_open": "/app_dev.php/_profiler/open?file=app/config/parameters.yml",  # Intento de acceso a archivo sensible
}
