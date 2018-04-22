# Repository for BIOC3001 (Advanced Practical in Molecular Biology) 

## Organisation of this Repo
The repository contains the following directories:  
* 'Scripts': QIIME scripts developed for the meta analysis of 16S rRNA sequencing data in the Cartesius supercomputer. 
* 'Data': data files used for processing and downstream analysis 
## 1. Obtaining the data
All the files used for data analyses including the raw sequencing data and the mapping file can be downloaded from the Data folder. Remember to unzip the sequencing data with the gzip command. 
### Mapping file (tab-delimited .txt)
This file contains all the information about the samples that was used to perform the data analysis. The sample ID, barcode sequence and metadata categories are provided in different columns. The potassium, phosphorus and nitrogen measurements were transformed into an exponential scale in order to be able to perform statistical testing. 
## 2. Validate the mapping file 
Ensure that the mapping file is correctly formated with the validate_mapping_file.py script. It will print a message indicating whether problems were found on the file and generate a log file and a file with the location of the errors. 
## 3. Demultiplex and quality filter the reads
In this step the reads are assigned to samples based on their barcode (demultiplexing). This step also performs quality filtering based on the parameters provided. To perform these steps we used: split_libraries.py
## 4. Closed reference OTU picking and tree building
### Step 1. Pick OTUs
Here we run the pick_closed_reference_otus.py script, wich picks OTUs using closed reference and constructs an OTU table. OTU picking is done against a reference database, e.g. SILVA, Greengenes, and those sequences that do not match the database are discarded from the analysis. 
### Step 2. Summarise OTU table
### Step 3. Pick a representative sequence from each OTU
### Step 4. Aling OTU representative sequences
### Step 5. Build a phylogenetic tree
