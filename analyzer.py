#!/usr/bin/python
#
# Created by Max Marchuk
# View README.md for usage

import sys
import jsonpickle

#Function to analyze the grammar
def analyze(grammar, testString):

    mappings = grammar["mappings"]
    variables = mappings.keys()
    terminals = getAlpha(grammar)

    stack = []
    stack.append(grammar["start_symbol"])

    while testString and stack: 
        print "######STACK######: ", stack
        popped = stack.pop() 

        #if the popped element is a variable (i.e. non-terminal)
        if popped in variables:

            #ensure that the next character in the string is the start of a rule for the variable
            for rule in mappings[popped]:
                print rule
                if rule.startswith(testString[0]):
                    for char in rule:
                        stack.append(char) #push the rule's symbols onto the stack
                        print stack

                    testString = testString[1:] #remove the first character in the string
                    ruleExists = True
                    print "test string: " + testString    
                    break
                else:
                    ruleExists = False 
            if not ruleExists:
                return False

        elif popped in terminals:
            if popped == testString[0]:
                testString = testString[1:] #remove the first character in the string
            else:
                return False
    if not stack and not testString:
        return True
    else:
        return False

#Function to determine the alphabet of a language based on its grammar
def getAlpha(grammar):
    rules = grammar["mappings"]
    variables = grammar["mappings"].keys()
    terminals = []

    #Loop through all rules, removes variables, create list of all terminals
    for rule in rules:
        for string in rule:
            for char in string:
                if char not in variables:
                    terminals.append[char]
    terminals = set(terminals) #remove all duplicates BECAUSE WE CAN 
    return terminals

#Function to open the file and return the decoded file as an object
def parseFile(fileName):
    grammarFile = open(fileName, 'r').read()
    return jsonpickle.decode(grammarFile)

if __name__ == '__main__':
    if len(sys.argv) < 3: 
        print 'Correct usage: ./analyze.py <Encoded Grammar> <Test String>'
    else:
        fileName = sys.argv[1]
        testString = sys.argv[2]
        grammar = parseFile(fileName)

        if analyze(grammar, testString):
            print u'\u2713 "' + testString + '" is in the language defined by the grammar.'
        else:
            print u'\u2717 "' + testString + '" is NOT in the language defined by the grammar.'

