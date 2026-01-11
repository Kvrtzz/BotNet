import socket
import platform
import time

CONTROLLER_HOST = '127.0.0.1'
CONTROLLER_PORT = 55555

def get_system_info():
    return f"OS: {platform.system()}
{platform.release()}, Node: {platform.node()}"

def get_timestamp():
    return f"Timestamp: {time.ctime()}"
    
def main():
    bot = socket.socket(socket.AF.INET, socket.SOCK_STREAM)
    
    try:
        bot.connect((CONTROLLER_HOST, CONTROLLER_PORT))
        print(f"[*] Connected to controller at
{CONTROLLER_HOST}:{CONTROLLER_PORT}")

while true:
    command = bot.recv(1024).decode()
    
if command == 'quit':
    print("[*] Received quit command. Shutting down...")
    break

elif command == 'info':
    response = get_system_info()
elif command == 'timestamp':
    response = get_timestamp()
    
else:
    response = "Unknown command"
bot.send(response.encode())

except Exception as e:
    print(f"[-] Error: {e}")
finally:
    bot.close()
    print("[*] Bot disconnected.")
    
if __name__ == "__main__":
    main()
