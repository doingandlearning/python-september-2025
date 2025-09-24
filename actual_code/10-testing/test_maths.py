from maths import add
import pytest

def setup_function():
  print("This is setting something up")

def teardown_function():
  print("This is tearing something down.")

def setup_module():
  print("Runs at the start of the test file.")

def teardown_module():
  print("Clean up after the file.")

def test_two_whole_numbers_add_correctly():
    # Arrange - Given
    number1 = 10
    number2 = 20
    expected = 30

    # Act  - When
    result = add(number1, number2)

    # Assert  - Then
    assert result == expected

def test_two_decimals_numbers_add_correctly():
    # Arrange - Given
    number1 = 10.3
    number2 = 20.6
    expected = 30.9

    # Act  - When
    result = add(number1, number2)

    # Assert  - Then
    assert result == pytest.approx(expected)

# paramaterize my test
@pytest.mark.parametrize('number1, number2, expected', [
  (-100, -100, -200),
  (1_000_000, 2_000_000, 3_000_000),
  (100, -10, 90),
  (0.9, 10, 10.9),
  (3_000_000, 10, 3_000_010)
]
)
def test_all_the_test_cases_pass(number1, number2, expected):
    # Act  - When
    result = add(number1, number2)

    # Assert  - Then
    assert result == pytest.approx(expected)


@pytest.mark.parametrize('value1, value2', [
  ([], []),
  ({}, {}),
  ("one", "two"),
  ("one", {}),
  ([], "twon")
])
def test_it_fails_when_adding_non_numbers(value1, value2):
  with pytest.raises(TypeError):
    result = add(value1, value2)