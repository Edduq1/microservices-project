import os
import psycopg2
import redis
import time

# --- Variables de Entorno ---
# Leemos las credenciales y configuraciones desde las variables de entorno
# que Docker Compose pasará a este contenedor desde el archivo .env
pg_host = os.getenv("POSTGRES_HOST")
pg_db = os.getenv("POSTGRES_DB")
pg_user = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT", 6379)) # Usamos 6379 como puerto por defecto

def test_postgres_connection():
    """Intenta conectarse a la base de datos PostgreSQL."""
    print("Intentando conectar a PostgreSQL...")
    conn = None
    try:
        # La cadena de conexión usa las variables de entorno
        conn = psycopg2.connect(
            host=pg_host,
            dbname=pg_db,
            user=pg_user,
            password=pg_password
        )
        # Si la conexión es exitosa, psycopg2 no lanza una excepción
        print("✅ ¡Conexión a PostgreSQL exitosa!")
    except psycopg2.OperationalError as e:
        print(f"❌ Error al conectar con PostgreSQL: {e}")
    finally:
        # Nos aseguramos de cerrar la conexión si se estableció
        if conn:
            conn.close()

def test_redis_connection():
    """Intenta conectarse al servidor de Redis."""
    print("\nIntentando conectar a Redis...")
    try:
        # Creamos un cliente de Redis
        r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        # El comando PING es la forma más simple de verificar la conexión
        r.ping()
        print("✅ ¡Conexión a Redis exitosa!")
    except redis.exceptions.ConnectionError as e:
        print(f"❌ Error al conectar con Redis: {e}")

if __name__ == "__main__":
    # Pequeña espera para dar tiempo a que los servicios se levanten completamente
    print("Esperando a que los servicios estén listos...")
    time.sleep(5) 
    
    test_postgres_connection()
    test_redis_connection()