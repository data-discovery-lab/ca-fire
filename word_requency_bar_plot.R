library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

filePath = "/home/long/TTU-SOURCES/ca-fire/data/wordcloud.txt"
text = readLines(filePath)



docs <- Corpus(VectorSource(text))

docs <- tm_map(docs, removeWords, c(stopwords("english"),"via","chico", "like", "socalfiresjameswoods", 
                                    "one", "day", "butte", "see", "still", "area", "get"))


dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)

set.seed(1234)

num_words = 20
head(d, num_words)

barplot(d[1:num_words,]$freq, las = 2, names.arg = d[1:num_words,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Word frequencies")