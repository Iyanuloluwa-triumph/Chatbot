import wikipedia


def wiki(*args):
    query = " ".join(args).strip()
    try:
        if len(args) >= 2:
            return wikipedia.page(query, auto_suggest=False).content
        else:
            return wikipedia.summary(query, auto_suggest=False, sentences=5)
    except wikipedia.DisambiguationError as e:
        return f"sorry,did not find {query} did you mean {e.options}"
    except wikipedia.exceptions.PageError:
        return f"sorry could you rephrase? did you mean any of these\n{wikipedia.search(query)}"
    except Exception as e:
        return f"Error: {e}"


def wiki_def(n):
    try:
        return wikipedia.summary(n, auto_suggest=False)
    except wikipedia.DisambiguationError as e:
        return f"sorry,did not find {n} did you mean {e.options}"