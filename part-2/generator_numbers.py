import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \\\
 доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    # for word in text.split():
    pattern = r"\d+\.\d+"
    for num in re.findall(pattern, text):
        yield num
        
        
def sum_profit(text: str, func: callable):
    all_nums = func(text)
    sum = 0.0
    for num in all_nums:
        sum = sum + float(num)
        
    return sum

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")