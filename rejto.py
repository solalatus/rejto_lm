
class Rejto_corpus():

    def __init__(self,path="rejto_all.txt"):
        self.path = path
        self.raw_sents = []
        self.sentences = []
        self.all_words = set()

        with open(self.path, "r") as fil:
            for sent in fil:
                self.raw_sents.append(sent)

        for sent in self.raw_sents:
            current_sent = []
            for word in sent.split(" "):
                word_tmp = word.replace("\n","").replace(" ","")
                if word_tmp !="":
                    self.all_words.add(word.replace("\xad",""))
                    current_sent.append(word.replace("\xad",""))
            if current_sent != []:
                self.sentences.append(current_sent)

    def words(self):
        return list(self.all_words)

    def sents(self):
        return self.sentences

    def n_words(self):
        return len(self.all_words)

    def n_sents(self):
        return len(self.sentences)
#print("run at import")
