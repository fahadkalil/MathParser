from sly import Lexer

class MyLexer(Lexer):    
    ignore = ' \t'
    ignore_comment = r'\#.*'

    tokens = {ID, NUMBER, EQ, FALSO, VDD, INC, QUIT}
    literals = { "=", "+", "-", "*", "/", "(", ")"}

    # identificador de comparação (==)
    EQ = r'=='
    INC = r'\+\+'

    # identificadores e palavras reservadas (keywords)
    ID = r'[a-zA-Z_][a-zA-Z0-9]*'
    ID['falso'] = FALSO
    ID['vdd'] = VDD
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t    

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Caractere ilegal {}".format(t.value[0]))
        self.index +=1

    
    
