# PolyElastic-cPRS
Composite PRS scores for Aging-associated diseases

This repository contains scripts for generating composite PRS scores for ageing-associated disorders. PolyElastic-cPRS runs as a command-line program and requires imputed genomes according to the hg19 genome assembly in PLINK BED format.

## NOTE

Accompanying summary statistic data is not included in this repository. Please contact directly for GWAS summary statistics.

Successful implementation of the pipeline requires the following dependencies:

## Prerequisite
[PRSice-2](https://www.prsice.info/)

R version 3.2.3 or higher

PLINK 1.90b or highr

Python 3.4.1 or higher

### Python libraries

- Python Data Analysis Library- pandas

- numpy

- sklearn.preprocessing

- random

- glob

- logging

## Basic usage

```bash
git clone https://github.com/RezaJF/PolyElastic-cPRS.git

cd PolyElastic-cPRS

./cPRS_generator.sh [PATH_to_PRSice] [PATH_to_imputed_BEDs] [OUTPUT_DIRECTORY]
```
- For accessing accompanying summary statistic data, please contact directly!

## Contact
For more update and instructions email me at: reza.jabal@einsteinmed.org


