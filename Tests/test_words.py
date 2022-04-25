from unittest import TestCase
from main import get_words
from random import choice
from string import ascii_lowercase


class Tester(TestCase):
    def test_get_words(self):
        ### INPUTS ####
        N = 6
        L = [
            "hot", "bird", "dog", "tailor", "hotdog", "or", "if", "tail",
            "".join(choice(ascii_lowercase)
                    for i in range(20)),  # add a big word
            " ",  # add an empty space
            12,  # add number
            "{}"  # add dict as string
        ]

        ### TEST FUNCTION ####
        my_result = get_words(N, L)

        ### ASSERT ###
        expected = ["tailor", "hotdog"]

        self.assertEqual(expected, my_result)
