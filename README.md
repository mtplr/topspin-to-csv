# topspin-to-csv
Python script to generate a normal X/Y csv file from a Bruker TopSpin .txt file

Usage:

1) Open Bruker's TopSpin and export the current view through: Right Click > Save Display Region To... > A text file for use with other programs (leave all default). A plain text file will be saved. Let's say you named it as `namefile.txt`
2) Launch the python script in the same folder with the command: `topspin-to-csv.py -f filename.txt`
3) A new file will be generated: `namefile.csv`. Now you can open it with Excel, Origin, QtiPlot or whatever.

Enjoy! 
