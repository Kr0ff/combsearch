# combsearch
Retrieve information about breached accounts from "Combination Of Many Breaches" database (from proxynova.com)

# Description
The script is pretty simple, it uses the API of proxynova.com to return results from the COMB database leak. 
> Please note that the information returned does not include all possible results and it seems to be a limitation of the API (afaik). The returned results appear to be always 20 entries, if there are more than 20 entries in the database.
> UPDATE: Proxynova have now updated their API to allow up to 100 results to be retrieved per request.

```sh
$ ./combsearch.py -h

 _  _  _ _  /_  __  _  __  /_
/_ /_// / //_/_\/_'/_|//_ / /    @Kr0ff

Combination Of Many Breaches (COMB) info via proxynova.com
    
usage: combsearch.py [-h] [-s SEARCH] [-v]

combsearch - Retrieve information about breached accounts from "Combination Of Many Breaches" database (from
proxynova.com)

options:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Keyword to use for the search (e.g testuser)
  -v, --version         Return version of script
```

# Example
Example of returned information:

```sh
$ ./combsearch.py -s testuser

 _  _  _ _  /_  __  _  __  /_
/_ /_// / //_/_\/_'/_|//_ / /    @Kr0ff

Combination Of Many Breaches (COMB) info via proxynova.com
    
[+] Results: 
testuser@mailcatch.com 	testuser
testUser@testmail.bzzagent.com:password9
testUser@testthis.com:fuckyourself
testuser-@web.de:atorea59ud
testuser@123test.com:test123
testuser@12et.com:myspace8
testuser@aaa.com:testuser
testuser@abc.com:abc123
testuser@aim.com:access
testuser@aim.com:hydsy64
testuser@aim.com:test
testuser@aim.com:testpass
testuser@aim.com:testuser
testuser@aim.com:testuses
testuser@aim.com:tlb012
testuser@aim.com:usertest
testuser@almerblank.com:test2010User
testuser@amelsberg.com:password
testuser@anthonyzarry.com:mydell1
testuser@aol.com:Buldum11
```

# Disclaimer
This script has been written for educational purposes only and the author is not liable for any missuse of third-parties !
