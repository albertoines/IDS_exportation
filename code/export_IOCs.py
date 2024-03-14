from keys import misp_url, misp_key
from functions import exportSuri, exportZeek_2
import datetime
# Script que se ejecuta diariamente para la actualización de los IOCs exportables a IDS. 

headers = { 'Authorization': misp_key, 'Accept': 'application/json', 'Content-type': 'application/json'}
typesuri = ["domain", "domain|ip", "hostname", "hostname|port", "ip-dst", "ip-dst|port", "ip-src", "ip-src|port", "url", "md5", "sha1", "sha256", "sha512"] 
typezeek = ["domain", "hostname", "url", "ip-src", "ip-dst", "md5", "sha1", "sha256", "sha512", "ja3-fingerprint-md5"]
indicator_type =["Intel::DOMAIN", "Intel::DOMAIN", "Intel::URL", "Intel::ADDR", "Intel::ADDR", "Intel::FILE_HASH", "Intel::FILE_HASH", "Intel::FILE_HASH", "Intel::FILE_HASH", "Intel::IN_JA3"]
last = "1d"
date = datetime.date.today()

for i in typesuri:
   typename = typesuri.index(i)
   exportSuri(misp_url, headers, i, typename, last, date)

for j in range(9):
    exportZeek_2(misp_url, headers, typezeek[j], indicator_type[j], last, date)