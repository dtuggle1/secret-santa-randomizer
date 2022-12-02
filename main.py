import string
import random
import pprint
import copy
import collections

PREVENT_LIST = {
    'Mei Mey': ['Paul'],
    'Paul': ['Mei Mey'],
    'Malaya': ['Derek'],
    'Derek': ['Malaya'],
    'Louisa': ['Da', 'James'],
    'Da': ['Louisa'],
    'James': ['Louisa'],
    'Nokyoon': [],
}


def code_generator():
    code = 'AA'
    for _ in range(10):
        code += random.choice(string.ascii_uppercase)
    return code


def build_codebook():
    codebook = {}
    for name in PREVENT_LIST:
        codebook[name] = code_generator()
    return codebook


def assigment_generation(codebook):
    possible_assignments = list(PREVENT_LIST.keys())
    assignments_dict = {}
    for name in PREVENT_LIST:
        invalid_list = copy.deepcopy(PREVENT_LIST[name])
        invalid_list.append(name)
        if collections.Counter(possible_assignments) == collections.Counter(invalid_list):
            return False
        valid_assignment = False
        while not valid_assignment:
            potential_assignment = random.choice(possible_assignments)
            if potential_assignment not in PREVENT_LIST[name] and potential_assignment != name:
                valid_assignment = True
            assignment = potential_assignment
        possible_assignments.remove(assignment)
        assignments_dict[name] = codebook[assignment]
    return assignments_dict


def reverse_codebook(codebook):
    reversed_codebook = {}
    for name, code in codebook.items():
        reversed_codebook[code] = name
    return reversed_codebook


def code_testing(codebook, assignments):
    codebook = reverse_codebook(codebook)
    assignment_values_code = assignments.values()
    assignment_values = [codebook[assignment_code] for assignment_code in assignment_values_code]

    for name in PREVENT_LIST:
        assignment = codebook[assignments[name]]
        if assignment in PREVENT_LIST[name] or assignment == name:
            raise ValueError('Incorrect assignment bug')
        if name not in assignment_values:
            raise ValueError('Someone not assigned bug')

if __name__ == '__main__':
    codebook = build_codebook()
    assignments = False
    while not assignments:
        assignments = assigment_generation(codebook)
        if not assignments:
            continue
        if assignments['Malaya'] != codebook['Mei Mey']:
            assignments = False
    code_testing(codebook, assignments)
    print('codebook')
    pprint.pprint(reverse_codebook(codebook))
    print()
    print('assignments')
    pprint.pprint(assignments)