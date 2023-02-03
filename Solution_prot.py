## codon table

codon_data = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA *      CAA Q      AAA K      GAA E
UAG *      CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA *      CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G""".split("\n")

codon = {}
for line in codon_data:
    databits = line.split("      ")
    for x in databits:
        # x is like "AUG M"
        codon[ x[:3] ] = x[-1]
    
    
# -----------------------------

fin = open("rosalind_prot.txt", "r")
rna = fin.readline().strip() 
fin.close()


prot = ""
for n in range( int(len(rna)/3) ):
    c_ = rna[n*3:(n+1)*3]
    aa = codon[c_]
    
    if aa == "*":
        break
    
    prot += aa

print(prot)