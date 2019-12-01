class Sentence:
    def __init__(self, text): 
        self.text = text
        self.words = text.split()
        
    def __iter__(self): 
        for i in self.words:
            yield i
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == "__main__":
    sent = Sentence("My name is Stephen")
    for i in sent:
        print(i)
    