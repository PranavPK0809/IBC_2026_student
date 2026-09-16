Practice 1
1.	To navigate there I typed cd ~

2.	cd /Pranav/Dining 


3.	For this I did 
a.	cd ../
b.	cd ‘/c/Pranav/Fall 2026/cbio/IntroBiolComp-2026/Python’

4.	cd ../Unix 
and then cd sandbox 


Practice 2
1.	I started with cd ../../, which brought me to IntroBiolComp-2026
I then did “cd Python”

2.	I did cd DataFiles
And then I did wc BeeSpecies.txt

There are 19509 lines in the file 

3.	cd../../Unix
cd DataFiles
wc CodonTable.tsv	
There are 195 words 

4.	cat CodonTable.tsv
TTT is the last codon


# Git Code

```bash
git add Kumar_P1.md
git commit -m "Added Week 1 practical answers in Markdown"
git push
```

## Final Problem 2

### Script: semicolon_csv_converter.sh

#!/bin/bash

input_file=$1
output_file="converted_$input_file"

tr ';' ',' < "$input_file" > "$output_file"
