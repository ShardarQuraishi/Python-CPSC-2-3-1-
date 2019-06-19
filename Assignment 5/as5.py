import time
def cosine_similarity(vec1, vec2):
    c = 0
    for i in vec1:

        for j in vec2:

            if i == j:
                x = vec1[i] * vec2[j]
                c += x

    u = 0
    for a in vec1:
        s = vec1[a] ** 2
        u += s

    v = 0
    for b in vec2:
        m = vec2[b] ** 2
        v += m

    cos_sim =float( c / ((u * v) ** 0.5))

    return cos_sim



def build_semantic_descriptors(sentences):

    l = []

    for i in sentences:
        for j in i:
            if j not in l:
                l.append(j)


    dict={}

    for x in l:
        d = {}

        for (a, b) in enumerate(sentences):

            if x in b:

                for k in b:
                    if k == x:
                        continue
                    if k not in d:
                        d[k] = 1
                    else:
                        d[k] += 1

        dict[x] = d

    return dict


def build_semantic_descriptor_from_files(filenames):

    with open(filenames[0], "r",encoding="utf-8") as myfile:

        data = ' '.join([line.replace('\n', '') for line in myfile.readlines()])
        data.lower()
        replacements = ('!', '?')
        punctuations=('--',',',':','-',';',"'",'"')
        for p in punctuations:
            data=data.replace(p," ")
        for r in replacements:
            data = data.replace(r, '.')

        words = []
        words.extend(data.split("."))

        lst=[]
        for i in words:
            a=i.split()
            lst.append(a)

        large=build_semantic_descriptors(lst)

        return large

def most_similar_word(word,choices):
    library=(build_semantic_descriptor_fromfiles())

    ans_list=[]

    for (i,j) in enumerate(choices):


        if word in library:
            v1=(library[word])


            if j in library:
                print('choices',j)
                v2=library[j]

                result = (cosine_similarity(v1, v2))

                print(result)

                ans_list.append(result)
                print('answer', ans_list)

            else:

                ans_list.append(-1)

    print(ans_list)

    y=max(ans_list)
    for (a,b) in enumerate(ans_list):
        if b==y:

            print(choices[a],b)
            return (choices[a],b)

        else:
            continue


#build_semantic_descriptor_fromfiles()
tic=time.clock()
filenames=['Proust.txt','Tolstoy.txt']
build_semantic_descriptor_fromfiles(filenames)
toc=time.clock()


print('last time',toc)
word='sleep'
#choices=['happy','paint','night','dhon']
#most_similar_word(word,choices)
#toc=time.clock()
#print(toc)
