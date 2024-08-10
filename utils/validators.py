from django.core.exceptions import ValidationError

def checks_if_the_calculated_digits_are_the_same_as_those_entered(cpf: str, first_digit: int, second_digit: int) -> int:
    if not (cpf[-2] == str(first_digit) and cpf[-1] == str(second_digit)): raise ValidationError('CPF invalido')

def calculates_checked_digits(cpf: str, multiplier: int) -> int:
    sum_ = sum(
        int(cpf[i]) * multiplier[i] for i in range(len(multiplier))
    )   
    rest = sum_ % 11

    return 0 if rest < 2 else 11 - rest

def checks_all_digits_are_the_same(cpf: str) -> ValidationError:
    if cpf == cpf[0] * 11 : raise ValidationError("CPF inválido")

def checks_if_it_has_eleven_digits(cpf: str) -> ValidationError:
    if len(cpf) != 11: raise ValidationError("CPF inválido")

def removing_stitches(word_to_remove_dots: str) -> str:
    return ''.join([char for char in word_to_remove_dots if char.isdigit()])

def validate_cpf(cpf_to_validate: str) -> bool:
    
    cpf = removing_stitches(cpf_to_validate)

    checks_if_it_has_eleven_digits(cpf)
    checks_all_digits_are_the_same(cpf)

    multiplicator_first = list(range(10, 1, -1))
    first_digit = calculates_checked_digits(cpf, multiplicator_first)

    multiplicator_second = list(range(11, 1, -1))
    second_digit = calculates_checked_digits(cpf, multiplicator_second)

    checks_if_the_calculated_digits_are_the_same_as_those_entered(cpf, first_digit, second_digit)

    return True

