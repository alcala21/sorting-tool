import sys


class SortingTool:
    def __init__(self, data_type="word"):
        self.data = []
        self.type = data_type
        self.max_val = -float("inf") if self.type == "long" else ""
        self.max_count = 0
        self.count = 0
        self.sorting = {"word": self.word, "line": self.line, "long": self.long}
        self.keywords = {
            "long": {
                "plural": "numbers",
                "adjective": "greatest",
                "singular": "number",
            },
            "line": {"plural": "lines", "adjective": "longest", "singular": "line"},
            "word": {"plural": "words", "adjective": "longest", "singular": "word"},
        }

    def start(self):
        self.get_input()
        self.sorting[self.type]()
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

    def max(self, arr):
        if isinstance(arr[0], int):
            return max(arr)
        max_len = max(map(len, arr))
        same_length = list(filter(lambda x: len(x) == max_len, arr))
        return max(same_length)

    def new_max_value(self, value):
        if self.type == "long":
            return value > self.max_val
        return len(value) > len(self.max_val) or (
            len(value) == len(self.max_val) and value > self.max_val
        )

    def process_array(self, arr):
        self.count += len(arr)
        max_val = self.max(arr)
        max_count = arr.count(max_val)
        if self.new_max_value(max_val):
            self.max_val = max_val
            self.max_count = max_count
        elif max_val == self.max_val:
            self.max_count = max_count

    def print(self):
        first_line = f"Total {self.keywords[self.type]['plural']}: {self.count}."
        second_line = f"The {self.keywords[self.type]['adjective']} {self.keywords[self.type]['singular']}:"
        second_line += '\n' if self.type == 'line' else ' '
        second_line += f"{self.max_val}"
        second_line += '\n' if self.type == 'line' else ' '
        second_line += (
            f"({self.max_count} time(s), {int(self.max_count/self.count * 100)}%)."
        )
        print(first_line)
        print(second_line)


data_type = "word"
if __name__ == "__main__":
    if len(sys.argv) > 2:
        data_type = sys.argv[2]
st = SortingTool(data_type)
st.start()
