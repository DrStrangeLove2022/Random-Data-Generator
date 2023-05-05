import random
from random import choice
def lorem_ipsum():
    sentences = []

    a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    b = "Quisque vitae varius ex, eu volutpat orci. "
    c = "Aenean ullamcorper orci et vulputate fermentum. "
    d = "Cras erat dui, finibus vel lectus ac, pharetra dictum odio. "
    e = "Nullam tempus scelerisque purus, sed mattis elit condimentum nec. "
    f = "Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc. "
    g = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. "
    h = "Proin ipsum purus, laoreet quis dictum a, laoreet sed ligula. "
    i = "Integer ultricies malesuada quam. "
    j = "Cras vel elit sed mi placerat pharetra eget vel odio. "
    k = "Duis ac nulla varius diam ultrices rutrum. "

    sentences.append(a)
    sentences.append(b)
    sentences.append(c)
    sentences.append(d)
    sentences.append(e)
    sentences.append(f)
    sentences.append(g)
    sentences.append(h)
    sentences.append(i)
    sentences.append(j)
    sentences.append(k)

    n = random.randint(4, 19)
    length = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    paragraphs = []

    for i in range(1, n + 1):
        if i == 1:
            paragraph = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        else:
            paragraph = ''
        numofsentences = choice(length)
        for j in range(1, numofsentences + 1):
            sentence = choice(sentences)
            paragraph = paragraph + sentence
        paragraphs.append(paragraph)

    for x in paragraphs:
        return x

lorem_ipsum()