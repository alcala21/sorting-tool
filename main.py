import sys
import argparse


class SortingTool:
    def __init__(self, data_type="word", sorting_type="natural"):
        self.data = []
        self.dtype = data_type
        self.stype = sorting_type
        self.max_val = -float("inf") if self.dtype == "long" else ""
        self.max_count = 0
        self.count = 0
        self.value_counts = {}
        self.values = []
        self.process = {
            "word": self.word,
            "line": self.line,
            "long": self.long,
        }
        self.keywords = {
            "long": {
                "plural": "numbers",
                "adjective": "greatest",
                "singular": "number",
            },
            "line": {"plural": "lines", "adjective": "longest", "singular": "line"},
            "word": {"plural": "words", "adjective": "longest", "singular": "word"},
        }
        self.integers = []

    def start(self):
        # self.get_input()
        self.data = ["1 -2   33 4", "42", "1                 1"]
        if self.data:
            self.process[self.dtype]()
            self.sort_values()
            self.print()

    def get_input(self):
        while True:
            try:
                self.data.append(input())
            except EOFError:
                break

    def long(self):
        for row in self.data:
            nums = list(
                map(int, filter(lambda x: x.lstrip("-+").isnumeric(), row.split()))
            )
            self.process_array(nums)

    def word(self):
        for row in self.data:
            words = row.split()
            self.process_array(words)

    def line(self):
        self.process_array(self.data)

    @staticmethod
    def max(arr):
        if isinstance(arr[0], int):
            return max(arr)
        max_len = max(map(len, arr))
        same_length = list(filter(lambda x: len(x) == max_len, arr))
        return max(same_length)

    def new_max_value(self, value):
        if self.dtype == "long":
            return value > self.max_val
        return len(value) > len(self.max_val) or (
            len(value) == len(self.max_val) and value > self.max_val
        )

    def process_array(self, arr):
        self.values += arr
        for val in arr:
            if self.value_counts.get(val, 0) == 0:
                self.value_counts[val] = 1
            else:
                self.value_counts[val] += 1

    def sort_values(self):
        self.values.sort()
        sorted_counts = dict()
        sorted_nums = []
        for key, val in self.value_counts.items():
            if not sorted_counts.get(val, None):
                sorted_counts[val] = {key}
            else:
                sorted_counts[val].add(key)
        unique_counts = sorted(sorted_counts)
        for count in unique_counts:
            for num in sorted(sorted_counts[count]):
                sorted_nums.append(num)
        self.value_counts = {x: self.value_counts[x] for x in sorted_nums}

    def print(self):
        self.count = len(self.values)
        first_line = f"Total {self.keywords[self.dtype]['plural']}: {self.count}."
        second_line = ""
        if self.stype == "natural":
            char = '\n' if self.dtype == 'line' else ' '
            second_line += f"Sorted data:{char}{char.join(map(str, self.values))}"
        else:
            for value, count in self.value_counts.items():
                second_line += f"{value}: {count} time(s), {int(count/self.count * 100)}%\n"
            # second_line = f"The {self.keywords[self.dtype]['adjective']} {self.keywords[self.dtype]['singular']}:"
            # second_line += "\n" if self.dtype == "line" else " "
            # second_line += f"{self.max_val}"
            # second_line += "\n" if self.dtype == "line" else " "
            # second_line += (
            #     f"({self.max_count} time(s), {int(self.max_count/self.count * 100)}%)."
            # )
        print(first_line)
        print(second_line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dataType", choices=["word", "long", "line"], default="word")
    parser.add_argument(
        "-sortingType", choices=["natural", "byCount"], default="natural"
    )
    args = parser.parse_args()
    sorting_type = args.sortingType
    data_type = args.dataType
data_type = "line"
sorting_type = "natural"
st = SortingTool(data_type, sorting_type)
st.start()
