# filepath: /C:/Users/US PC/Documents/django projects/Nexbox/nexbox/test_connection.py
import socket

try:
    hostaddr = socket.gethostbyname("db.mzinqqeiyrmnazyisqnw.supabase.co")
    print(f"Resolved host address: {hostaddr}")
except Exception as e:
    print(f"Hostname resolution failed: {e}")