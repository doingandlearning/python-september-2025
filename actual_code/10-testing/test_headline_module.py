from headline_module import Headline
import pytest

def test_that_object_creation_works_properly():
  headline = Headline("Python course is amazing", "Kevin")

  assert headline.text == "Python course is amazing"
  assert headline.source == "Kevin"
  assert isinstance(headline, Headline)

def test_get_word_count_method():
  headline = Headline("Ukraine: Hopefully more meaningful peace talks", "BBC")
  assert headline.get_word_count() == 6


@pytest.fixture
def sample_headline():
  return Headline("This is a sample headline for testing", "BBC News")

@pytest.fixture
def example_headlines():
  return [
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


def test_is_long_headline(sample_headline):
  assert sample_headline.is_long_headline() == False

def test_get_character_counts(example_headlines):
  for headline in example_headlines:
    assert headline.get_character_count() == len(headline.text)

def test_search_keyword(sample_headline):
  assert sample_headline.contains_keyword("testing")
  assert not sample_headline.contains_keyword("thisisnotthere")