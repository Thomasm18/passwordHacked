import requests
import hashlib
import sys

def pwned_api_check(password):
	#converts to hashcode and splits it
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #hexdigest creates the hexcode upper as its required by api
	first5_char, tail = sha1password[:5], sha1password[5:]
	#Gets response from API
	response = request_api_data(first5_char)
	#Compares response with password
	count = check_password_leak(response, tail)
	return count

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check API key')
	return res 

def check_password_leak(hashes, hash_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines()) #splitlines splits the text in each line
	for h,count in hashes:
		if h == hash_to_check:
			return count
	return 0

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count != 0:
			print(f"It seems your {password} password has been found {count} times..You should change it")
		else:
			print(f"Your {password} password has not been found, carry on")
	return "done!"

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))

