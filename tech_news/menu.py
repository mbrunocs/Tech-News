import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_tag, search_by_category)
from tech_news.scraper import get_tech_news


def show_menu():
    return input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""",
    )


def num_news():
    command = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(command)


def src_news():
    command = input("Digite o título:")
    return search_by_title(command)


def src_by_date():
    command = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(command)


def src_by_tag():
    command = input("Digite a tag:")
    return search_by_tag(command)


def src_by_cat():
    command = input("Digite a categoria:")
    return search_by_category(command)


def shutdown():
    return print("Encerrando script\n")


def get_5_news():
    return top_5_news()


def get_5_cat():
    return top_5_categories()


def verify_input(string, command):
    if string not in command or string == "":
        raise KeyError
    return string


def analyzer_menu():
    try:
        command = dict({
            '0': num_news,
            '1': src_news,
            '2': src_by_date,
            '3': src_by_tag,
            '4': src_by_cat,
            '5': get_5_news,
            '6': get_5_cat,
            '7': shutdown,
        })
        opt = verify_input(show_menu(), command)
        return command[opt]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")
# path do sys.argv, controle somente do comando tech-news-analyzer?
#       preciso de outros args? necessário apenas pra teste no terminal?
# + outros erros
