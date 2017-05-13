import hashlib
import base64
import uuid

D  =  { 'password':'PASSWORD',
'qwerty':'QWERTY' ,
'welcome':'Welcome' ,
'1qaz2wsx':'1qaz2wsxx' ,
'Master':'master' ,
'monkey':'monkey1' ,
'letmein':'1letmein' ,
'princess':'!princess' ,
'passw4rd':'passworD' ,
'starwars4':'starwars$' 
}

for key,value in D.iteritems(): 
	t_sha = hashlib.sha512()
	t_sha.update(value)
	f = open( "users/"+key, 'w')
	f.write( base64.urlsafe_b64encode(t_sha.digest()) )  
	f.close() 
