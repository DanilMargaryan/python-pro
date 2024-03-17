import latex

data = [
    ["Column 1", "Column 2", "Column 3"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

latex_code = latex.generate_start()
latex_code += latex.generate_latex_table(data)
latex_code += latex.generate_latex_img('artifacts/frog.jpg', 0.5, "it's frog")
latex_code += latex.generate_end()

# Сохранение LaTeX кода в файл
with open("main.tex", "w") as file:
    file.write(latex_code)
