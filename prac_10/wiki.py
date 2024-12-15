"""Wikipedia API & Python Library"""

import wikipedia


def main():
    """Get page title or search phrase, display page details."""

    search_string = input("Enter page title: ")
    while search_string != "":
        try:
            search_result = wikipedia.page(search_string, auto_suggest=False)
            print(search_result.title, search_result.summary.strip(),
                  search_result.url, sep='\n')
        except wikipedia.exceptions.PageError:  # e.g., input is "zvv"
            print(f'Page id "{search_string}" does not match any pages. '
                  f'Try another id!')
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, "
                  f"or a new search:\n{e.options[:5]}...")
        search_string = input("Enter page title: ")


main()
