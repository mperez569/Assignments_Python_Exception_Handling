def F_to_C(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = F_to_C(fahrenheit)
    except ValueError:
        print("Error: Please enter a valid number for the temperature.")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

main()
