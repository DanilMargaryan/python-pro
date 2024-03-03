import sys


def tail(file, lines=10, header=None):
    if header:
        print(header)
    try:
        with open(file, 'r') if file != sys.stdin else file as f:
            all_lines = f.readlines()
            for line in all_lines[-lines:]:
                print(line, end='')
    except Exception as e:
        print(f"Error reading file {file}: {e}")


if __name__ == "__main__":
    files = sys.argv[1:]
    lines_count = 10
    lines_count_stdin = 17

    if files:
        for i, file_name in enumerate(files):
            header = f"==> {file_name} <==\n" if len(files) > 1 else None
            tail(file_name, lines=lines_count, header=header)
            if i < len(files) - 1:
                print()  # Добавляем пустую строку между выводами файлов
    else:
        tail(sys.stdin, lines=lines_count_stdin)
