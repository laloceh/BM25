#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:32:31 2019

@author: eduardo
"""
from gensim import corpora
from gensim.summarization import bm25
from nltk.stem.porter import PorterStemmer
from gensim.summarization.bm25 import get_bm25_weights

import itertools
import numpy as np

p_stemmer = PorterStemmer()

q_context = [
"""Please note, there are 4 sizes (10, 10.2, 14, and 16 inches) of the same case type; I am writing a review of the 16-inch case.\
This is a well-made but relatively inexpensive bag for a laptop PC. It is so light that I can barely feel its weight, but it still has sufficient padding to \
protect its contents against bumps during everyday use.This is NOT the kind of case with zippers that can be pulled further to the left and right sides when \
you open the bag. In other words, the opening for you to put in and take out things is very small. Does this matter? Yes, if you have a laptop \
PC that measures diagonally 15.6 to 16 inches. The fit is snug, and because of the narrow opening, putting in and taking out a computer is not that smooth and easy. \
Although the zippers are plastic, there is a chance of them scraping against the computer's edges. I would not recommend this case if you have concerns about this aspect. \
If your computer is a netbook, which is about 10 inches diagonal, then this case will be fine.There is an USB thumb drive pocket in the main compartment, \
where the computer is stored, but I feel it is not a good location, because it is likely to chafe against the laptop computer. There are two side pockets. \
I use the larger one to store AC adapter, cord, mouse pad, and mouse.I deem this bag more suitable for carrying smaller laptops. It is not suitable for\
 15.6 to 16-inch laptops because of the tight fit.Update (2-4-2011):Case Logic has another 16-inch case that zipper opens three sides instead of just one. \
 It is called Case Logic VNCi-116 Value 16-Inch Laptop Briefcase. It will easily fit any 16-inch notebook computer. Even my 17.3-inch HP DV7 can be accommodated \
 in the case. You can read my review on its web page on Amazon.com.""",
"""This laptop bag is very well padded inside that I almost wanted this bad formy cameras. The design looks very simple, yet the interior pockets andpadding are \
very well made. Because of its cloth material, it feels littlebit cheap, but then again it is very light. There is also enough room fortwo laptops, \
maybe one 13 inch Mac book Pro and a 10 inch Net book, with allthe power blocks in the front pocket. There is an additional small pocketfor a cell phone or \
other small accessories, and I liked this pocket a lotbecause it is easy to reach, not to mention its location is convenient. Icould not find any cons about this bag, \
not only because it comes with ashoulder strap, but also because it has a "25 Years Quality Guarantee"stamp. I probably won't use this bag for 25 years, but it is \
good to knowthat the company guarantees its product. Also, if one prefers to use thisbag for carrying light, thin books/notebooks for classes or conferences,this\
 bad works well for this purpose as well. For this bag's weight andquality, the price is ideal.""",
"""I recently purchased an iPad2 and needed a quality carry case that would fit the iPad2 and my Kindle. TheCaselogic VNA210 10.2-Inch Netbook/iPad Attache \
(Black)was the perfect choice! Not only was the price great, but the case easily holds my iPad2 (w/Smart Cover) and Kindle (in it's own case) together, \
with plenty of room. The accessories pocket has room for my USB drive, charge cables, and more. The outer pocket also fits my iPhone 3GS (barely, but it does). \
Quality is great, very sturdy, and well padded. It is small and easy to carry, exactly what I was looking for.""",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
"""I've beat this case to death with my HP Slate and accessories.  That's why I ordered Case Logic for my laptop.  It holds up to my heavy use.""",
"""I just bought an ASUS 15.6 inch laptop and wanted a simple bag to carry it with me. I saw and ordered this one. It is just what I wanted. The laptop is 10 inch \
by 15 inch and about 1 inch thick. I leave the wireless mouse dongle and a micro USB flash drive in their USB ports, so add another 1/2 inch to the width (15.5 inches) \
It fits perfectly in the bag with a little room to spare. I know it is a vertical loading case and I prefer that. Only the top unzips, you must slide the laptop \
up or slide it out lying flat on a table. There is sufficeint padding to protect the laptop from "most dings". The power block, cables and mouse fit in the front\
 pocket and actually adds very little to the bulkiness of the case. I don't plan on loading it up with extras, so this bag works out just right. It fits all \
 the basics without any problems."""
]

print q_context


candidates = [
"""I look at a lot of shoulder bags and this one is perfect. Love this bag.It protects my iPad Air, which is in a Air Bender 2v case and allows me to have accessories like an external  battery, spare cables and wall charger handy  along with a head set and business cards in a handy professional looking shoulder bag. On time delivery and it arrive as advertized.""",
"""light weight, nice design, well design.  I have always like all the Case Logic product, I have some other ones for more than 20 years that looks like and works like new still today. Recommend: yes!""",
"""I went from a 15&#34; dell laptop to a 13&#34; macbook pro and wanted a less bulky case. This fit the bill perfectly and is much nicer to carry around. It's nice that it has 2 main compartments I use the second one for my ipad and charger and the front panel is misc. stuff like phone chargers, pens etc...It's a nice case that travels well and the price is right.""",
"""There was an Amazon Basic version of this style but for a difference of $4.00 did not have the bells and whistles of the Case Logic model.  My MacBook Pro fits nicely in either of of the two main compartments.  It has many places to put things from a small thumb drive holder to pen and mouse pockets and a shoulder strap - or a iPad!""",
"""Outstanding design and manufacture combine to make this just about perfect for my laptop. It holds the laptop itself along with the charger brick, and a bunch of accessories and supplies comfortably while affording easy access. I especially like how the shoulder strap is positioned, to carry the laptop so that its center of gravity lines up with my body, making carrying and walking a whole lot easier. I would not have thought of that, but Case Logic did. All I can say is &#34;Wow!&#34;""",
"""Works fine with my MacBook Pro. Does not have as much room but it is acceptable and I am able to include another small item or two.""",
"""It's a lot bigger than I thought. I knew I shouldn't have listened to my husband. I wanted to get the smaller size. It's a little big for my Kindle 8,9 but I can use it for many things. It's a strong canvas type and well padded. Has 3 seperate padded sections And one small section, good for a cell or wallet (the outside of this pocket isn't padded). Overall I'm very satisfied with this.""",
"""For the price you cannot go wrong.  It is nice and well designed.  Works well with netbooks and with the ipad (including the smart case).""",
"""This bag is a lot smaller than I expected, but I do put it to good use.  It fits my iPad perfectly, but doesn't really fit much more.  It does have a lot of nice pockets for accessories, but I would have preferred a little bitter pouch to carry more things.""",
"""I use this bad to lug around both my 15" Macbook Pro, a power plug, and an iPad in, and I have to say, I am VERY impressed with the Caselogic bag. It is well  made, has a very comfortable handle and strap, and simply works. If you have need to bring a LOT of gear, this is not the bag for you. But if you only need to carry a few things, you should consider this page. It works well, and I really like it."""
]
print len(candidates)


article_list = []

for a in candidates:
    a_split = a.replace('?', ' ').replace('(', ' ').replace(')',' ').split(' ')
    stemmed_tokens = [p_stemmer.stem(i) for i in a_split]
    article_list.append(stemmed_tokens)

print article_list


# Join the context into a single document
single_q_context = [x for x in q_context]
print single_q_context
single_q_context = ' '.join(single_q_context)
print single_q_context
print len(single_q_context)

P

## bm25
bm25model = bm25.BM25(article_list)

# Average IDF
average_idf = sum( map( lambda k: float(bm25model.idf[k]), bm25model.idf.keys())) / len(bm25model.idf.keys())
print average_idf


### Scores
scores = bm25model.get_scores(q_context_list[0], average_idf)

print scores

most_sim = np.argsort(-np.asarray(scores))      # To be in descending order
print most_sim

print candidates[most_sim[0]]

print candidates[most_sim[1]]


