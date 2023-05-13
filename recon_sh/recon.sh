#!/bin/bash
nmap_scan(){
	
	nmap $DOMAIN > $DIRECTORY/nmap
	echo "Nmap scan results are sotored in $DIRECTORY/nmap"
}

dirsearch_scan(){
if ! [ -x "$(command -v dirsearch)" ]; then
    echo "dirsearch is not installed. Installing..."
    pip install dirsearch
else

dirsearch -u $DOMAIN -e php -e php -format simple -o $DIRECTORY/dirsearch
echo "The dirsearch scan results are sotored in $DIRECTORY/dirsearch"

fi

}

crt_scan(){
	 curl "https://crt.sh/?q=$DOMAIN&output=json" -o "$DIRECTORY/crt"+

    echo "The CRT scan results are stored in $DIRECTORY/crt"
}

getopts "m:" OPTION
MODE=$OPTARG

for i in "${@:$OPTIND:$#}"
do
	DOMAIN=$i
	DIRECTORY=${DOMAIN}_recon
	echo "Creating directory $DIRECTORY"
	mkdir $DIRECTORY

	case $MODE in
		nmap-only)
		 nmap_scan
		;;
		dirsearch-only)
		 dirsearch_scan
		 ;;
		crt-only)
		 crt_scan
		 ;;
		*)
		   nmap_scan
		   dirsearch_scan
		   crt_scan
		 ;;
	   esac

	   echo "Creating report for $DOMAIN ..."
	   TODAY=$(date +"%Y-%m-%d")
	   echo "This scan was created on $TODAY" > $DIRECTORY/report
	   if [ -f $DIRECTORY/nmap ];then
	   	echo "Results for namp" >> $DIRECTORY/report
	   	grep -E "^\s*\S+\s+\S+\s+\S+\s*$" $DIRECTORY/nmap >> $DIRECTORY/report
	   fi

	   	if  [ -f $DIRECTORY/dirsearch ];then
	   	echo "Results for dirsearch" >> $DIRECTORY/report
	   	cat $DIRECTORY/dirsearch >> $DIRECTORY/report
	   fi

	   
	   	if [ -f $DIRECTORY/crt ];then
	   	echo "Results for crt.sh" >> $DIRECTORY/report
	   	jq -r '.[] | .name_value' $DIRECTORY/crt >> $DIRECTORY/report

	   fi

	done







		


