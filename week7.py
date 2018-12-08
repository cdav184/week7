#!/usr/bin/env python

#For the different bases in the DNA sequences calculate the frequencies.

dnaSeq = input ("Enter your DNA sequence:")

#Begin calculating the entire length of the given sequence.
print ("Total Sequence Length:")
print (len(dnaSeq))

#count total number of A's.
print ("Number of As:")
print (dnaSeq.lower().count ('a'))

#count total number of C's.
print ("Number of Cs:")
print (dnaSeq.lower().count ('c'))

#count total number of G's.
print ("Number of Gs:")
print (dnaSeq.lower().count ('g'))

#count total number of T's.
print ("Number of Ts:")
print (dnaSeq.lower().count ('t'))

# DB: Good, although this won't work properly if the sequence is upper case. You can
#     avoid this by adding .lower() after dnaSeq (see above). Also, it's a good idea to 
#     only use .sh for shell scripts. Instead, use .py for python.