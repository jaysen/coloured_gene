import tkinter, math, string

base_col = dict({'A':"red", 'C':"orange", 'G':"yellow", 'T':"brown"})
#base_col = dict({'A':"red", 'C':"blue", 'G':"yellow", 'T':"green"})


### draw a grid of gene base sequences as coloured blocks 
# seq: sequence of base (GTAC)
# bs: block size (the size in pixels of each block)
# strip: boolean strip whitespaces or not
def tk_gene_colour(seq, bs=5, strip=True, borders=True, title="gene color"):
    root = tkinter.Tk()
    root.title(title)
    
    if strip: # strip whitespaces
        seq = seq.translate(str.maketrans('', '', string.whitespace))
    
    # calc dimensions of grid and size of canvas
    length = len(seq)
    dim = round(math.sqrt(length),0)
    if dim*dim < length:
        dim = dim + 1
    size = dim * bs
    print(f"len={length}; dim={dim}; size={size}")

    cv = tkinter.Canvas(root, bg="white", height=size, width=size)
    
    for i in range(0, len(seq)):
        row = i // dim
        col = i % dim
        colour = base_col.get(seq[i],"black")
        if borders:
            bordercol = "black"
        else:
            bordercol = colour
        cv.create_rectangle(col*bs, row*bs, bs+col*bs, bs+row*bs, outline=bordercol, fill=colour)
    
    cv.pack()
    root.mainloop()


### Read gene sequence from file and print color blocks:
# filepath: path to text file with sequence data (contains sequences of characters each of GTAC)
# blocksize: size of each colored block in pixels
# strip: strip whitespaces or no
# borders: use borders around each block or no
def tk_blocks_from_file(filepath, blocksize=6, strip=True, borders=True, title=""):
    with open (filepath, "r") as gene_file:
        seq = gene_file.read()
    if len(title) == 0: title = filepath
    tk_gene_colour(seq, blocksize, strip, borders, title=title)


if __name__ == "__main__":
    #tk_gene_colour("ATTTACGGCATGGTAATCCTCGAGCGTGTAGGC  G")
    #tk_gene_colour("ATTTACGGCATGGTAATCCTCGAGCGTGTAGGC GATTTACAGTCGGCATGGAGCGTGTAG GATTTACGGCATGGTAATCCTCGAGCGTGTAGGC  GATTTACGGCATGGAGCGTGTAGGATTTACGGCATGGAGCGTGTAG",10)
    
    tk_blocks_from_file("covid-19.txt", blocksize=4, borders=True, title="COVID-19")
    tk_blocks_from_file("hiv1.txt", blocksize=4, borders=True, title="HIV-1")


### testing with the following viral sequences:
#covid-2 https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
#hiv-1   https://www.ncbi.nlm.nih.gov/nuccore/9629357
