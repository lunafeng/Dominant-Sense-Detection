#!/usr/bin/python
import os
import json
import ast
import networkx as nx
import community
def cluster(givenWord):
		clusters = {}
		top = 300
		try:
				g = nx.read_edgelist("Graphs/" + givenWord + "_Top" + str(top) + ".gh")
				partition = community.best_partition(g)
				print "partition:",partition
				for i in set(partition.values()):
					members = list_nodes = [str(nodes) for nodes in partition.keys() if partition[nodes] == i]
					clusters[str(i)] =  members  
				return clusters
		except:
			return None

fd = open("../Spots_Tagme_apathetic_v3","r")
contents = fd.readlines()
raws = [c.strip("\n").split("\t")[0] for c in contents if int(c.strip("\n").split("\t")[1]) == 1]
top = 300
raws = list(set(raws))
for word in raws:
		communities = {}
		givenWord = word
		if not os.path.exists("Senses/" + givenWord + ".json"):
				print givenWord
				clusters = cluster(givenWord)
				if clusters != None:
					communities[str(word)] = clusters
				comNew = json.dumps(communities)
				fd = open("Senses/"+ givenWord + ".json","w")
				fd.write(comNew)
