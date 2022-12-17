import cexprtk

name = 'Math plugin'
description = 'This plugin tries to parse the query to an expression and evaluate it'
default_on = True  # enabled by default
js_dependencies = tuple()
css_dependencies = tuple()

st = cexprtk.Symbol_Table({}, add_constants=True)


def post_search(request, search):
    query = search.search_query.query.strip()
    try:
        expr = cexprtk.Expression(query, st)
        search.result_container.answers["Calculator"] = {"answer": f"{query} = {expr():.4f}"}
    except cexprtk._exceptions.ParseException:
        pass
