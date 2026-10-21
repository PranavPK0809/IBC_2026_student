# Disease Risk Q1
# Read the genotype data, calculate the total genotypes at each site
# Finding the total number of people that were sampled
geno <- read.table("H938_Euro_chr6.geno", sep=" ", h=T)

#
total <- geno$nA1A1 + geno$nA1A2 + geno$nA2A2
max(total)

# Disease Risk Q2
# Use rowSums to calculate the total genotypes at each site and finding the maximum
head(geno)
total_rows <- rowSums(geno[,5:7])
max(total_rows)

# Disease Risk Q3
# Read the disease risk data and join its third column to the genotype data
risks <- read.csv("SNP_risks.csv")
geno_risks <- cbind(geno, risks[,3])

head(geno_risks)

# Disease Risk Q4
# The average number of heterozygous individuals at Risk and Non-Risk sites
geno_risks$Risk <- risks[,3]

mean(geno_risks[geno_risks$Risk == "Risk",]$nA1A2)
mean(geno_risks[geno_risks$Risk == "Non-Risk",]$nA1A2)



# Data Cleanup 1Q
# Read the mammal body mass data and determine how many species are represented
smith <- read.delim("Smith2003_data.txt", h=F)

nrow(smith)

# Data Cleanup 2Q
# Replace missing values in columns 7 and 8 with NA and write the cleaned data to a new file
smith[smith[,7] == -999, 7] <- NA

smith[smith[,8] == -999, 8] <- NA

write.table(smith, file="Smith2003_clean.txt", sep="\t", row.names=F, col.names=F)