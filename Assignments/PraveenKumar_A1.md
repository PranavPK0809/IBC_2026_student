\# Assignment 1: Unix and Python



\## 1. Number of Subjects



\### A. Downloading the Data



I first went to the course repository and used `git pull`. I then navigated into the Assignment1 directory and used `ls` to view the downloaded assignment files.



```bash

cd "/c/Pranav/Fall 2026/cbio/IntroBiolComp-2026"

git pull

cd Assignment1

ls

```



\### B. Number of Samples for Individuals 8 and 22



I used `cut` to count how many times individuals 8 and 22 appeared in the data. The `-w` option matches the individual ID, and the `-c` counts the # of matching lines.



```bash

cut -f 1 Gesquiere2011\_data.csv | grep -w -c 8

cut -f 1 Gesquiere2011\_data.csv | grep -w -c 22

```



Individual 8 was sampled \*\*17 times\*\*, and individual 22 was sampled \*\*5 times\*\*.





\### C. Script to Count Samples for an Individual



I wrote a script that takes the data filename as $1 and the individual ID as $2. The script uses `grep` to match the individual ID and count the number of matching lines.



```bash

\#!/usr/bin/bash



\# Count the number of samples for an individual

\# $1 is the data file and $2 is the individual ID



cut -f 1 $1 | grep -w -c $2

```

Used individual 8 and 22 to check



```bash

bash CountIndividual.sh Gesquiere2011\_data.csv 8

bash CountIndividual.sh Gesquiere2011\_data.csv 22

```



I got 17 for individual 8 and 5 for individual 22.





\### D. Number of Samples for Each Individual



I wrote a Bash script to count how many times each individual was sampled and save the results in Num\_samples.csv. It loops through each ID, counts the samples, and saves the results.



```bash

\#!/usr/bin/bash



\# Count the number of samples for each individual

\# $1 is the data file



echo "maleID,Num\_samples" > Num\_samples.csv



for ID in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 118 119 120 121 122 123 124 125 126 127

&#x20;   do

&#x20;       number=`cut -f 1 $1 | grep -w -c $ID`

&#x20;       echo "$ID,$number" >> Num\_samples.csv

&#x20;   done

```



I ran it with:



```bash

bash CountAllIndividuals.sh Gesquiere2011\_data.csv

```

This file `Num\_samples.csv` had each row containing an individual ID and the number of times that individual was sampled.





\## 2. Mining The Origin of Species



\### A. Downloading the Text



Used `curl` to download \*The Origin of Species\* and saved it as `OriginofSpecies.txt` using the code below:



```bash

curl https://www.gutenberg.org/cache/epub/1228/pg1228.txt -o OriginofSpecies.txt

```



\### B. Word Counts



I used `grep` and `wc` to count each word



```bash

grep -i -o "sterility" OriginofSpecies.txt | wc -l

grep -i -o "isolation" OriginofSpecies.txt | wc -l

```

"Sterility" occurred \*\*97 times\*\* and the word "isolation" occurred \*\*12 times\*\*.





\### C. 



I used `grep` to find each word with three lines before and after it, then saved the results into separate files.



```bash

grep -i -B 3 -A 3 "sterility" OriginofSpecies.txt > sterility.txt

grep -i -B 3 -A 3 "isolation" OriginofSpecies.txt > isolation.txt

```



\### D. WordClouds



I used `wordcloud` to create a word cloud for each text file.



```bash

wordcloud\_cli --text sterility.txt --imagefile sterility.png

wordcloud\_cli --text isolation.txt --imagefile isolation.png

```



!\[Sterility Word Cloud](sterility.png)



!\[Isolation Word Cloud](isolation.png)



\### E. Interpretation

Based of the word clouds, I don't think Darwin failed to address the processes that lead to the formation of new species. In the sterility and isolation sections, there are words like species, hybrids, fertility, favourable and natural selection that appear often. This shows that the ideas were indeed discussed. 





\## 3. Twelve Days of Christmas



I used two lists to store the days and gifts. 

```python

days = \["First", "Second", "Third", "Fourth", "Fifth", "Sixth",

&#x20;       "Seventh", "Eigth", "Ninth", "Tenth", "Eleventh", "Twelfth"]



gifts = \["A Partridge in a Pear Tree",

&#x20;        "Two Turtle Doves, and",

&#x20;        "Three French Hens",

&#x20;        "Four Colly Birds",

&#x20;        "Five Gold Rings",

&#x20;        "Six Geese-a-Laying",

&#x20;        "Seven Swans-a-Swimming",

&#x20;        "Eight Maids-a-Milking",

&#x20;        "Nine Ldaies Dancing",

&#x20;        "Ten Lords-a-Leaping",

&#x20;        "Eleven Pipers Piping",

&#x20;        "Twelve Drummers Drumming"]



for i in range(0,12):

&#x20;   print("On the", days\[i], "day of Christmas my true love gave to me:")



&#x20;   for j in range(i,-1,-1):

&#x20;       print(gifts\[j])



&#x20;   print()

```



\## 4. Submission



I used the following code to add, commit, and push my assignment files to the repository.



```bash

git add Assignments

git commit -m "Add Assignment 1"

git push

```



