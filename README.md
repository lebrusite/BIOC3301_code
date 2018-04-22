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
To view the statistics of the OTU table we run:
```biom summarize-table -i otus/otu_table.biom```
The following results were generated:
```Num samples: 30
Num observations: 16176
Total count: 4617705
Table density (fraction of non-zero values): 0.258
Counts/sample summary:
 Min: 640.0
 Max: 1467043.0
 Median: 110746.500
 Mean: 153923.500
 Std. dev.: 248373.010
 Sample Metadata Categories: None provided
 Observation Metadata Categories: taxonomy
Counts/sample detail:
515rcbc20: 640.0
515rcbc36: 34859.0
515rcbc8: 41831.0
515rcbc13: 60071.0
515rcbc34: 62599.0
515rcbc37: 62873.0
515rcbc9: 66575.0
515rcbc27: 70604.0
515rcbc23: 74817.0
515rcbc35: 89390.0
515rcbc32: 92499.0
515rcbc11: 98214.0
515rcbc33: 105672.0
515rcbc15: 106731.0
515rcbc17: 107850.0
515rcbc18: 113643.0
515rcbc28: 114903.0
```
Alternatively --qualitative can be passed to get the number of OTUs per sample
### Step 3. Pick a representative sequence from each OTU
### Step 4. Aling OTU representative sequences
### Step 5. Build a phylogenetic tree
