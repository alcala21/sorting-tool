import argparse


class SortingTool:
    def __init__(self, data_type="word", sorting_type="natural", input_file=None, output_file=None):
        self.data = []
        self.dtype = data_type
        self.stype = sorting_type
        self.count = 0
        self.value_counts = {}
        self.values = []
        self.process = {
            "word": self.word,
            "line": self.line,
            "long": self.long,
        }
        self.keywords = {"long": "numbers", "line": "lines", "word": "words"}
        self.ifile = input_file
        self.ofile = output_file

    def start(self):
        self.get_input()
        if self.data:
            self.process[self.dtype]()
            self.sort_values()
            self.print()

    def get_input(self):
        if self.ifile:
            with open(self.ifile, 'r') as f:
                self.data = f.read().split('\n')
        else:
            while True:
                try:
                    self.data.append(input().strip())
                except EOFError:
                    break

    def long(self):
        for row in self.data:
            nums = []
            for num in row.split():
                try:
                    nums.append(int(num))
                except:
                    print(f'"{num}" is not a long. It will be skipped.')
            self.process_array(nums)

    def word(self):
        for row in self.data:
            words = row.split()
            self.process_array(words)

    def line(self):
        self.process_array(self.data)

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
        output = f"Total {self.keywords[self.dtype]}: {self.count}.\n"
        if self.stype == "natural":
            char = "\n" if self.dtype == "line" else " "
            output += f"Sorted data:{char}{char.join(map(str, self.values))}"
        else:
            for value, count in self.value_counts.items():
                output += (
                    f"{value}: {count} time(s), {int(count/self.count * 100)}%\n"
                )
        if self.ofile:
            with open(self.ofile, 'w') as f:
                f.write(output)
        else:
            print(output)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument(
            "-dataType", choices=["word", "long", "line"], default="word"
        )
        parser.add_argument(
            "-sortingType", choices=["natural", "byCount"], default="natural"
        )
        parser.add_argument("-inputFile", default=None)
        parser.add_argument("-outputFile", default=None)
        args, unknown = parser.parse_known_args()
        if unknown:
            for p in unknown:
                print(f'"{p}" is not a valid parameter. It will be skipped.')
        sorting_type = args.sortingType
        data_type = args.dataType
        input_file = args.inputFile
        output_file = args.outputFile
        st = SortingTool(data_type, sorting_type, input_file, output_file)
        st.start()
    except argparse.ArgumentError as e:
        print(f"No {e.argument_name[1:-4]} type defined!")
