from datetime import datetime

# -------------------------------
# DIFFERENTIAL EQUATION ANALYZER
# -------------------------------

def save_history(content):
    with open("history.txt", "a") as file:
        file.write(content + "\n")


def classify_differential_equation(equation):
    equation = equation.replace(" ", "")

    if "dy/dx" in equation:
        if "y^2" in equation or "y*y" in equation:
            return "Bernoulli Differential Equation"
        elif "y" in equation:
            return "Linear Differential Equation"
        else:
            return "Homogeneous Differential Equation"

    elif "dx" in equation and "dy" in equation:
        return "Exact Differential Equation"

    return "General Differential Equation"


def detect_order(equation):
    if "d2y/dx2" in equation:
        return 2
    elif "dy/dx" in equation:
        return 1
    return "Unknown"


def detect_degree(equation):
    if "(dy/dx)^2" in equation:
        return 2
    elif "dy/dx" in equation:
        return 1
    return "Unknown"


def integrating_factor(Px):
    return f"e^(∫({Px})dx)"


def jacobian_matrix(functions, variables):
    print("\nJACOBIAN MATRIX")
    print("-" * 40)

    for f in functions:
        row = []

        for v in variables:
            row.append(f"∂({f})/∂{v}")

        print(row)


def hessian_matrix(function, variables):
    print("\nHESSIAN MATRIX")
    print("-" * 40)

    for v1 in variables:
        row = []

        for v2 in variables:
            row.append(f"∂²({function})/∂{v1}∂{v2}")

        print(row)


def analyze_equation():
    equation = input("\nEnter Differential Equation: ")

    eq_type = classify_differential_equation(equation)
    order = detect_order(equation)
    degree = detect_degree(equation)

    print("\nANALYSIS RESULT")
    print("-" * 40)
    print("Equation :", equation)
    print("Type     :", eq_type)
    print("Order    :", order)
    print("Degree   :", degree)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_history(
        f"[{timestamp}] Equation: {equation} | "
        f"Type: {eq_type} | Order: {order} | Degree: {degree}"
    )

    print("\nAnalysis saved to history.txt")


def show_history():
    print("\nANALYSIS HISTORY")
    print("-" * 40)

    try:
        with open("history.txt", "r") as file:
            data = file.read()

            if data.strip():
                print(data)
            else:
                print("No history available.")

    except FileNotFoundError:
        print("No history found.")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():

    while True:

        print("\n")
        print("=" * 50)
        print(" ADVANCED DIFFERENTIAL EQUATION ANALYZER ")
        print("=" * 50)

        print("1. Analyze Differential Equation")
        print("2. Compute Integrating Factor")
        print("3. Generate Jacobian Matrix")
        print("4. Generate Hessian Matrix")
        print("5. View Analysis History")
        print("6. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            analyze_equation()

        elif choice == "2":
            P = input("Enter P(x): ")
            print("\nIntegrating Factor:")
            print(integrating_factor(P))

        elif choice == "3":

            n = int(input("Enter Number of Functions: "))

            functions = []

            for i in range(n):
                functions.append(
                    input(f"Enter Function {i+1}: ")
                )

            variables = input(
                "Enter Variables (space separated): "
            ).split()

            jacobian_matrix(functions, variables)

        elif choice == "4":

            function = input("Enter Function: ")

            variables = input(
                "Enter Variables (space separated): "
            ).split()

            hessian_matrix(function, variables)

        elif choice == "5":
            show_history()

        elif choice == "6":
            print("\nProgram Terminated Successfully.")
            break

        else:
            print("\nInvalid Choice. Try Again.")


main()