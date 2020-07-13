import os
import sys

def ch_reboot():
	return os.path.exists("/run/reboot-required")

def main():
	if ch_reboot():
		print("Pending reboot.")
		sys.exit(1)
	print("ev ok:")
	sys.exit(0)
main()