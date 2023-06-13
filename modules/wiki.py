import wikipedia


def get_wiki_arcticale(artical):
    wikipedia.set_lang("ru")
    try:
        return wikipedia.summary(artical)
    except wikipedia.WikipediaException:
        return  "NE udalos naitu infu"

