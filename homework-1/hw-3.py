import sys


def count_stats(filename=None):
    lines = 0
    words = 0
    chars = 0
    if filename:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line.encode('utf-8'))
    else:
        for line in sys.stdin:
            lines += 1
            words += len(line.split())
            chars += len(line.encode('utf-8'))
    return lines, words, chars


def wc(files):
    total_lines = 0
    total_words = 0
    total_chars = 0
    for file in files:
        try:
            lines, words, chars = count_stats(file)
            print(f"{lines} {words} {chars} {file}")
            total_lines += lines
            total_words += words
            total_chars += chars
        except Exception as e:
            print(f"Ошибка при обработке файла {file}: {e}", file=sys.stderr)
    if len(files) > 1:
        print(f"{total_lines} {total_words} {total_chars} total")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        lines, words, chars = count_stats()
        print(f"{lines} {words} {chars}")
