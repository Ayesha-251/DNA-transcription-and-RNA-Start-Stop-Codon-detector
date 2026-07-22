##DNA to RNA and codon determination:
BIOLOGICAL SIGNIFICANCE:
RNA plays a central role in protein synthesis through the process of translation. The transcription of DNA to form RNA is a major biological aspect in protein formation.
RNA is the bridge that converts the genetic information present in the DNA to functional proteins. 
The complete set of RNA is the transcriptome of the cell, study of transcriptome(RNA) is highly important due to the fact that transcriptome varies cell to cell.
The study of RNA helps in understanding gene expression and gene regulation within cells.
INPUT: 
  A DNA sequence provided by user. 
On terminal: 
    Enter the DNA Sequence: 
OUTPUT: 
If the input sequence contains an invalid nucleotide:
On terminal:
    Enter a DNA sequence: ttgcy
    Invalid DNA sequence
For the Valid sequence, DNA sequence is transcribed into an RNA sequence by replacing T with U:
On terminal:
    Enter a DNA sequence: aaggattaacaa
    The transcribed RNA sequence is AAGGAUUAACAA
If RNA sequence is not in proper codon form: 
On terminal WARNING!!!, RNA SEQUENCE LENGTH IS NOT IN PROPER CODON LENGTH 
If RNA contains a start codon: 
  On terminal: 
    Enter a DNA sequence: cgtatgaccaat
    The transcribed RNA sequence is CGUAUGACCAAU
    Start codon present at position 3
    No stop codon found
If RNA contains a stop codon: 
  On terminal:  
    Enter a DNA sequence: aattaaccttaa
    The transcribed RNA sequence is AAUUAACCUUAC
    RNA stop codon present at position 3
    No start codon found 
If both start codon and stop codon are present: 
    On terminal:
      Enter a DNA sequence: atgacgtga
      The transcribed RNA sequence is AUGACGUGA
      Start codon present at position 0
      RNA stop codon present at position 6
No start or stop codon found:
    On terminal: 
      Enter a DNA sequence: aacgcagtc 
      The transcribed RNA sequence is AACGCAGUC
      No start codon found
      No stop codon found
CODE WORKING: 
The code takes DNA sequence from the user and convert it in Uppercase and remove leading and trailing white spaces.
The DNA sequence is validated to ensure it contains only valid nucleotides (A, T, G, and C). If the sequence contains any nucleotide other than "A", "T", "G", "C". It shows the message of Invalid DNA sequence on terminal and terminate the program.
If the sequence is valid the "T" Thymine present in DNA sequence is then changed to "U" Uracil which converts the sequence from DNA to RNA.
The transcribed sequence is printed on the terminal.
The code checks for the RNA sequence length to determine if proper codons can be formed. 
If the RNA sequence length is not divisible by 3, the program displays a warning and does not perform codon determination analysis. 
If formed it checks for the codons from the flag variable and shows the exact location of the start codon and stop codon. 
If no start codon or stop codon is detected after scanning the entire sequence, the program displays a message indicating their absence.
If the start codon is present the exact position of start codon on the terminal. 
The terminal shows no stop codon found, no start codon found and terminates the program.
