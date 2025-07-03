def calculate(C: int, P: int, G: int, A: int) -> None:
    calc_string = f"900000 * ({P} + 0.65 * {G}) / {A} + 100000 * {C} / {A}"
    res = eval(calc_string)
    res = round(res + 1e-7)  # 四舍五入
    print(f"{calc_string} = {res}(四舍五入后)")

if __name__ == "__main__":
    amount = int(input("输入物量: "))
    max_combo = int(input("输入最大连击数: "))
    perfect = int(input("输入 Pefect 数: "))
    good = int(input("输入 Good 数: "))
    calculate(max_combo, perfect, good, amount)