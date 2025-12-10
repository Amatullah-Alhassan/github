def count_nucleotides(dna):
    dna = dna.upper()
    return {
        "A": dna.count("A"),
        "C": dna.count("C"),
        "G": dna.count("G"),
        "T": dna.count("T")
    }

sequence = input("Enter DNA sequence: ")
counts = count_nucleotides(sequence)
print(counts)
