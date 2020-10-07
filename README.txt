
genome.jp/tools/motif result.txt to FASTA file converter:
========================================================= 

Use:
	After submission of Motif pattern in Search Sequence Database(https://www.genome.jp/tools/motif/MOTIF2.html) will generate the result file having sequences found in SWISSPORT. Which will contain several columns. The present tool removes those columns and give fasta file having Uniprot ID and Protein sequences (see the example folder) which can be used for further analysis like BLAST or sequences analysis. 

Usage:
       GUI based: Download the tool Motif_result_to_fasta.exe from https://www.dropbox.com/s/5g7sayg4j5zjfbs/motif_resulttofastaGUI.zip?dl=0

for Windows and run in your local computer. It does not require any dependencies installation. It will open window where you can browse file for result.txt and Run. It will pop-up window and generates the ‘swissfastafile.fasta’ file and mycsv.csv file in same directory where tool has been present. 
       
       Command line: Download the “motif_resulttofasta.py” file and run in cmd “python motif_resulttofasta.py result.txt”. Before running make sure that both .py and result.txt files in same directory. If you renamed result.txt, type "python motif_resulttofasta.py yourfilename.txt" in cmd. To run this tool in cmd you need Python, Pandas module.

           
