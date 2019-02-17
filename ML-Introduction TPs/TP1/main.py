from random import sample
from collections import Counter

fn = 'fr_gsd-ud-train.conllu'

def valideLine(line):
    return not any([line.startswith('#'), '-' in line.split('\t'), not line.strip()])

def q1_inter(filename='fr_gsd-ud-train.conllu') :
    n_tokens = 0
    for line in open(filename, 'r', encoding='UTF-8'):
        if valideLine(line):
            n_tokens += 1
    print ("number of tokens : ", n_tokens)

def q1bis(filename='fr_gsd-ud-train.conllu') :
    n_tokens = sum(1 for line in open(filename, 'r', encoding='UTF-8') if valideLine(line))
    print (n_tokens)


def q2(filename='fr_gsd-ud-train.conllu') :
    print (len({line.split('\t')[1] for line in open(filename, 'r', encoding='UTF-8') if valideLine(line)}))
    
def q3str(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = ''
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            sentences.append(sentence)
            sentence = ''
        else :
            if valideLine(line):
                sentence = sentence + line.split('\t')[1] + ' '
    return sentences


def q3list(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = []
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            sentences.append(sentence)
            sentence = []
        else :
            if valideLine(line):
                sentence.append(line.split('\t')[1])
    return sentences

def q3str(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = ''
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            sentences.append(sentence)
            sentence = ''
        else :
            if valideLine(line):
                sentence = sentence + line.split('\t')[1] + ' '
    return sentences
def q3list(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = []
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            sentences.append(sentence)
            sentence = []
        else :
            if valideLine(line):
                sentence.append(line.split('\t')[1])
    return sentences

def q3all(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = []
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            sentences.append(sentence)
            sentence = []
        else :
            if valideLine(line):
                sentence.append(line)
    return sentences

def q3allyeild(filename='fr_gsd-ud-train.conllu') :
    sentences = []
    sentence = []
    for line in open(filename, 'r', encoding='UTF-8'):
        #print(line)
        if not line.strip() : # is a sentence
            yield sentence
            sentence = []
        else :
            if valideLine(line):
                sentence.append(line)

def q4(sentence):
    n_verb = 0
    n_passive_cons = 0
    for line in sentence:
        l = line.split('\t')[7]
        if 'nsubj' in l :
            n_verb += 1 
        if 'nsubj:pass' == l :
            n_passive_cons += 1
    return n_verb, n_passive_cons

def q5(trys):
    for i in trys:
        sum_v = 0
        sum_pass = 0
        tup = [q4(s)for s in sample(q3all(), i)]
        for x,y in tup :
            sum_v += x
            sum_pass += y
        print(sum_pass/sum_v)
    
q5([5, 50, 100, 1000, 5000, 10000, 20000, 50000])

# q6 : construire les donnees a generator quand on en a besoin, il renvoie une list de une ligne
#    le type de content est <class 'generator'>

#    recuperer tous les ligne et les traduire a une matrix

#   comme apres on a besoin de utiliser 'sample' ou Population must be a sequence or set. 
#   autre raison, c'est prendre n lignes aleatoire sur tous les ligne, donc il faut tous les lignes dans le memoire

#   ligne 17 : on prend n mots de la list de texte aleatoire sur tous les ligne et calculer les nombres de fois chaque truc apparait dans la list on prend
#   ligne 19 : on calculer le sommation de fois du mot 'nsubj' apparait

def sequence_to_matrix(s):
    matrix = []
    lines = s.split('\n')[:-1]
    #map(lambda line: matrix.append(line.split(' ')), lines)
    for line in lines:
        columns = line.split('\t')
        matrix.append(columns)
    return matrix


def get_sequences(fileneme):
    file = open(fileneme, mode='r', encoding='UTF-8')

    sequences = []
    sequence = ''

    try:
        for line in file:
            if len(line) == 1:
                sequences.append(sequence)
                sequence = ''
            else:
                if valideLine(line):
                    sequence += line
    finally:
        file.close()

    return sequences


def calulate_num_of_word_by_sequence(s):
    list = [line[1] for line in s]
    set  = {line[1] for line in s}
    return len(set)




#sequences = get_sequences(fn)

#last_matrix = sequence_to_matrix(sequences[-1])

#print(last_matrix)
#print(calulate_num_of_word_by_sequence(last_matrix))

