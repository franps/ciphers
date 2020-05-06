import random
import sys

abc={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
abc_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_abc= []
plain_text = "hello world"
method = "no_method"
csr = 0

if len(sys.argv)>1:
	method=sys.argv[1]
if len(sys.argv) == 3:
	plain_text = sys.argv[2]
if len(sys.argv) == 4 and sys.argv[1]=='csr':
	method = sys.argv[1]
	csr = sys.argv[2]
	plain_text = sys.argv[3]


if method == 'rand':
	print("Random substitution")
	new_abc = random.sample(abc_list,len(abc_list)) 
elif method == 'csr':
	print("Caesar cipher with "+str(csr)+" movements")
	new_abc = random.sample(abc_list,len(abc_list)) 
else:
	print("No method or invalid method chosen")
	new_abc = abc_list

print("--------------------------------------------------------------")
print(abc_list)
print(new_abc)
print("--------------------------------------------------------------")

def caesar(csr):
	return abc
	
def cipher(plain):
	print("Plain text: "+plain)
	c = ""
	for l in plain:
		if l == ' ':
			c+= ' '
		else:
			c += new_abc[abc[l]]
	return c

print("Ciphered text: "+cipher(plain_text))
