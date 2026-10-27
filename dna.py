# Mera pehla bioinformatics code
dna = "ATGCATGCATGC"

print("Mera DNA:", dna)
print("Length:", len(dna))

# Complement banana
complement = ""
for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

print("Complement:", complement)
print("Bioinformatics journey started! - Mubeen")
