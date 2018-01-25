"""
Skrip ini maunya aku pakai untuk menghitung load dari masing-masing node berdasarkan
informasi dependency ratio (dari graph yang dihasilkan oleh xl-stage.
Asumsinya, besaran load masing-masing chip akan berkorelasi dengan traffic load (seperti
yang dihasilkan dengan plot matlab), tapi sepertinya TIDAK berkorelasi.

Skrip ini butuh file dag_25Nodes.Traffic.Volume.Ratio.Raw
Sedangkan file dag_25Nodes.Traffic.Volume.Ratio.Raw didapat dari file .gv yang dah aku olah
pakai gedit.
"""
with open("dag_25Nodes.Traffic.Volume.Ratio.Raw", "r") as f:
    vol = [0.0 for _ in range(25)]
    for line in f:
        splt = line.split(":")
        lterm = splt[0].split(",")
        src = int(lterm[0])
        des = int(lterm[1])
        val = float(splt[1])
        # iterate the sources and dests
        if src <= 25:
            vol[src-1] += val
        if des <= 25:
            vol[des-1] += val

with open("dag_25Nodes.Traffic.Volume.Ratio.Result", "w") as f:
    for v in vol:
        f.write(str(v))
        f.write("\n")


