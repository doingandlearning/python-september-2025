from exceptions import GuessOutOfRangeError

def get_user_guess(min, max):
    """
    This gets a user guess, verifies it is a number and is between the min and max

    Arguments:
      - min (minimum value)
      - max (maximum value)
    """
    print("Let's get your next guess!")
    
    # This verifies that it's a number

    try:
        guess = int(input(f"Enter your guess ({min}-{max}): "))
    except ValueError:
        print("Whoops! That's not a number.")
        return get_user_guess(min, max)
    
    # This verifies that the number is in range
    try:
        if is_number_in_range(guess, min, max):
            return guess
        raise GuessOutOfRangeError()
    except GuessOutOfRangeError:
        print("That number is out of range. Try again.")
        return get_user_guess(min, max)


def is_number_in_range(target, min, max):
    return min <= target <= max


class FetchingDataError(Exception):
  """"""

import time

def get_data_from_website(url, retry=0):
  try:
    print("Get some data!")
  except:
    if retry == 3:
      raise FetchingDataError()
    # exponential backoff
    time.sleep(0.5 * retry)
    get_data_from_website(url, retry + 1)