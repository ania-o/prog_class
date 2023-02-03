revcomp = {"A" : "T", 
              "T" : "A", 
              "C" : "G", 
              "G" : "C"}
			  
fin= open("rosalind_revc.txt", "r")
dna= fin.read().strip()

revc = ""

for nuc in dna:
   revc = revcomp[nuc] + revc
	
#print(revc)

fin.close()

#or to write into file: 

fout = open("solution_rna.txt", "w")
fout.write(revc)
fout.close()

