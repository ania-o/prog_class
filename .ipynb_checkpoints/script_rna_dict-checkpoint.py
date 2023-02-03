transcribe = {"A" : "A", 
              "T" : "U", 
              "C" : "C", 
              "G" : "G", 
              "\n" : " "}
			  
fin= open("rosalind_rna.txt", "r")
dna= fin.read()

rna = []

for nuc in dna:
    nuc_r = transcribe[nuc]
    rna.append(nuc_r)
	
print("".join(rna))

fin.close()

#or to write into file: fout = open("solution_rna.txt", "w")