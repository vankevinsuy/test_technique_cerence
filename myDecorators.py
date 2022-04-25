def verify_dimension(func):
    def check(*args, **kwargs):
        # verify if the first argument is
        # an integer
        # higher than 2 because the minimal word has at least 2 letters
        correct = (type(args[0]) == int) and args[0] > 2

        if not correct:
            raise Exception(
                "first argument must be an integer and higher than 0")

        return func(*args, **kwargs)

    return check


def clean_list(func):
    def clean(*args, **kwargs):
        # verify if the list is not empty
        if len(args[1]) == 0:
            raise Exception("list is empty")

        # clean the input list from :
        # elements that are not a string
        # empty space
        # not letters

        clean_list = []

        for element in args[1]:
            if (type(element) == str) and \
                    (' ' not in element) and \
                    element.isalpha():
                clean_list.append(element)

        args = list(args)
        args[1] = clean_list

        return func(*args, **kwargs)

    return clean
