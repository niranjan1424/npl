class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        return self.parse_term() + self.parse_expression_tail()

    def parse_expression_tail(self):
        if self.match('+'):
            self.consume('+')
            return '+' + self.parse_term() + self.parse_expression_tail()
        else:
            return ''

    def parse_term(self):
        return self.parse_factor() + self.parse_term_tail()

    def parse_term_tail(self):
        if self.match('*'):
            self.consume('*')
            return '*' + self.parse_factor() + self.parse_term_tail()
        else:
            return ''

    def parse_factor(self):
        if self.match('('):
            self.consume('(')
            result = '(' + self.parse_expression() + ')'
            self.consume(')')
            return result
        elif self.match_digit():
            return self.consume_digit()
        else:
            raise SyntaxError("Unexpected token")

    def match(self, expected):
        return self.current_index < len(self.input_string) and self.input_string[self.current_index] == expected

    def consume(self, expected):
        if self.match(expected):
            self.current_index += 1
        else:
            raise SyntaxError(f"Expected '{expected}', but found '{self.input_string[self.current_index]}'")

    def match_digit(self):
        return self.current_index < len(self.input_string) and self.input_string[self.current_index].isdigit()

    def consume_digit(self):
        result = self.input_string[self.current_index]
        self.current_index += 1
        return result


# Example usage
input_string = "2*(3+4)+5"
parser = Parser(input_string)

try:
    result = parser.parse()
    print(f"Parsing successful. Result: {result}")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
