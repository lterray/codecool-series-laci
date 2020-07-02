from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def search_characters(phrase):
    phrase_words = phrase.split()
    where_condition = ''
    # { 'word_0': 'dan', 'word_1': 'laci' }
    params = {}

    for i, word in enumerate(phrase_words):
        key = 'word_' + str(i)

        if where_condition != '':
            where_condition += ' AND '

        where_condition += f'character_name ILIKE %({key})s'
        params[key] = '%' + word + '%'

    query = f'''
        SELECT
       show_characters.character_name,
       shows.title,
       actors.name
        FROM show_characters
        JOIN actors ON show_characters.actor_id = actors.id
        JOIN shows ON show_characters.show_id = shows.id
        WHERE {where_condition}
        '''

    print(query)
    print(params)

    return data_manager.execute_select(query, params)