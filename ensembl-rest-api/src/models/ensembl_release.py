class EnsemblRelease:
    def __init__(self, version):
        self.version = version

    def generate_download_links(self, species_name):
        return {
            "dna": f"ftp://ftp.ensembl.org/pub/release-{self.version}/fasta/{species_name}/dna/{species_name}.*.dna.toplevel.fa.gz",
            "cdna": f"ftp://ftp.ensembl.org/pub/release-{self.version}/fasta/{species_name}/cdna/{species_name}.*.cdna.all.fa.gz",
            "ncrna": f"ftp://ftp.ensembl.org/pub/release-{self.version}/fasta/{species_name}/ncrna/{species_name}.*.ncrna.fa.gz"
        }