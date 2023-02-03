from Bio.SeqIO.FastaIO import SimpleFastaParser


def make_empty_matrix(l=1000):
	""" Returns a list with l elements, each element is a dictionary
	containing freq counts for A, C, G, T
	# parameters
	"""
	mat = [ []] * l
	for n in range( len(mat) ):
		mat[n] =  { "A":0, "C":0, "G":0, "T":0 }
	return mat


def count_bases_in_seqs(filename="rosalind_cons.txt"):
    with open(filename) as handle:
        for values in SimpleFastaParser(handle):
            seqname, seq = values
	        # ------------------
            for i in range(len(seq)):
                nt = seq[i]
                bases[i][nt] += 1	



bases = make_empty_matrix()
count_bases_in_seqs()

consensus = ""
for i in range(len(bases)):
    max_freq = max(bases[i].values())
    if max_freq == 0:
        break
    max_nuc = ""
    for nt in bases[i]:
        if bases[i][nt] == max_freq:
            max_nuc = nt
            break
    consensus += max_nuc

fout=open( "cons.output.txt"", "w")
fout.write(consensus + "\n")

for nuc in  ["A", "C", "G", "T"]:
    nuc_str = f"{nuc}:"
    for n in range(len(consensus)):
        nuc_str += " %d" % (bases[n][nuc])
    fout.write(nuc_str + "\n")
fout.close()