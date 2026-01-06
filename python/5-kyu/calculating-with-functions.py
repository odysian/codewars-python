def number_factory(n):
    def number_function(operation=None):
        if operation is None:
            return n
        else:
            return operation(n)

    return number_function


zero = number_factory(0)
one = number_factory(1)
two = number_factory(2)
three = number_factory(3)
four = number_factory(4)
five = number_factory(5)
six = number_factory(6)
seven = number_factory(7)
eight = number_factory(8)
nine = number_factory(9)


def plus(right_operand):
    return lambda left_operand: left_operand + right_operand


def minus(right_operand):
    return lambda left_operand: left_operand - right_operand


def times(right_operand):
    return lambda left_operand: left_operand * right_operand


def divided_by(right_operand):
    return lambda left_operand: left_operand // right_operand
