import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 55555
bots = []

def handle_bot(bot_socket, bot_address):
    print(f"[+] New bot connected: {bot_address}")
    bots.append(bot_socket)
    
    try:
        while True:
            command = input(f"Enter command for
{bot_address} (info/timestamp/quit): ")

if command =='quit':
    bot_socket.send(command.encode())
    break

elif command in ['info', 'timestamp']:
    bot_socket.send(command.encode())
    response = bot_socket.recv(1024).decode()
    print(f"Response from {bot_address}: {response}")
    
else:
  print("invalid command. Use 'info",
'timestamp', or 'quit'.")

except Exception as e:
    print(f"[-] Error with {bot_address}: {e}")
finally:
    bot_socket.close()
    bots.remove(bot_socket)
    print(f"[-] Bot disconnected: {bot_address}")
    
    def main():
        server = socket.socket(socket.AF.INET,
    socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Controller listening on {HOST}:{PORT}")
        
try:
    while True:
        bot_socket, bot_address = server.accept()
        bot_thread = threading.Thread(target=handle_bot,
    args=(bot_socket, bot_address))
        bot_thread.start()
        
except KeyboardInterrupt:
    print("\n[*] Shutting down controller...")
finally:
    server.close()
    
    if __name__ == "__main__":
        main()
