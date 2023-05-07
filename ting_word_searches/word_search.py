def exists_word(word, instance):
    current = list()
    new_list = list()
    range_instance = range(instance.__len__())
    for index in range_instance:
        line = instance.search(index)["linhas_do_arquivo"]
        range_line = range(len(line))
        for index_line in range_line:
            if word.lower() in line[index_line].lower():
                current.append({"linha": index_line + 1})
    if len(current) != 0 and len(current) > 0:
        obj = {
                "palavra": word,
                "ocorrencias": current,
                "arquivo": instance.search(index)["nome_do_arquivo"],
        }
        new_list.append(obj)
    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
