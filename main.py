class SortingTool:
    def __init__(self):
        self.max_val = -float('inf')
        self.max_count = 0
        self.int_count = 0

    def start(self):
        while True:
            try:
                data = input()
                nums = list(map(int, filter(lambda x: x.lstrip('-+').isnumeric(), data.split())))
                self.int_count += len(nums)
                max_nums = max(nums)
                max_count = nums.count(max_nums)
                if max_nums > self.max_val:
                    self.max_val = max_nums
                    self.max_count = max_count
                elif max_nums == self.max_val:
                    self.max_count += max_count

            except EOFError:
                break

        self.print()

    def print(self):
        print(f"Total numbers: {self.int_count}")
        print(f"The greatest number: {self.max_val} ({self.max_count} time(s))")


SortingTool().start()