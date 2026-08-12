import magic_calc.basic_ops as myops
import magic_calc.advanced_ops


result = myops.add(10, 5)
print(result)

result = myops.multiply(22, 4)
print(result)

result1 = magic_calc.advanced_ops.sqrt(10)
print(f"10+5={result} 10의 제곱근은 {round(result1,4)}입니다.")

result3 = magic_calc.advanced_ops.magic_multiply(5)
print(result3)

