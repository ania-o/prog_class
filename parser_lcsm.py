from Bio.SeqIO.FastaIO import SimpleFastaParser

fout=open("sequences_lcsm.txt", "w")
with open("rosalind_lcsm.txt") as handle:
        for values in SimpleFastaParser(handle):
            seqname, seq = values
            fout.write(seq + "\n")

fout.close()
          


