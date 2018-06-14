# Modules
import os
import re

textfile = os.path.join(".", "raw_data", "paragraph_1.txt")

delims = "(?&lt;=[.!?]) +"
wordcounts = []

with open(textfile, 'r') as text:

 
    
    lines = text.read()
    print(lines)
    words = lines.split()
    average = sum(len(word) for word in words) / len(words)

    sents = lines.split(",") + lines.split(".")
    avg_len = sum(len(lines.split()) for lines in sents) / len(sents)

    print("```") 
    print("Paragraph Analysis") 
    print("----------------------------")    
    print("Approximate Word Count: " + str(len(lines.split(" "))))
    print("Approximate Sentence Count: " + str(len(lines.split(".") + lines.split(","))  ))
    print("Approximate letter count (per word) " + str(average))
    print("Average Sentence Length: " + str(avg_len))
