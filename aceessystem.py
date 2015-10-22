#
#
#
#        tokenizer system on python
#
#
#

#import string
#a = string.ascii_lowercase


# эта функция переводит из системы счисления а в систему счисления с основанием b
def numTObase(a,b):
	k = ''
	if a<0:
		k='-'
		a=abs(a)
	x = a
	n = ""
	if a==0:
		return '0'
	if b<=0:
		return str(a)
	while x > 0:
		y = str(x % b)
		n = y + n
		x = int(x / b)
	return k+n

# эта функция возвращает время в миллисекундах подобно (new Date()).getTime() -> int
def TimestampMillisec64():
	import datetime
	return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 

# эта штука генерирует ключ доступа на время t (int) -> str
def generateToken(time=10000):
	livetime = numTObase(time,6)
	from random import randrange as r
	import string
	a = string.ascii_lowercase
	offset = r(2)
	final = ''
	for i in str(TimestampMillisec64()):
		final+=a[int(i)+(10*offset)]
		if r(10)>6 and livetime!='':
			final+=a[int(livetime[0])+20]
			livetime=livetime[1:]
	while livetime!='':
		final+=a[int(livetime[0])+20]
		livetime=livetime[1:]
	return final

#эта функция возвращает из ключа его время создания и время, на которое он создан в массиве (str) -> [a,b] int
def tokenTomillis(token):
	import string
	a = string.ascii_lowercase
	final = ''
	timing = ''
	for i in token:
		if a.find(i)>=20:
			timing+=str(a.find(i)-20)
		else:
			final+=(lambda x: str(x) if int(x)<10 else str(int(x)-10) )( a.find(i) )
	timing = int(timing,6)
	return [int(final),timing]

#эта функция смотрит действителен ли ключ (str)-> bool
def secure(Token):
	time,p = tokenTomillis(Token)
	if TimestampMillisec64()-time<p:
		return True
	else:
		return False


#debug mode:

def simplePR(t):
	Y = generateToken(t)
	n=0
	while secure(Y):
		print('app is work, current token is: '+Y+' ; current time is: '+str(n))
		n+=1


