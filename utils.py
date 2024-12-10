from typing import Any, TypeVar

T = TypeVar("T")

DEBUG = False


def answer1(value: T) -> T:
    print(f"Part 1 Answer: {value}")
    return value


def answer2(value: T) -> T:
    print(f"Part 2 Answer: {value}")
    return value


def get_input(filename: str, operation: str = "strip") -> list[str]:
    with open(filename) as fp:
        return [getattr(line, operation)() for line in fp]


def get_input_as_int(filename):
    with open(filename) as fp:
        return [int(line.strip()) for line in fp]


def get_input_as_str(filename: str) -> str:
    with open(filename) as fp:
        return fp.read().strip()


def get_input_as_grid(filename: str) -> dict[tuple[int, int], str]:
    output_dict: dict[tuple[int, int], str] = {}
    with open(filename) as fp:
        for y_index, row in enumerate(line.strip() for line in fp):
            for x_index, col in enumerate(row):
                output_dict[(x_index, y_index)] = col

    return output_dict


def print_grid(grid: dict[tuple[int, int], str]) -> None:
    temp = ""
    for (x, y), char in grid.items():
        if x == 0:
            print(temp)
            temp = ""

        temp += char

    print(temp)


def get_line_separated_inputs(filename: str) -> list[list[str]]:
    chunks: list[list[str]] = []
    chunk: list[str] = []
    with open(filename) as fp:
        for line in fp:
            if line.strip() == "":
                chunks.append(chunk)
                chunk = []
            else:
                chunk.append(line.strip())

    if chunk:
        chunks.append(chunk)

    return chunks


def debug(string):
    if DEBUG:
        print(string)
