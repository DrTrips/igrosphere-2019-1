import re


def read_file(file_path):
    with open(file_path, 'r')as f:
        return f.read()


def filter_lines(regexp, lines):
    result = []
    for line in lines:
        if re.match(regexp, line):
            result.append(line)
        else:
            print(f"line {line} don't match")
    return [line for line in lines if re.match(regexp, line)]


<<<<<<< HEAD
if __name__ == "__main__":
    filename = "coverage-error.log"
    regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:\d\d\].+"
    lines = read_file(filename)
    print("Author is a.kulikov")
    print(filter_lines(regexp, lines))
=======
filename = "coverage-error.log"
regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:d\d\].+"
lines = read_file(filename)
print(filter_lines(regexp, lines))
>>>>>>> parent of bb11080... fix regexp
