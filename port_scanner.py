import socket
from datetime import datetime
def scan_port(target, port):
  """
  Attempts to connect to a specific port on the target.
  Returns True if open, False otherwise.
  """
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0
  except Exception:
    return False
def main():
  print("=== Mini Port Scanner (Safe) ===")
  target = input("Enter target IP (e.g., 127.0.0.1): ")
  common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]
  print(f"\nScanning {target} for common ports...\n")
  print(f"{'Port':<8}{'Status':<10}")
  print("-" * 18)

  open_ports = []

  start_time = datetime.now()

  for port in common_ports:
        if scan_port(target, port):
            status = "Open"
            open_ports.append(port)
        else:
            status = "Closed"
        print(f"{port:<8}{status:<10}")

   end_time = datetime.now()
   print(f"\nScan completed in: {end_time - start_time}")
   if open_ports:
     print(f"Open ports: {open_ports}")
   else:
     print("No open ports found.")
if __name__ == "__main__":
    main()
#Adapted from guidance for internship project demonstration
