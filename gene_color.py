import tkinter, math, string
# base_col = dict({'A':"red", 'C':"orange", 'G':"yellow", 'T':"brown"})
base_col = dict({'A':"red", 'C':"blue", 'G':"yellow", 'T':"green"})

### draw a grid of color blocks
# n: absolute position in the grid
# width: width of the grid
# color: color of the block
# bs: block size (the size in pixels of each block)
def position_color_block(canvas, n, width=16, color="red", bs=5):
    row = n // width
    col = n % width
    #print(f"({row},{col})")
    canvas.create_rectangle(col*bs,row*bs,bs+col*bs,bs+row*bs, fill=color)


def gene_colour(canvas, width, seq, bs=5):
    #print(f"len(seq) = {len(seq)}")
    for i in range(0,len(seq)):
        position_color_block(canvas, i, width, base_col.get(seq[i],"black"), bs)


def tk_gene_colour(seq, blocksize=5, strip=True):
    root = tkinter.Tk()
    if strip:
        print("stripping")
        seq = seq.translate(str.maketrans('', '', string.whitespace))
    length = len(seq)
    dim = round(math.sqrt(length),0)
    if dim*dim < length:
        dim = dim + 1
    size = dim * blocksize
    print(f"len={length}; dim={dim}; size={size}")
    cv = tkinter.Canvas(root, bg="white", height=size, width=size)
    
    gene_colour(cv, dim, seq, blocksize)
    
    cv.pack()
    root.mainloop()


# Read gene sequence from file and print color blocks:
def tk_blocks_from_file(filepath):
    with open (filepath, "r") as gene_file:
        seq = gene_file.read()
    
    tk_gene_colour(seq,5,True)


if __name__ == "__main__":
    #tk_gene_colour("ATTTACGGCATGGTAATCCTCGAGCGTGTAGGC  G")
    #tk_gene_colour("ATTTACGGCATGGTAATCCTCGAGCGTGTAGGC GATTTACAGTCGGCATGGAGCGTGTAG GATTTACGGCATGGTAATCCTCGAGCGTGTAGGC  GATTTACGGCATGGAGCGTGTAGGATTTACGGCATGGAGCGTGTAG",10)
    tk_blocks_from_file("covid-19.txt")