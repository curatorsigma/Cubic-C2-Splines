#!/bin/python3

# Cubic C2-Splines through x=-2,-1,0,1,2
# with s'(2) = x'(-2) = 0
# All Results in Fractions until being displayed.
# By Jonathan Schleucher (twitter @Imathnathan)

import fractions


def spline_calc(inx):
    for i in range(0, 5):
        if CurrX >= x[i] and CurrX < x[i + 1]:
            return fractions.Fraction(poly_calc(i, CurrX))


def poly_calc(i, inx):
    """Berechnet den Wert des i-ten Polynoms in x."""
    return (alpha[i] + beta[i] * (inx - x[i]) + gamma[i] * (inx - x[i])**2 +
            delta[i] * (inx - x[i])**3)


def derivative_calc(i, inx):
    """Berechnet die Ableitung des i-ten Polynoms in x."""
    return (beta[i] + 2 * gamma[i] * (inx - x[i]) +
            3 * delta[i] * (inx - x[i])**2)


def snd_derivative_calc(i, inx):
    """Berechnet die zweite Ableitung des i-ten Polynoms in x."""
    return 2 * gamma[i] + 6 * delta[i] * (inx - x[i])


if __name__ == "__main__":
    x = [-2, -1, 0, 1, 2]
    y = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        y[i] = int(input(f"Geben sie y_{i} ein!"))

    # Berechne delta_0
    delta_0 = fractions.Fraction((3 * y[4] - 12 * y[3] +
                                  42 * y[2] - 100 * y[1]), 56)

    # Berechne Koeffizienten
    alpha = [0, 0, 0, 0]
    beta = [0, 0, 0, 0]
    gamma = [0, 0, 0, 0]
    delta = [0, 0, 0, 0]

    for i in range(0, 4):
        alpha[i] = fractions.Fraction(y[i])

    beta[0] = fractions.Fraction(0)
    beta[1] = 2 * y[1] + delta_0
    beta[2] = 3 * y[2] - 8 * y[1] - 4 * delta_0
    beta[3] = 3 * y[3] - 12 * y[2] + 27 * y[1] + 15 * delta_0

    gamma[0] = y[1] - delta_0
    gamma[1] = y[1] + 2 * delta_0
    gamma[2] = 3 * y[2] - 11 * y[1] - 7 * delta_0
    gamma[3] = 3 * y[3] - 18 * y[2] + 46 * y[1] + 26 * delta_0

    delta[0] = delta_0
    delta[1] = y[2] - 4 * y[1] - 3 * delta_0
    delta[2] = y[3] - 7 * y[2] + 19 * y[1] + 11 * delta_0
    delta[3] = y[4] - 7 * y[3] + 30 * y[2] - 73 * y[1] - 41 * delta_0

    # Output
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Alpha: {[float(var) for var in alpha]}")
    print(f"Beta: {[float(var) for var in beta]}")
    print(f"Gamma: {[float(var) for var in gamma]}")
    print(f"Delta: {[float(var) for var in delta]}")

    for i in range(0, 4):
        # More Output
        print(f"\nPolynom s_{i}:")
        print(f"s_{i} = {alpha[i]} + {beta[i]}(x - {x[i]}) + {gamma[i]}(x - {x[i]})^2 + {delta[i]}(x - {x[i]})^3")
        print(f"s_{i}(x_{i}) = {poly_calc(i, x[i])}")
        print(f"s_{i}(x_{i+1}) = {poly_calc(i, x[i+1])}")
        print(f"s'_{i}(x_{i}) = {derivative_calc(i, x[i])}")
        print(f"s'_{i}(x_{i+1}) = {derivative_calc(i, x[i+1])}")
        print(f"s''_{i}(x_{i}) = {snd_derivative_calc(i, x[i])}")
        print(f"s''_{i}(x_{i+1}) = {snd_derivative_calc(i, x[i+1])}")

        #Test Cases To be sure.
        if i < 3:
            assert(poly_calc(i, x[i]) == y[i])
            assert(poly_calc(i, x[i + 1]) == y[i + 1])
            assert(derivative_calc(i, x[i + 1]) ==
                   derivative_calc(i + 1, x[i + 1]))
            assert(snd_derivative_calc(i, x[i + 1]) ==
                   snd_derivative_calc(i + 1, x[i + 1]))
        elif i == 3:
            assert(poly_calc(i, x[i]) == y[i])
            assert(poly_calc(i, x[i + 1]) == y[i + 1])
            assert(derivative_calc(i, x[i + 1]) == 0)

        print("Alle Tests wurden bestanden. Die Angegebenen Polynome sind " +
              "die passenden Polynom-Splines.")

    # Information about specific Point.
    while True:
        instr = input("Geben sie eine Stelle an," +
                      "oder beenden sie mit 'q'.\n")
        if instr in ["q", "Q"]:
            quit()
        else:
            CurrX = fractions.Fraction(instr)
        # Chooses right Part of Spline.
        for i in range(0, 5):
            if CurrX >= x[i] and CurrX < x[i + 1]:
                print(f"s({CurrX}) = {fractions.Fraction(poly_calc(i, CurrX))}")
                print(f"s'({CurrX}) = {fractions.Fraction(derivative_calc(i, CurrX))}")
                print(f"s''({CurrX}) = {fractions.Fraction(snd_derivative_calc(i, CurrX))}")
                break
