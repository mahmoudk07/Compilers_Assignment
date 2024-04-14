from collections import deque
class RE_Postifix():
    def __init__(self, regex):
        self.regex = regex
        self.operators = ['*', '+', '?', '#', '|']
        self.alpha_numeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z',
                          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@' , '.' , '$' , '%' , '_', '!', ':' , '/']
        self.postifix = ""
        self.stack = deque()
        self.precedence = {
            '*' : 5,
            '+' : 4,
            '?' : 3,
            '#' : 2,
            '|' : 1
        }
    def handling_sqaure_brackets(self) -> str:
        i = 0
        while (i + 1) != len(self.regex):
            if self.regex[i] == '[':
                j = i + 1
                while self.regex[j] != ']':
                    if self.regex[j] == '-' and self.regex[j + 1] in self.alpha_numeric:
                        self.regex = self.regex[:j + 2] + '|' + self.regex[j + 2:]
                    if self.regex[j] in self.alpha_numeric and self.regex[j + 1] in self.alpha_numeric:
                        self.regex = self.regex[:j + 1] + '|' + self.regex[j + 1:]
                    j += 1
                if self.regex[j - 1] == '|':
                    self.regex = self.regex[: j - 1] + self.regex[j:]
                    i = j - 1
                else:
                    i = j
            else:
                i += 1
        return self.regex
            
    def regex_preprocessing(self) -> str:
        i = 0
        while i < len(self.regex):
            if i + 1 < len(self.regex) and self.regex[i] in ['*' , '+' , '?' , ')' , ']'] and self.regex[i + 1] not in ['*' , '+' , '?' , ')' , ']' , '|']:
                self.regex = self.regex[:i + 1] + '#' + self.regex[i + 1:]
            elif i + 1 < len(self.regex) and self.regex[i] in self.alpha_numeric and (self.regex[i + 1] in ['(' , '['] or self.regex[i + 1] in self.alpha_numeric):
                self.regex = self.regex[:i + 1] + '#' + self.regex[i + 1:]
            i += 1
        return self.regex
    def regex_to_postifix(self):
        i = 0
        while i < len(self.regex):

            if self.regex[i] in self.alpha_numeric:
                self.postifix += self.regex[i]

            elif self.regex[i] == ')' or self.regex[i] == ']':
                while len(self.stack) > 0 and self.stack[-1] not in ['(' , '[']:
                    self.postifix += self.stack.pop()
                if not len(self.stack):
                    return False , ""
                self.stack.pop()

            elif self.regex[i] == '(' or self.regex[i] == '[':
                self.stack.append(self.regex[i])
            
            elif self.regex[i] in self.operators:
                while len(self.stack) > 0 and self.stack[-1] in self.precedence and self.precedence[self.regex[i]] <= self.precedence[self.stack[-1]]:
                    self.postifix += self.stack.pop()
                self.stack.append(self.regex[i])

            else:
                previous_character = self.regex[i - 1]
                next_character = self.regex[i + 1]
                if previous_character not in self.alpha_numeric and next_character not in self.alpha_numeric:
                    return False , ""
                self.postifix += self.regex[i]
                # range_characters = []
                # for character in self.alpha_numeric:
                #     if ord(character) > ord(previous_character) and ord(character) < ord(next_character):
                #         range_characters.append('|')
                #         range_characters.append(character)
                # range_characters.append('|')    
                # self.regex = self.regex[:i + 1] + "".join(range_characters) + self.regex[i + 1:]
            i += 1

        while len(self.stack) > 0:
            if self.stack[-1] in ['(' , '[']:
                return False , ""
            self.postifix += self.stack.pop()
        return True , self.postifix
    
    def postifix_to_NFA(self):
        pass
    def nfa_visualizing(self):
        pass

"""
loop for every character in regex:
1- if character is alphanumric -> push it into postifix string
2- if character is operator:
    - if stack not empty and top of stack has precedence higher than current operator -> pop from stack and push into postifix string(unti precedence of current is higher) and then push current
    - else -> push current operator into stack
3- if character is '(' or '[' -> push character into stack (if [ set flag to be True)
4- if character is ')' or ']' -> pop from stack until you reach to first opening parenthesis (if ] set flag to be False) 
5- if character is -:
    - get character before - and character after -
    - and then insert to infix each character between first and last and | after each character
    - check also if - is between to valid character if not return false
"""

regex = "ab(b|c)*d+"
re_nfa = RE_Postifix(regex)
regex = re_nfa.handling_sqaure_brackets()
preprocessed_regex = re_nfa.regex_preprocessing()
print(preprocessed_regex)
exist, postifix = re_nfa.regex_to_postifix()
print(postifix,exist)




