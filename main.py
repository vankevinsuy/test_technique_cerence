from typing import List
from myDecorators import clean_list, verify_dimension
from itertools import permutations


@verify_dimension
@clean_list
def get_words(dimension: int, word_list: List[str]) -> List[str]:
    # get all words of X dimension character
    words_dimension_N = [word for word in word_list if len(word) == dimension]

    # remove words that are strictly bigger than the defined dimension
    word_list = [word for word in word_list if len(word) <= dimension]

    # get all possible permutation with the rest of the input list
    permutation = [''.join(perm) for perm in permutations(word_list, 2)]

    return [word for word in words_dimension_N if word in permutation]
