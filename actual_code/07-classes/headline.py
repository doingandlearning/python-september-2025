class Headline:
  def __init__(self, text, source):
    self.text = text 
    self.source = source

  def __str__(self):
    return f"Headline from {self.source}: '{self.text}'"

  def __repr__(self):
    return f"Headline(source='{self.source}', text='{self.text}')"

  def get_word_count(self):
    return len(self.text.split())

  def get_character_count(self):
    return len(self.text)

  def contains_keyword(self, keyword):
    return keyword.lower() in self.text.lower()


headline1 = Headline("Jimmy Kimmel reinstated", "BBC")
headline2 = Headline("Mad inflation", "Guardian")

print(headline1)
print(headline2)

headlines = [headline1, headline2]

for headline in headlines:
  print(f"Headline from {headline.source} is {headline.get_word_count()} words long.")

headlines = [
    Headline("General election: Labour and Tories clash over tax", "BBC"),
    Headline("England crowned T20 world champions", "BBC"),
    Headline("Summer travel chaos feared as airline strikes loom", "BBC"),
    Headline("UK inflation rate falls to lowest level in three years", "BBC"),
    Headline("New David Hockney exhibition opens in London", "BBC"),
    Headline("Science discovers new way to tackle plastic waste", "BBC"),
    Headline("Government announces new funding for NHS", "BBC"),
    Headline("Stock market hits record high on tech boom", "BBC"),
    Headline("Debate rages over future of Artificial Intelligence", "BBC"),
    Headline("Classic Doctor Who episodes to be released in colour", "BBC")
]

word_counts = [headline.get_word_count() for headline in headlines]
print(word_counts)

character_counts = [headline.get_character_count() for headline in headlines]
print(f"The average character length of headline is {sum(character_counts)/len(character_counts)}.")

debate_headlines = [headline for headline in headlines if headline.contains_keyword("debate")]
print(debate_headlines)