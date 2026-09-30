# Open the fasta file and get contents from the Turkey file and create the results file
with open("Turkey_transcripts_15.fasta", "r") as infile, open("gc_content.txt", "w") as outfile:

#Go through the file two lines at a time
    for i, line in enumerate(infile):
        line = line.rstrip()

#Save the sequence name
        if i % 2 == 0:
            gene_id = line.split()[0]

#Calculate GC content for the sequence
        else:
            seq = line
            gc = (seq.count("G") + seq.count("C")) / len(seq)
            outfile.write(gene_id + "\t" + str(gc) + "\n")