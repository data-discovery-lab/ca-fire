library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

filePath = "/home/long/TTU-SOURCES/ca-fire/data/wordcloud.txt"
text = readLines(filePath)



docs <- Corpus(VectorSource(text))

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)

set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 20,
          max.words=150, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))