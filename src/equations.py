from __future__ import annotations


class Equation:
    def __init__(self, equation: str):
        lex, rex = self.parse_equation(equation)
        self.lhs = lex
        self.rhs = rex

    @staticmethod
    def parse_equation(equation: str) -> (Expression, Expression):
        eq_stripped = ""
        for c in equation:
            if c != " ":
                eq_stripped += c
        eq_idx = -1
        for i in range(len(eq_stripped)):
            if eq_stripped[i] == "=":
                assert eq_idx == -1, "ERROR: Equation contains more than 1 equals sign."
                eq_idx = i

        assert eq_idx != -1, "ERROR: Equation does not contain an equals sign."
        assert eq_idx != 0, "ERROR: Equation does not contain a left hand side."
        assert eq_idx != len(eq_stripped)-1, "ERROR: Equation does not contain a right hand side."

        return Expression(eq_stripped[:eq_idx]), Expression(eq_stripped[eq_idx+1:])

    def __str__(self):
        return f"{str(self.lhs)} = {self.rhs}"


class Expression:
    def __init__(self, expression: str):
        self.terms: list[Term] = self.parse_expression(expression)

    @staticmethod
    def parse_expression(expression: str) -> list[Term]:
        terms = list()
        curr_term = ""
        curr_sign = -1 if expression[0] == "-" else 1

        for c in expression:
            if c in ["+", "-"]:
                terms.append(Term(curr_term, curr_sign))

                curr_term = ""
                curr_sign = 1 if c == "+" else -1
            else:
                curr_term += c

        terms.append(Term(curr_term, curr_sign))
        return terms

    def __str__(self):
        return " ".join([str(t) for t in self.terms])


class Term:
    def __init__(self, term: str, sign: int):
        self.term: str = term
        self.sign: int = sign

    def __str__(self):
        sign_str = "+" if self.sign == 1 else "-"
        return f"{sign_str}{self.term}"


class Variable:
    def __init__(self, name):
        self.name: str = name


if __name__ == "__main__":
    x = Equation("2*x+4=1")
    print(x)
