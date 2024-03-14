from keys import misp_url, misp_key
from functions import fetchAllFeeds

headers = { 'Authorization': misp_key, 'Accept': 'application/json', 'Content-type': 'application/json'}
fetchAllFeeds(misp_url, headers)