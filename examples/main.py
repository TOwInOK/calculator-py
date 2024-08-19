from lib import Calculator

if __name__ == "__main__":
    result = Calculator(10).plus(5).minus(3).multiply(2).divide(1).result()
    print("calc result: ", result)

    expression = "(10+10*2)*2"
    calc = Calculator(10)
    result = calc.minus(10).calculate(expression).minus(1).result()
    print("Result:", result)
