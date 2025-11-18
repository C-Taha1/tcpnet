import sys , time , socket
from colorama import Fore , Style , init

Green = Fore.GREEN
Red = Fore.RED
Magenta = Fore.MAGENTA
Reset = Style.RESET_ALL

def typewritter(word):
		for w in word :
			sys.stdout.write(w)
			time.sleep(0.02)
			sys.stdout.flush()

def serv(ip , port):
	Serverbanner = r"""

#########################################################
#
#   TCPNET -- Connect Everything EveryWhere...
#          ( Made By CTaha-1 )
#
#########################################################
"""
	typewritter(f"{Magenta}{Serverbanner}{Reset}")

	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	try:

		s.bind((ip , port))

		s.listen()

		typewritter(f"{Green}[OK] SERVER IS LISTENING ON PORT {port}\n{Reset}")

		conn , addr = s.accept()

		while True:
			data = conn.recv(1024).decode(errors='ignore')
			if data == "/quit" or data == "/exit":
					conn.send(typewritter("[CLOSE] SERVER IS CLOSED...").encode())
					break

		else:
			import subprocess
			output = subprocess.check_output(data)
			conn.send(output.encode())

	except Exception as exp:
			typewritter(f"{Red}[ERROR] UNEXPECT BEHAVIOR WHY ➤ {exp}\n{Reset}")
			s.close()
			choice = int(input("[ASK] Retry? ( 0 = y / 1 = n) : "))

			if choice == 0:
				return serv(ip , port)

			elif choice == 1:
				typewritter("[EXITED] Exited Safely....\n")
				exit()
			else:
				print(f"{Red}[UNKNOWN] UNKNOWN CHOICE: {choice}\n{Reset}") 
				choice = int(input("[ASK] Retry? ( 0 = y / 1 = n) : "))

	finally:
		s.close()



def main():
		if len(sys.argv) < 2:
			typewritter(f"Usage: python3 {sys.argv[0]} <ip> <port>\n")
			return
		ip = str(sys.argv[1])
		port = int(sys.argv[2])

		serv(ip , port)


if __name__ == "__main__":
		main()


