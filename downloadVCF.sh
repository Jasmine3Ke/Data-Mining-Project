#! /usr/bin/bash --


webPrefix="ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502"
geneFile="Homo_sapiens.GRCh38.102.gtf"
logfile="log.txt"
>$logfile
for i in {1..22..1}
do
	wget $webPrefix"/ALL.chr"$i".phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
	Rscript --verbose process_vcf.R "ALL.chr"$i".phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz" $geneFile "1kgenomes_variants_af0.01_chr${i}_genebodyOnly" 2>&1 | tee -a $logfile
done
Rscript mergeDat.R
cat 1kgenomes_variants_af0.01_chr{1..22}_genebodyOnly.dat > 1kgenomes_variants_af0.01_autosome_genebodyOnly.dat
cat 1kgenomes_variants_af0.01_chr{1..22}_genebodyOnly.genes > 1kgenomes_variants_af0.01_autosome_genebodyOnly.genes
cat 1kgenomes_variants_af0.01_chr{1..22}_genebodyOnly.rownames > 1kgenomes_variants_af0.01_autosome_genebodyOnly.rownames
cat 1kgenomes_variants_af0.01_chr{1..22}_genebodyOnly.colnames > 1kgenomes_variants_af0.01_autosome_genebodyOnly.colnames