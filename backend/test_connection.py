"""
Quick server connectivity test
"""
import socket
import time

def test_server_connection():
    """Test if server is listening on port 8000"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex(('localhost', 8000))
        sock.close()
        
        if result == 0:
            print("✅ Server is listening on port 8000")
            return True
        else:
            print("❌ Server is not responding on port 8000")
            return False
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        return False

if __name__ == "__main__":
    print("🔌 Testing server connectivity...")
    test_server_connection()
