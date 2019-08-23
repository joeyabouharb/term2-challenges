"""
application that checks if number is divisible by 7
"""
from types import GeneratorType as Generator


def number_generator(start: int, end: int) -> Generator:
    """
    creates a generator to iterate number from start to end
    """
    for num in range(start, end):
        yield num


def check_number_is_divisible_by(number: int, divisible=7) -> bool:
    """
    checks if number is divisible by specified value
    """
    if number % divisible == 0:
        return True
    return False


def check_number_is_not_multiple_of(number: int, multiple=5) -> bool:
    """
    check if number is not multiple of specified value
    """
    if number % multiple == 0:
        return False
    return True

def run_tests(numbers: Generator) -> list:
    """
    runs the tests to check if both values are divisible and multiple of specified values
    """
    correct_values = list()
    for number in numbers:
        is_divisible = check_number_is_divisible_by(number)
        is_multiple = check_number_is_not_multiple_of(number)
        if is_divisible and is_multiple:
            correct_values.append(number)
    return correct_values


def str_seq(seq: list) -> str:
    """
    return list as string
    """
    return " ".join(str(num) for num in seq)


def main(start: int, end: int) -> None:
    """
    main entrypoint
    """
    number_to_test = number_generator(start, end)
    print(str_seq(run_tests(number_to_test)))

if __name__ == '__main__':
    main(2, 1000)
    