
#DNA to RNA and codon determination:
DNA= input("Enter a DNA sequence: ").upper().strip()
RNA=DNA.replace("T", "U")
print(f"The transcribed RNA sequence is {RNA}")
RNA_start_codon=["AUG"]
RNA_start_codon_found=False
RNA_stop_codon=["UAG", "UGA", "UAA"]
RNA_stop_codon_found=False
if len(RNA)%3!=0:
    print("WARNING!!!, not accurate RNA length for codon determination")
else:
    for i in range(0,len(RNA),3):
        if RNA[i:i+3] in RNA_start_codon:
            print(f"Start codon present at position {i}")
            RNA_start_codon_found=True
        if RNA[i:i+3] in RNA_stop_codon:
            print(f"RNA stop codon present at position {i}")
            RNA_stop_codon_found=True
    if not RNA_start_codon_found:
        print("No start codon found")
    if not RNA_stop_codon_found:
        print("No stop codon found")
    
