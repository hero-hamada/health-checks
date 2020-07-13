import os
import sys

def ch_reboot():
	return os.path.exists("/run/reboot-required")

def check_disk():
	return True

def main():
	if ch_reboot():
		print("Pending reboot.")
		sys.exit(1)
	if check_disk():
		print("Good")
	print("ev ok:")

	sys.exit(0)
<<<<<<< HEAD

main()
=======
main()
>>>>>>> 246d8744f4e6a6b4b4b36016f499121a442d8681
