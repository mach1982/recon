# recon
A reconnaissance tool inspired by the recon.sh(see recon_sh folder) script in Bug Bounty Bootcamp by Vickie Li. Created with the assistance of chatGPT'

Requires diresearch
https://github.com/maurosoria/dirsearch



Reconnaissance Tool

This is a reconnaissance tool inspired by the recon.sh script in "Bug Bounty Bootcamp" by Vickie Li. It was created with the assistance of chatGPT.
Usage

To use the tool, run the following command:


python3 recon.py [-h] [-m MODE] domains [domains ...]

The tool has several modes that can be specified using the -m flag:

    nmap: runs the default nmap scan on the target domain
    dirsearch: runs dirsearch on the target domain
    crt: runs a search for the target domain on https://crt.sh/
    default: runs all modes

The tool takes one or more domain names as positional arguments.
Example

To run nmap on github.com, use the following command:

python3 recon.py -m nmap github.com

To run nmap, dirsearch, and crt.sh on github.com, use the following command:

python3 recon.py github.com

Installation

To use this tool, you need to have Python 3 installed on your machine. You can download Python 3 from the official website at https://www.python.org/downloads/.

Depending on your system, you may need to install other Python packages:

You can install these packages using the following command:
pip install <pagckage_name>

Contributing

Contributions are welcome! If you find a bug or have a feature request, please create an issue on the GitHub repository.
Spelling


