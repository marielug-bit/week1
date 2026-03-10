#class DNA:
    #pass
    #class Chromosome:
        #pass
            #class Genes:
            #pass

import random 

class Gene:
    def __init__(self,value):
        if value not in {0,1}:
            raise ValueError('the value should be one or zero')
        self.value = value

    def mutate(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0

class Chromosome:
    def __init__(self,genes:list):
        self.genes = genes #list of 10 0 and 1
    
    def mutate(self):
        mutated = []
        for gene in self.genes:
            if random.random() < 0.5:
                mutated.append(gene.mutate())
            else:
                mutated.append(gene)
        self.genes = mutated
        return self
    
    def is_all_ones(self):
        return all(g.value == 1 for g in self.genes)

    def __repr__(self):
        return "".join(str(g.value) for g in self.genes)

class DNA:
    def __init__(self,chromosomes:list):
        self.chromosomes = chromosomes #list of 10 lists
    
    def mutate(self):
        mutated = []
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                mutated.append(chromosome.mutate())
            else:
                 mutated.append(chromosome)
        self.chromosomes = mutated
        return self
    
    def is_all_ones(self):
        return all(chrom.is_all_ones() for chrom in self.chromosomes)

    def __repr__(self):
        return "\n".join(str(c) for c in self.chromosomes)

class Organism:
    def __init__(self,DNA_object:DNA,evt):
        self.DNA_object = DNA_object
        self.evt = evt
    


    def mutate(self):
            # organism mutates its DNA with probability environment
            if random.random() < self.evt:
                self.DNA_object.mutate()
            return self
    
    def random_gene():
        return Gene(random.choice([0, 1]))

def random_chromosome():
    return Chromosome([random_gene() for _ in range(10)])

def random_dna():
    return DNA([random_chromosome() for _ in range(10)])


def run_simulation(num_organisms=20, environment=0.3, max_generations=1_000_000):
    organisms = [Organism(random_dna(), environment) for _ in range(num_organisms)]

    for generation in range(1, max_generations + 1):
        for org in organisms:
            org.mutate()
            if org.dna.is_all_ones():
                return generation, org  # stop when one succeeds

    return None, None


gen, winner = run_simulation(num_organisms=50, environment=0.3)
print(gen)
print(winner.dna)