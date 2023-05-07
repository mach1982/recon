# recon
A reconnaissance tool inspired by the recon.sh script in Bug Bounty Bootcamp by Vickie Li. Created with the assistance of chatGPT'


usage: recon.py [-h] [-m MODE] domains [domains ...]

MODES 
    nmap - runs default namp scan on traget
    dirsearch - runs dirsearch on target domain 
    crt - runs tart get againg https://crt.sh/
    defualt - runs all modes 
    

positional arguments:
  domains     Domain names for reconnaissance
  
Example 
python3 recon.py -m namp github.com - run nmap on github.com
python3 recon.py github.com - run nmap, dirsearch, crt.sh on github.com

