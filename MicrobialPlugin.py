import sys
import PyPluMA

# This script takes in the reads that are proposed by bmtagger to be human, and filteres them out of the original fastq file.

# Note: Built from MetaWRAP (Uritskyi et al, 2018) "select_human_reads.py" script
# Available at: https://github.com/bxlab/metaWRAP
# Also under license from MIT, copy included


class MicrobialPlugin:
    def input(self, filename):
       self.parameters = dict()
       for line in open(filename, 'r'):
            line = line.strip()
            contents = line.split('\t')
            self.parameters[contents[0]] = contents[1]

       # Load in the human reads:
       self.human={}
       for line in open(PyPluMA.prefix()+"/"+self.parameters["bmtaggerfile"]):
          self.human[line.strip()]=None

    def run(self):
        pass

    def output(self, filename):
       # Print out the fastq file line by line unless the read is human:
       skip=False
       outfile = open(filename, 'w')
       for i, line in enumerate(open(PyPluMA.prefix()+"/"+self.parameters["sequences"])):
        if i%4==0:
         if line[1:].split("/")[0].split()[0] in self.human: 
          skip=True
         else: 
          skip=False
        if skip==False: outfile.write(line.rstrip()+"\n")

