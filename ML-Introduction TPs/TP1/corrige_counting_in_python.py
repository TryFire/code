# Question 1: number of tokens
# -----------

# `standard' version

print("")
print("Question 1")
print("----------")

n_tokens = 0
for line in open("fr_gsd-ud-train.conllu", "r"):

    if line.startswith("#"):
        continue

    if "-" in line.split("\t")[0]:
        continue

    if not line.strip():
        continue

    n_tokens += 1

print(f"number of token (standard version): {n_tokens:,}")
    
# pythonic version:
n_tokens = sum(1 for line in open("fr_gsd-ud-train.conllu", "r") if not any([\
                                                                             line.startswith("#"),
                                                                             "-" in line.split("\t")[0],
                                                                             not line.strip()]))

print(f"number of token (pythonic version): {n_tokens:,}")

# Question 2: number of types
# -----------

print("")
print("Question 2")
print("----------")
n_types = len({line.split("\t")[1] for line in open("fr_gsd-ud-train.conllu", "r") if not any([\
                                                                             line.startswith("#"),
                                                                             "-" in line.split("\t")[0],
                                                                             not line.strip()])})
print(f"number of types in the corpus: {n_types:,}")

# Question 3: 
# -----------

def read_sentences(infile):
    # Note that this function reads all the file into memory which is
    # usually not a good idea (the file may be very large)
    data = infile.read()

    # do not return an empty sentence at the end of file
    return [d for d in data.split("\n\n") if d.strip()]


def stream_sentences(infile):

    data = []
    for line in infile:
        if not line.strip():
            yield "\n".join(data)
            data = []
            continue
        
        data.append(line.strip())

    if data:
        yield "\n".join(data)


print(f"#sentences: {len(read_sentences(open('fr_gsd-ud-train.conllu'))):,}")
        
assert read_sentences(open("fr_gsd-ud-train.conllu"))[0] == next(stream_sentences(open("fr_gsd-ud-train.conllu", "r")))
assert read_sentences(open("fr_gsd-ud-train.conllu"))[-1] == list(stream_sentences(open("fr_gsd-ud-train.conllu", "r")))[-1]

# Question 4: number of verbs and passive verbs in the sentence
def count_verbs(sentence):

    c = Counter(line.split("\t")[7] for line in sentence.split("\n") if not any([\
                                                                                 line.startswith("#"),
                                                                                 "-" in line.split("\t")[0]]))

    return sum(v for k, v in c.items() if "nsubj" in k), c["nsubj:pass"]



