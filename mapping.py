#!/usr/bin/python
import os
import json
import stemming
import getFreq

fd = open("../Spots_Tagme_apathetic_v3","r")
contents = fd.readlines()
for c in contents:
	communities = {}
	c = c.strip("\n")
	cList = c.split("\t")
	wordAm = cList[0]
	ambig = cList[1]
	
	if not os.path.exists("wikiConcepts/" + wordAm + "_wikiConcepts.json") and int(ambig) == 1:
			wikiConcepts = {}
			try:
					senses = json.load(open("../Cluster/Senses/" + wordAm + ".json", "r"))[wordAm]
					tfidf = getFreq.main(wordAm)
					for senseId in senses:
						max = 0
						match = ""
						finalMatch = ""
						senseWords = senses[senseId]
						for article in tfidf:
							print "wiki:", article
							sum = 0
							count = 0
							tfidfwords = tfidf[article] 
							article_length = len(tfidfwords)
							for word in senseWords:
								try:
									if "_" in word:
										wordList = word.split("_")
										for word in wordList:
											if stemming.main(word) in tfidfwords:
												count += 1
											sum += tfidfwords[stemming.main(word)]
									else:
										if stemming.main(word) in tfidfwords:
											count += 1
										sum += tfidfwords[stemming.main(word)]
								except:
									pass
							print "overlap:", count
							print "length:", article_length
							if article_length != 0:
								sum *= (float(count) ** 1.5)/(article_length)
							else:
								sum = float(0)
							print "sum final:", sum
							if sum > max:
								max = sum
								match = article
							print "Sum:", sum
						if match == "":
							finalMatch = None
						else:
							finalMatch = "https://en.wikipedia.org/wiki/" + match
						wikiConcepts[wordAm + "_" + str(senseId)] = finalMatch
						print "senseId:", senseId
						print "match:", match, ":", max
					json.dump(wikiConcepts, open("wikiConcepts/" + wordAm + "_wikiConcepts.json", "w"))
			except:
				pass
