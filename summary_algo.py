import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
import re
import io

def generate_summary(inputValue, length):
#     inputValue="""
#     Maria Sharapova has basically no friends as tennis players on the WTA Tour.
# The Russian player has no problems in openly speaking about it and in a recent interview she said: 'I don't really hide any feelings too much.
# When I'm on the courts or when I'm on the court playing, I'm a competitor and I want to beat every single person whether they're in the locker room or across the net.
# So I'm not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match.
# I say my hellos, but I'm not sending any players flowers as well.
# Uhm, I'm not really friendly or close to many players.
# I have not a lot of friends away from the courts.'
# When she said she is not really close to a lot of players, is that something strategic that she is doing?
# I think just because you're in the same sport doesn't mean that you have to be friends with everyone just because you're categorized, you're a tennis player, so you're going to get along with tennis players.
# I have friends that have completely different jobs and interests, and I've met them in very different parts of my life.
#     """
    sentences = []
    sentences.append(sent_tokenize(inputValue))

    sentences = [y for x in sentences for y in x]
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    clean_sentences = [s.lower() for s in clean_sentences]
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
    #Extract word vector
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()
    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)
    # similarity matrix
    sim_mat = np.zeros([len(sentences), len(sentences)])
    from sklearn.metrics.pairwise import cosine_similarity
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
    import networkx as nx

    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    # Specify number of sentences to form the summary
    print(ranked_sentences[0])
    print("********")
    # sn = 5
    sn = length

    summary_list = ""

    # Generate summary
    for i in range(sn):
        print(ranked_sentences[i][1])
        summary_list+=ranked_sentences[i][1]

    return summary_list

# if __name__ == "__main__":
#     generate_summary()
