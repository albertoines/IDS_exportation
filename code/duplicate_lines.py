from functions import remove_duplicate_lines
typename =  ["domain", "domain-ip", "hostname", "hostname-port", "ip-dst", "ip-dstport", "ip-src", "ip-src-port", "url", "md5", "sha1", "sha256", "sha512" ] 
typezeek = ["domain", "hostname", "url", "ip-src", "ip-dst", "md5", "sha1", "sha256", "sha512", "ja3-fingerprint-md5"]

for i in typezeek:
    name= "misp_"+ i +".intel"
    remove_duplicate_lines("rules/"+ name, "rules/" + name)

for i in typename:
    name= "misp_"+ i +".rules"
    remove_duplicate_lines("rules/"+ name, "rules/" + name)