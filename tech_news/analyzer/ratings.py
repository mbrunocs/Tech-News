from tech_news.database import find_news


# ref: https://stackoverflow.com/questions/1143671/
#       how-to-sort-objects-by-multiple-keys
def top_5_news():
    result = [row for row in find_news() if row["comments_count"] > 0]
    return [(row["title"], row["url"]) for row in sorted(
        result, key=lambda k: (-k['comments_count'], k['title']))][:5]


# ref: https://stackoverflow.com/questions/613183/
#       how-do-i-sort-a-dictionary-by-value
def top_5_categories():
    count_egories = dict()
    for row in find_news():
        if row["category"] in dict.keys(count_egories):
            count_egories[row["category"]] += 1
        else:
            count_egories[row["category"]] = 1

    return [k for k, v in sorted(
        count_egories.items(), key=lambda i: (-i[1], i))][:5]
