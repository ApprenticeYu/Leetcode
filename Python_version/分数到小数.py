class Solution:
    def fraction_to_decimal(self,numerator,denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)
        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        s.append(str(numerator // denominator))
        s,append('.')
        decimal_dict = {}
        value = numerator % denominator
        while value and value not in decimal_dict:
            decimal_dict[value] = len(s)
            value *= 10
            s.append(str(value // denominator))
            value %= denominator
        if value != 0:
            pos = decimal_dict[value]
            s.insert(pos,'(')
            s.append(')')
        return ''.join(s)
