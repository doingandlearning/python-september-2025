headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]

# A function that finds the number of words in a line of text
def find_word_count(text):
  word_list = text.split()  # a list of the individual words
  word_count = len(word_list)  # the word count
  return word_count

list_of_word_lengths = []

for headline in headlines:
  word_count = find_word_count(headline)
  list_of_word_lengths.append(word_count)

print(list_of_word_lengths)


def find_keyword_in_headline(headlines, keyword):
  result = []

  for headline in headlines:
    for word in headline.split():
      if word.lower() == keyword.lower():
        result.append(headline) 

  return result

print(find_keyword_in_headline(headlines, "debate"))
print(find_keyword_in_headline(headlines, "to"))
print(find_keyword_in_headline(headlines, "uk"))


# regular expressions -> super powerful but can be super confusing!! 

headline_lengths = [find_word_count(headline) for headline in headlines]
print(headline_lengths)

short_headlines = [headline for headline in headlines if find_word_count(headline) <= 7]
print(short_headlines)

long_headlines = [headline for headline in headlines if find_word_count(headline) >= 7]
print(long_headlines)