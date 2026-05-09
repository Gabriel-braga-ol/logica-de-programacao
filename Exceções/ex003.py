# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito__zero(d):
    if d == 0:
        raise ZeroDivisionError('não é possível dividir por zero')
    return True

def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)): # Verificando se n é float ou int
        raise TypeError(
            f'"{n}" deve ser um númnero inteiro'
            f' "{tipo_n.__name__}" enviado'
        )
    return True

def divide(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceito__zero(d)
    return n / d
    
   

print(divide(8, '0'))