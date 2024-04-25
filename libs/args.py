import sys

try:
    import argparse
except ImportError:
    print("Failed to import \"argparse\"")
    sys.exit(99)
    
from .http import *
from .globals import *

def parse_args():
    
    parser = argparse.ArgumentParser(description="combsearch - Retrieve information about breached accounts from \"Combination Of Many Breaches\" database (from proxynova.com)")
    parser.add_argument("-s", "--search", help="Keyword to use for the search (e.g testuser)")
    parser.add_argument("-v", "--version", help="Return version of script", action="store_true")
    arg = parser.parse_args()
    
    if arg.search:
        requestInfo(arg.search)
        
    if arg.version:
        print(f"--- Version: {VERSION} ---")
        sys.exit(0)