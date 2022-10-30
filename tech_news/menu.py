import sys
# from datetime import date
# import tech_news.analyzer.ratings as ratings
# import tech_news.analyzer.search_engine as search
# import tech_news.scraper as scraper


def show_menu():
    input(
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


def analyzer_menu():
    show_menu()
    _, path, args = sys.argv
    # command = dict({
    #     '0': ():
    #         input("Digite quantas notícias serão buscadas:")
    #         scraper.get_tech_news(command)
    # })
    # try:
    #     if '0' in path:
    #         command = input("Digite quantas notícias serão buscadas:")
    #         scraper.get_tech_news(command)
    #     elif '1' in path:
    #         command = input("Digite o título:")
    #         search.search_by_title(command)
    #     elif '2' in path:
    #         command = input("Digite a data no formato aaaa-mm-dd:")
    #         search.search_by_date(date(command))
    #     elif '3' in path:
    #         command = input("Digite a tag:")
    #         search.search_by_tag(command)
    #     elif '4' in path:
    #         command = input("Digite a categoria:")
    #         search.search_by_category(command)
    #     elif '5' in path:
    #         ratings.top_5_news()
    #     elif '6' in path:
    #         ratings.top_5_categories()
    #     elif '7' in path:
    #         sys.stdout.write = "Encerrando script"
    # except ValueError:
    #     sys.stderr.write = "Opção inválida"
