import hashlib
import base64
import uuid
import os.path
import sys

def pass_n2s_last(passw):
	passs = " "
	if passw.strip()[-1] == '1' :
		passs  = passw[:-1].join( "@" )	
	if passw[-1:] == "2" :
		passs = passw[:-1].join( "@" )	
	if passw[-1:] == "3" :
		passs = passw[:-1].join( "#" )	
	if passw[-1:] == "4" :
		passs = passw[:-1].join( "$" )
	if passw[-1:] == "5" :
		passs = passw[:-1].join( "%" )	
	if passw[-1:] == "6" :
		passs = passw[:-1].join( "^" )
	if passw[-1:] == "7" :
		passs = passw[:-1].join( "&" )
	if passw[-1:] == "8" :
		passs = passw[:-1].join( "*" )	
	if passw[-1:] == "9" :
		passs = passw[:-1].join( "(" )
	if passw[-1:] == "0" :
		passs = passw[:-1].join( ")" )		
	t_sha = hashlib.sha512()
	t_sha.update(passs)
        hashcode = base64.urlsafe_b64encode(t_sha.digest())
	return hashcode


username = raw_input("enter username: ")
password = raw_input("\nenter password: ")
pass_swc_all = password.upper()
pass_swc_first = password.capitalize()
pass_rm_last = password[:-1]
pass_rm_first = password[1:] 
t_sha = hashlib.sha512()
filename = "users/" + username
if os.path.isfile(filename):
	with open( filename , 'r') as f:
    		first_line = f.readline()
	t_sha = hashlib.sha512()
	t_sha.update(pass_swc_all)
	hashcode = base64.urlsafe_b64encode(t_sha.digest())
	if first_line == hashcode:
		 print("Sucess!!")
		 sys.exit()	
	t_sha = hashlib.sha512()
	t_sha.update(pass_swc_all)
	hashcode = base64.urlsafe_b64encode(t_sha.digest())
	if first_line == hashcode:
		 print("Sucess!!")
		 sys.exit()	
	t_sha = hashlib.sha512()
	t_sha.update(pass_swc_first)
	hashcode = base64.urlsafe_b64encode(t_sha.digest())
	if first_line == hashcode:
		 print("Sucess!!")
		 sys.exit()	
	t_sha = hashlib.sha512()
	t_sha.update(pass_rm_last)
	hashcode = base64.urlsafe_b64encode(t_sha.digest())
	if first_line == hashcode:
		 print("Sucess!!")
		 sys.exit()	
	t_sha = hashlib.sha512()
	t_sha.update(pass_rm_first)
	hashcode = base64.urlsafe_b64encode(t_sha.digest())
	if first_line == hashcode:
		 print("Sucess!!")
		 sys.exit()	
	if first_line == pass_n2s_last(password):
		 print("Sucess!!")
		 sys.exit()	
