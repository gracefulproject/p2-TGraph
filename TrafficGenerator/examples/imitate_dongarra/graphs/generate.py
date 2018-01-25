

with open('dag0000.gv', 'w') as fgv:
    fgv.write("digraph {\n  splines=true;\n\n");
    fgv.write("node [margin=0 fontname=arial fontcolor=black fontsize=12 shape=circle width=0.5 fixedsize=true style=filled fillcolor=powderblue]\n\n")
    for i in range(1,105):
        str = '  {} [Label=\"P{}\"]\n'.format(i,i)
        fgv.write(str)
    fgv.write("rankdir=LR\n\n")
    fgv.write("edge [margin=0 fontname=arial fontcolor=black fontsize=12]\n\n")

    
