import sys , socket
import time
from colorama import Fore , Style , init

Green = Fore.GREEN
Red = Fore.RED
Magenta = Fore.MAGENTA
Reset = Style.RESET_ALL

def typewritter(word):
		for i in word:
			sys.stdout.write(i)
			time.sleep(0.01)
			sys.stdout.flush()

def connect(ip , port):
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		try:
			banner = r"""

###########################################
#
#	TCPNET -- Connect Everything Everywhere...
#       ( Made By CTaha-1 )
#
############################################

"""
			typewritter(f"{Magenta} {banner} {Reset}")

			s.connect((ip , port))

			typewritter(f"{Green}[OK] CONNECTED TO: {ip}:{port}\n{Reset}")

			while True:
				data = input("➤  ")

				s.send(data.encode())

				if data == "/quit" or data == "/exit":
							break

				received = s.recv(1024).decode(errors='ignore')

				print(f"#############[SERVER RESPONSE]#############\n{received}\n##########################")


		except Exception as exp:
				typewritter(f"{Red}[ERROR] UNEXPECTED BEHAVIOR WHY ➤ {exp}{Reset}\n")
				s.close()
				choice = int(input("[ASK] Retry? ( 0 = y / 1 = n): "))

				if choice == 0:
						return connect(ip , port)
				elif choice == 1:
					typewritter("[EXIT] EXITED...\n")
					exit()

				else:
					typewritter(f"{Red}[UNKNOWN] UNKNOWN ➤ {choice}{Reset}")
					choice = int(input("[ASK] Retry? ( 0 = y / 1 = n): "))

		finally:
			s.close()


def main():
		if len(sys.argv) < 2:
				typewritter(f"Usage: python3 {sys.argv[0]} <ip> <port>\n")
				return

		ip = str(sys.argv[1])
		port = int(sys.argv[2])

		connect(ip , port)



if __name__ == '__main__':
		main()
