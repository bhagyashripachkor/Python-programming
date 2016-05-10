# import hashlib

# x = hashlib.sha256("udacity")
# print x.hexdigest()

# import hashlib
# import hmac

# SECRET = 'imsosecret'
# def hash_str(s):
#    return hashlib.md5(s).hexdigest()
	# return hmac.new(SECRET, s).hexdigest()


# -----------------
# User Instructions
# 
# Implement the function make_secure_val, which takes a string and returns a 
# string of the format: 
# s,HASH

# def make_secure_val(s):
	# return "%s %s" % (s, hash_str(s))


# print make_secure_val("test")
#print make_secure_val("cool")

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

# def check_secure_val(h):
    # val = h.split(',')[0]
#	if h == make_secure_val(val):
#		return val
		
#print make_secure_val("udacity")

import random
import string
import hashlib

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    ###Your code here
	return ''.join(random.choice(string.letters) for x in xrange(5))

	
# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw):
    salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h,salt)
	
#print make_salt()
print make_pw_hash('spez', 'hunter2')