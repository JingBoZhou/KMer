# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:16:38 2017

@author: zhoujb
"""

#from __future__ import print_function, division #If python2,add this line
import os
from itertools import product

# Where to save the data
PROJECT_ROOT_DIR = "."  

class KMer:
    def __init__(self,file_name,k_mer=3):
        self.file_name = file_name
        self.k_mer = k_mer
        
    def k_mer_dna(self,number):

        return {''.join(x):0 for x in product('ACTG', repeat=number)}

    def count_k_mer(self,seq,n):
        k_mer_dna_dict = self.k_mer_dna(n)
        for i in range(len(seq) - n + 1):
            count = seq[i:i+n]
            if count in k_mer_dna_dict:
                k_mer_dna_dict[count] += 1

        return k_mer_dna_dict

    def write_file(self,file_name,k_mer):
        output_file = open(os.path.join(PROJECT_ROOT_DIR,'k_mer_output.tsv'),'w')
        seq = ''

        for line in open(os.path.join(PROJECT_ROOT_DIR,file_name)):
            line = line.rstrip()
            if line.startswith(">") and seq == '':
                output_file.write('\t'.join(self.k_mer_dna(k_mer).keys())+'\n')

            elif not line.startswith('>'):
                seq += line

            elif line.startswith('>') and seq != '':
                output_file.write('\t'.join([str(x) for x in self.count_k_mer(seq,k_mer).values()])+'\n')
                seq = ''

        output_file.write('\t'.join([str(x) for x in self.count_k_mer(seq,k_mer).values()])+'\n')
        output_file.close()

    def print_k_mer(self,file_name='k_mer_output.tsv'):
        for line in open(os.path.join(PROJECT_ROOT_DIR,file_name)):
            line = line.rstrip()
            print(line)

    def main(self):
        self.write_file(self.file_name,self.k_mer)
        self.print_k_mer(file_name='k_mer_output.tsv') 