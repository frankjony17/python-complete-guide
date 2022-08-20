import builtins

import ast


def for_equal(false_assignments, source_list, words, i):
    if source_list[i] == '=':
        if words in source_list[i - 1] and i:
            false_assignments.append(words)
    return false_assignments


def for_function(false_assignments, source_list, words, i):
    if source_list[i] == 'def':
        source = source_list[i + 1].split('(')[0]
        if source == words:
            false_assignments.append(source)
    return false_assignments

def for_str(false_assignments, source_list, words, i):
    if 'str' in source_list[i] and source_list[i - 1] in ['return', 'class'] and 'str' == words:
        false_assignments.append(source_list[i][0:3])

    return false_assignments

def for_error(source):
    try:
        ast.parse(source)
        return False
    except SyntaxError:
        return True


def for_parameters(false_assignments, source_list, words, i):
    if 'iter' in source_list[i] and 'iter' == words:
        false_assignments.append(source_list[i][0:4])
    if 'set' in source_list[i] and 'set' == words:
        false_assignments.append('set')
    if 'list' in source_list[i] and 'list' == words:
        false_assignments.append('list')
    return false_assignments


def find_variable_assignments(source, target_var_names):
    false_assignments = []
    source_list = source.split()

    # if for_error(source):
    #     return []

    for i in range(len(source_list)):
        for words in target_var_names:
            false_assignments = for_equal(false_assignments, source_list, words, i)
            false_assignments = for_function(false_assignments, source_list, words, i)
            false_assignments = for_str(false_assignments, source_list, words, i)
            false_assignments = for_parameters(false_assignments, source_list, words, i)

    return set(false_assignments)


src = """
def fn(): 
    next,dir,list,dir = 1,2,3,"bin = 4"
str = 45
"""
expected = ["next", "str", "dir", "list"]

targets = dir(builtins)
print(find_variable_assignments(src, targets))
