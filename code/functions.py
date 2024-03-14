import requests
from datetime import datetime
import json
from keys import misp_url, misp_key

typename =  ["domain", "domain-ip", "hostname", "hostname-port", "ip-dst", "ip-dstport", "ip-src", "ip-src-port", "url", "md5", "sha1", "sha256", "sha512" ] 
typenamezeek =["ip", "url", "domain", "email", "filename", "ja3-fingerprint-md5", "filehash" ]

def restSearch(misp_url, headers, type, timestamp):
    endpoint = misp_url + 'attributes/restSearch'
    data = {"returnFormat": "json", "to_ids": "1", "timestamp": timestamp ,"type": type }
    json_data = json.dumps(data)

    # Realiza la solicitud POST a la API de MISP
    response = requests.post(endpoint, headers=headers, data=json_data)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.json()
        # Imprime los atributos
        data = response.content
        print(data.decode())
        #attr = data['response']['Attribute']
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)

def exportZeek(misp_url, headers, type, last, date):
    endpoint = misp_url + 'attributes/bro/download'
    datetime = "# "+ type + " MISP Zeek Rules ----> " + str(date)+"\n"
    data = {"returnFormat": "json", "to_ids": "1", "last": last ,"type": type }
    json_data = json.dumps(data)

    # Realiza la solicitud GET a la API de MISP
    response = requests.post(endpoint, headers=headers, data=json_data)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.content.decode('utf-8')
        #lineas = data.splitlines(True)[1:]
        #data = ''.join(lineas)
        file = open("rules/misp_"+ type +".intel", "a")
        file.write(datetime) 
        file.write(data + "\n") 
        file.close()
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)

def exportZeek_2(misp_url, headers, type, indicator, last, date):
    endpoint = misp_url + 'attributes/restSearch'
    datetime = "# "+ type + " MISP Zeek Rules ----> " + str(date)
    intel_type_blob = "#fields	indicator	indicator_type	meta.source"
    intel_type_blob = "{}\n{}".format(intel_type_blob, datetime)
    data = {"returnFormat": "json", "to_ids": "1", "last": last ,"type": type }
    json_data = json.dumps(data)

    # Realiza la solicitud GET a la API de MISP
    response = requests.post(endpoint, headers=headers, data=json_data)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        for attr in response.json()["response"]["Attribute"]:
            intel_type_blob = "{}\n{}\t{}\t{} (event ID {})".format(intel_type_blob, attr["value"], indicator, attr["Event"]["info"], attr["event_id"])
        intel_type_blob = "{}\n".format(intel_type_blob)
        file = open("rules/misp_"+ type +".intel", "a")
        file.write(intel_type_blob) 
        file.close()
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)
def exportSuri(misp_url, headers, type, index, last, date):
    endpoint = misp_url + 'attributes/restSearch'
    datetime = "# "+ type + " MISP Suricata Rules ----> " + str(date)+"\n"
    data = {"returnFormat": "suricata", "to_ids": "1", "last": last, "type": type }
    json_data = json.dumps(data)

    # Realiza la solicitud POST a la API de MISP
    response = requests.post(endpoint, headers=headers, data=json_data)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Imprime los atributos
        data = response.content.decode('utf-8')
        lineas = data.splitlines(True)[10:]
        data = ''.join(lineas)
        file = open("rules/misp_"+ typename[index] +".rules", "a")
        file.write(datetime) 
        file.write(data +"\n") 
        file.close()
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)   
        
def delAttr(headers, id):
    endpoint = misp_url + 'attributes/delete/' + str(id) + '/1'  # Hard delete
    # Realiza la solicitud GET a la API de MISP
    response = requests.delete(endpoint, headers=headers)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.json()
        # Imprime los atributos
        print(data)
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)

def fetchAllFeeds(misp_url, headers):
    endpoint = misp_url + 'feeds/fetchFromAllFeeds'
    
     # Realiza la solicitud GET a la API de MISP
    response = requests.post(endpoint, headers=headers)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Imprime los atributos
        data = response.content
        print(data.decode())
        #attr = data['response']['Attribute']
    else:
        # Imprime el mensaje de error si la solicitud no fue exitosa
        print('Error:', response.text)
    

def remove_duplicate_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    unique_lines = set()
    new_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line not in unique_lines:
            unique_lines.add(stripped_line)
            new_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(new_lines)

def process_file(input_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    with open(input_filename, 'w') as output_file:
        for line in lines:
            if line.startswith("http://") or line.startswith("https://"):
                line = line.split('//', 1)[-1]
            output_file.write(line)

