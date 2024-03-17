def generate_latex_table(data: list) -> str:
    """
    Принимает двойной список `data` и возвращает строку с LaTeX кодом таблицы.
    """
    header = data[0]
    rows = data[1:]

    latex_code = "\n\\begin{center}\n\\begin{tabular}{|| " + "c " * len(header) + "||}\n\\hline\n"
    latex_code += " & ".join(header) + "\\\\\n\\hline\hline\n"
    # Данные таблицы
    for row in rows:
        latex_code += " & ".join(map(str, row)) + " \\\\\n\\hline\n"

    latex_code += "\\end{tabular}\n\\end{center}\n"
    return latex_code


def generate_latex_img(filepath: str, width: float, caption: str) -> str:
    """
    Возвращает строку с LaTeX кодом для вставки изображения.

    Аргументы:
    filepath (str): Путь к файлу изображения.
    width (int): Масштаб изображения.
    caption (str): Подпись к изображению.
    """
    latex_code = '\n\\begin{figure}\n\\centering'
    latex_code += '\n\\includegraphics' + '[width=' + str(
        width) + '\linewidth]{' + filepath + '}\n\\caption{' + caption + '}' + '\n\\end{figure}'
    return latex_code


def generate_start():
    latex_code = '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}'
    return latex_code


def generate_end():
    latex_code = '\\end{document}'
    return latex_code
