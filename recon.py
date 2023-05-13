    
import os
import sys
import subprocess
import argparse
import json
import requests
import datetime
import tldextract
import shutil
import nmap3


def nmap_scan(domain, directory):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    nmap = nampo3.nmap(domain)
    nmap_command = f"nmap {domain}"
    nmap = subprocess.check_output(nmap_command, shell=True, text=True)
    with open(f"{directory}/nmap", "w") as f:
        f.write(f"This scan was created on {today}\n\n")
        f.write(output)
    print(f"The nmap scan results are stored in {directory}/nmap")



def dirsearch_scan(domain, directory):
    

    '''if not shutil.which('dirsearch'):
        print("dirsearch is not installed. Installing...")
        subprocess.run(['pip', 'install', 'dirsearch'])'''
    
    dirsearch_output = os.path.join(directory, 'dirsearch')
  
    subprocess.run(['dirsearch -u'+ domain, '-e', 'php', '-e', 'asp', '-f', 'csv', '-o', dirsearch_output + ".csv"], shell=True, text=True)
    print(f"The dirsearch scan results are stored in the reports folder")

def crt_scan(domain, directory):
    

    crt_output = os.path.join(directory, 'crt')
   
    url = f"https://crt.sh/?q={domain}&output=json"
    
    try:
        response = requests.get(url)

        if response.content:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            crt_data = json.loads(response.content)

            with open(crt_output, 'w') as f:
                f.write(f"This scan was created on {today}\n\n")
                for data in crt_data:
                    f.write(data['name_value']+'\n')
            print(f"The CRT scan results are stored in {crt_output}")
        else:
            print("No results were found for the specified domain.")
            
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='mode', help='Choose mode: nmap, dirsearch, crt or default')
    parser.add_argument('domains', nargs='+', help='Domain names for reconnaissance')
    args = parser.parse_args()

    for domain in args.domains:
        directory = tldextract.extract(domain).domain + "_recon"
        os.makedirs(directory, exist_ok=True)

        if args.mode == 'nmap':
            print(f"Creating directory {directory}")
            nmap_scan(domain, directory)
        elif args.mode == 'dirsearch':
            dirsearch_scan(domain, directory)
            shutil.rmtree(directory)
        elif args.mode == 'crt':
            print(f"Creating directory {directory}")
            crt_scan(domain, directory)
        else:
            print(f"Creating directory {directory}")
            nmap_scan(domain, directory)
            dirsearch_scan(domain, directory)
            crt_scan(domain, directory)

if __name__ == '__main__':
    main()
    