[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub issues](https://img.shields.io/github/issues/mtplr/blacomcalc)](https://github.com/mtplr/topspin-to-csv/issues)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# topspin-to-csv

A very simple Python script to generate a normal X/Y csv file from a Bruker TopSpin® .txt file

## Usage

1) Open Bruker's TopSpin® and export the current view through: Right Click > Save Display Region To... > A text file for use with other programs (leave all default). A plain text file will be saved. Let's say you named it as `namefile.txt`
2) Launch the python script in the same folder with the command: `topspin-to-csv.py -f filename.txt`
3) A new file will be generated: `namefile.csv`. Now you can open it with Excel, Origin, QtiPlot or whatever.

Enjoy! ✨

## Acknowledgements
Many thanks to **Glenn Facey** 🙏🏼 and to his hidden gem in the web, found after many **days** of research, to have provided us all with the algorithm to extract such data: [University of Ottawa NMR Facility Web Site](https://u-of-o-nmr-facility.blogspot.com/2014/02/getting-xy-ascii-data-from-topspin.html).
