# DominantSenseDetection

The assumption is people tend to use dominant senses of ambiguous words in daily life rather than all the formally defined senses on Wikipedia. Therefore, by analysing twitter content, we want to find dominant senses people use frequently presenting by Wikipedia entires.

The process includes two parts: 1) sense words detection and 2) sense mapping.

Sense Words Detection
The step aims to find dominant senses from tweets by creating a words graph for each ambiguous word, in the words graph, nodes are the words that are highly related with the ambiguous word, this can be obtained from previous word Semantic Relatedness by get top n words from the static distribution, edges are the semantic relatedness scores between each word pairs.

Usage
python createGraph.py

Then a clustering method is used to do cluster on the words graph, we assume words that are highly related should be clustered in the same cluster. Each cluster should present one sense. Therefore, by clustering the graph, we can find dominant senses for each target ambiguous word, the dominant senses are represented as a set of words so far.

Usage
python cluster.py

Sense Mapping
To better present the dominant senses, we want to map each set of dominant sense words to an valid Wikipedia entry. In order to do so, we compute similarity between each words set with Wikipedia's disambiguation pages. The entry with the highest score will be selected as the mapping.

