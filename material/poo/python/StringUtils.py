class StringUtils:

    new_line = "\n"
    tab = "\t"

    @staticmethod
    def get_first(input):
        return input[0]

    @staticmethod
    def get_last(input):
        return input[-1]

    @staticmethod
    def get_substring(input, first, last):
        return input[first:last]


print(StringUtils.get_substring("python", 2, 4))
print(f"1{StringUtils.tab}2")
