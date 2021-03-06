## iRep

iRep is a method for determining replication rates for bacteria from single time point metagenomics sequencing and draft-quality genomes.

The method is described in:

["Measurement of bacterial replication rates in microbial communities"](http://dx.doi.org/10.1038/nbt.3704) - Christopher T. Brown, Matthew R. Olm, Brian C. Thomas, Jillian F. Banfield (*Nature Biotechnology* 2016).

## Installation:

`pip install iRep`

## Scripts:

`iRep` -> measure replication rates using draft-quality genome sequences

`iRep_filter` -> combine and/or filter iRep output

`bPTR` -> measure replication rates using complete genome sequences (modified from Korem et al. *Science* 2015)

`gc_skew` -> calculate GC skew across complete genome sequences

## Example usage:

### iRep

```$ iRep -f sample_data/l_gasseri.fna -s sample_data/l_gasseri*sam -o test.iRep```

### bPTR

```$ bPTR -f sample_data/l_gasseri.fna -s sample_data/l_gasseri*sam -o test.bPTR.tsv -plot test.bPTR.pdf -m coverage```

### GC Skew

```$ gc_skew -f sample_data/l_gasseri.fna```

#### Example output is provided in sample_output. 

## Usage notes:

Running iRep and bPTR requires that you have genome sequences for each of the organisms for which you want to measure replication rates. Each program takes the file paths to each of the genomes, in separate FASTA files, as input. bPTR requires complete (closed) genome sequences, and iRep requires high-quality draft genomes (>=75% complete, <=175 fragments/Mbp sequence, and <=2% contamination). Both methods are most accurate when the genomes have been assembled from metagenomes from the samples being studied, or if it is known that an organism is present in the system with a highly similar genome sequence. The second set of inputs are mapping files in SAM format, which should be generated by mapping DNA sequencing reads against assembled genomes using Bowtie2. In this case, provide the path to each SAM file generated for each sample. 

Please note that high levels of strain variation will confound results. 

iRep and bPTR.py output both a table (.tsv file) of results and a PDF with plots showing genome coverage measurements used for calculating replicaiton rates.

### IMPORTANT:

Both iRep and bPTR require ordered SAM files that can be generated using the Bowtie2 --reorder flag. Ordered SAM files, where both reads representing a set of paired reads are ordered one after the other, are requred for these scripts to filter reads based on mapping quality. If the SAM file is not sorted, the scripts will make incorrect choices about which mapped reads to include when calculating coverage. This only applies when using a mapping quality cutoff; however, using a quality cutoff is recommend as it helps with off-target read mapping.

### Additional information:

See iRepValues.pdf for more information on interpreting iRep results. 
