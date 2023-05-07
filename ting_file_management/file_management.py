import sys


def txt_importer(path_file):
    txt_file = open(path_file, 'r')
    while txt_file:
        if path_file[-1:-4] != '.txt' and txt_file is not None:
            print('Formato inválido', file=sys.stderr)
        else:
            raise FileNotFoundError
        return txt_file.read().split(sep='\n')
