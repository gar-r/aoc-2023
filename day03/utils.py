def pretty_print(data):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]))
