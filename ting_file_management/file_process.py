from .file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)
    item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    if item not in instance.queue:
        instance.enqueue(item)

    print(item, file=sys.stdout)


def remove(instance):
    if len(instance.queue) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        removed = instance.dequeue()
        print(
            f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso',
            file=sys.stdout
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
