

import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()
    
    if err_vars == None:
        err_vars = f.free_symbols
        
    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'
        
    return latex(sympy.sqrt(s), symbol_names=latex_names)

R, C, L = sympy.var('R C L')

f = R / (4 * sympy.pi * L) + 1 / (2 * sympy.pi) * sympy.sqrt(1 / (L * C) + R**2 / (4 * L**2))

print(error(f))

