"""
Extra Exercises
Strings - count the number of codons

Created on Tue Jun  1 08:18:52 2021

@author: john.hanks
"""

# Variables
dna = 'ATTTGCGGTCCAAATCCAAATTGCATTTGCGGT'

#################  Questions  ###############


# find the first position of the TGC codon




# count the locations of the TGC codons




# can you output in one line of code the positions of the codon?
# see https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python/2294502











############### Solutions ######################

# find the first position of the TGC codon
c = "TGC"
position = dna.find("TGC")
print('The first postion of the codon is: ', position) 


# count the locations of the TGC codons
position= []
print('The DNA: ', dna)

for pos,char in enumerate(dna):
    test_codon = dna[pos:pos+3]
    if c == test_codon:
        position.append(pos)

print('The positions of all the TGC codons: ', position)  


# can you output in one line of code the positions of the codon?
# see https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python/2294502

([pos for pos, char in enumerate(dna) if dna[pos:pos+3] == c])


