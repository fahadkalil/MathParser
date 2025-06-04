from sly import Parser
from .lexer import MyLexer

class MyParser(Parser):
    debugfile = 'parser.out'
    tokens = MyLexer.tokens

    # ordem: da menor para a maior precendencia
    precedence = (
        ('left', 'EQ'),
        ('left', '+', '-'),        
        ('left', '*', '/'),        
        ('right', 'UMINUS'), 
        )

    def __init__(self):
        self.names = { }

    # funcoes 'statement' não possuem retorno
    # funcoes 'expr' possuem retorno

    @_('ID "=" expr')
    def statement(self, p):
        self.names[p.ID] = p.expr
           
    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr') # Soma
    def expr(self, p):
        return p[0] + p[2]

    @_('expr "-" expr') # Subtração
    def expr(self, p):
        return p[0] - p[2]

    @_('expr "*" expr') # Multiplicação
    def expr(self, p):
        return p[0] * p[2]

    @_('expr "/" expr') # Divisão
    def expr(self, p):
        return p[0] / p[2]

    @_('expr EQ expr') # Comparação
    def expr(self, p):
        return p[0] == p[2]

    @_('"-" expr %prec UMINUS') # caso especial, ex.: 5 * -5
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
        
    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print('ID <{}> indefinido'.format(p.ID))
            return 0

    @_('ID INC')
    def expr(self, p):
        try:
            self.names[p.ID]+=1
            return self.names[p.ID]
        except LookupError:
            print('ID <{}> indefinido'.format(p.ID))
            return 0
        
        

    
