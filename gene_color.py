from colorama import Fore as FG
from colorama import Style as ST


# convert gene base string to color block
def gene_to_blocks(gene_seq, stripblanks=False):
    red = f"{FG.RED}■"
    yel = f"{FG.YELLOW}■"
    blu = f"{FG.BLUE}■"
    grn = f"{FG.GREEN}■"
    mag = f"{FG.MAGENTA}■"

    blocks = gene_seq.replace('A',red).replace('T',blu).replace('G',grn).replace('C',yel)
    if stripblanks:
        blocks = blocks.replace(' ','')
    return blocks


# Read gene sequence from file and print color blocks:
def print_blocks_from_file(filepath):
    with open (filepath, "r") as gene_file:
        seq = gene_file.read()
    print(gene_to_blocks(seq,True))



if __name__ == "__main__":
    print(gene_to_blocks("GTACAT TACTAA AGTAGT TGAGGT"))
    print(gene_to_blocks("GTACAT TACTAA AGTAGT TGAGGT",True))
    print_blocks_from_file("covid-19.txt")

