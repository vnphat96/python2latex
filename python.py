import random

def generate_random_data():
    groups = []
    for i in range(5):
        group_range = f"[{i*5+10}; {i*5+15})"
        representative_value = round(random.uniform(i*5+10, i*5+15), 1)
        frequency = random.randint(5, 20)
        groups.append((group_range, representative_value, frequency))
    return groups

def calculate_mean(groups):
    total_sum = sum(representative * freq for _, representative, freq in groups)
    total_freq = sum(freq for _, _, freq in groups)
    mean = total_sum / total_freq
    return mean

def calculate_variance(groups, mean):
    total_freq = sum(freq for _, _, freq in groups)
    variance = sum(freq * (representative - mean) ** 2 for _, representative, freq in groups) / total_freq
    return variance

def generate_problem_and_solution():
    groups = generate_random_data()
    mean = calculate_mean(groups)
    variance = calculate_variance(groups, mean)
    stddev = variance ** 0.5

    problem = r"""
        \[
        \begin{array}{|c|c|c|}
        \hline
        \text{Nhóm} & \text{Giá trị đại diện} & \text{Tần số} \\
        \hline
    """
    for group in groups:
        problem += f"{group[0]} & {group[1]} & {group[2]} \\\\ \\hline\n"

    problem += r"""
        \end{array}
        \]
        """
    bs = '\\'
    solution = f"""
        {bs}[
        {bs}bar{{x}} = {bs}frac{{{ ' + '.join([f'{repr_value} {bs}cdot {freq}' for _, repr_value, freq in groups]) }}}{{{' + '.join([str(freq) for _, _, freq in groups])}}} = {round(mean, 2)}
        {bs}]
        {bs}[
        s^2 = {bs}frac{{1}}{{{' + '.join([str(freq) for _, _, freq in groups])}}} {bs}left[ { ' + '.join([f'{freq}({repr_value} - {round(mean, 2)})^2' for _, repr_value, freq in groups]) } {bs}right] = {round(variance, 2)}
        {bs}]
        {bs}[
        s = {bs}sqrt{{{round(variance, 2)}}} = {round(stddev, 2)}
        {bs}]
        Đáp án: Gần với {round(stddev, 2)} nhất.
    """

    return problem, solution

def generate_latex():
    latex_content = r"""
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Bài toán và lời giải}

"""

    for i in range(1, 6):
        problem, solution = generate_problem_and_solution()
        latex_content += f"% Câu {i}\n"
        latex_content += f"{bs}textbf{{Câu {i}.}} Cho mẫu số liệu ghép nhóm thống kê mức lương của công ty (đơn vị: triệu đồng).\n"
        latex_content += problem
        latex_content += "Tính độ lệch chuẩn của mẫu số liệu ghép nhóm biểu diễn mức lương của công ty.\n"
        latex_content += "{bs}[\n{bs}text{A. } 5 {bs}quad {bs}text{B. } 6 {bs}quad {bs}text{C. } 7 {bs}quad {bs}text{D. } 8\n{bs}]\n\n"
        latex_content += "{bs}textbf{Lời giải:}\n"
        latex_content += solution
        latex_content += "\n"

    latex_content += r"""
\end{document}
    """

    with open("bai_toan_va_loi_giai_ngau_nhien.tex", "w", encoding="utf-8") as f:
        f.write(latex_content)

generate_latex()
