import sys
import json

from .globals import *
from .colours import *

try:
    import requests
except ImportError:
    print("Failed to import \"requests\"")
    sys.exit(99)

def parsejson(json_obj, p: str):
    _json = json.loads(json_obj)
    return _json[f"{p}"]
    

def requestInfo(keyword: str) -> str:
    
    if len(keyword) < 3:
        print("[-] The provided search keyword is less than four (4) characters !")
        sys.exit(2)
    
    r = ""
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Cache-Control": "max-age=0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd"
    }
    
    s = requests.Session()
    
    FINAL_URL = PROXYNOVA_URL + COMB_PROXYNOVA_URI + COMB_PARAM
    
    try:
        r = requests.get( (FINAL_URL + keyword + "&start=0&limit=100"), verify=True, headers=headers )
        SUCCESS(f"Results: ")
        
        _json = parsejson(r.text, "lines")
        for line in _json:
            print(line)
            
    except Exception as e:
        print(e)
        sys.exit(1)
    
