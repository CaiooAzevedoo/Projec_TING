import sys


def txt_importer(path_file):
    try:
        txt_file = open(path_file, 'r')
        while txt_file:
            if path_file[-1:-4] != '.txt' and txt_file is not None:
                print('Formato inválido', file=sys.stderr)
            return txt_file.read().split(sep='\n')
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
