#!/usr/bin/python
#
# Created by Max Marchuk

import sys
import jsonpickle

#Function to analyze the grammar
def analyze(grammar, string):

    #initialize all the things we'll need
    stack = []
    dict = grammar["mappings"]   #mapping of variables to rules
    variables = dict.keys()          
    terminals = getAlpha(grammar)

    stack.append(grammar["start_symbol"])

    #begin operation on string
    while stack and string:
        popped = stack.pop()

        if popped in variables:
            firstChar = string[0]
            rules = dict[popped]
            ruleFound = False

            for rule in rules:
                if rule[0] == firstChar:
                    ruleFound = True

                    for char in rule[::-1]:
                        stack.append(char)
                    break


            if ruleFound == False:
                return False

        if popped in terminals:
            if popped == string[0]: 
                string = string[1:]
            else:
                return False

    if stack == [] and string == "":
        return True
    else:
        return False

#Function to determine the alphabet of a language based on its grammar
def getAlpha(grammar):
    rules = grammar["mappings"].values()
    variables = grammar["mappings"].keys()
    terminals = []

    for rule_list in rules:
        for rule in rule_list:
            for character in rule:
                if character not in variables and character not in terminals:
                    terminals.append(character)
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
        string = sys.argv[2]
        grammar = parseFile(fileName)

        if analyze(grammar, string):
            print u'\u2713 "' + string + '" is in the language defined by the grammar.'
        else:
            print u'\u2717 "' + string + '" is NOT in the language defined by the grammar.'

