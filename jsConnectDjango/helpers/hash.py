# Python imports
import hashlib


# A simple decorator
def hash_digestor(func):
    def f(string):
        return func(string).hexdigest()
    return f


# Our hash functions
hash_sha1 = hash_digestor(hashlib.sha1)
hash_md5 = hash_digestor(hashlib.md5)


# The default hash function
def default_hash_func(hash_type):
    def func(string):
        digest = hashlib.new(hash_type, string).hexdigest()
        return "%s%s" % (digest, hash_type)
    return func


# Hashes a string in MD5 or SHA1 depending on secure
def js_connect_hash(string, secure = True):
    hash_func = default_hash_func
    if secure == 'md5' or isinstance(secure, bool):
        hash_func = hash_md5
    elif secure == 'sha1':
        hash_func = hash_sha1
    return hash_func(string) 
