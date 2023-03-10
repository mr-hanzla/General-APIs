
def cshow(msg):
    print('*'*50)
    print(msg)
    print('*'*50)


def get_in_h_tag(val, tag_number):
    return f'<h{tag_number}>{val}</h{tag_number}>'


def get_books():
    return [
        {
            'id': 0,
            'title': 'A Fire Upon the Deep',
            'author': 'Vernor Vinge',
            'first_sentence': 'The coldsleep itself was dreamless.',
            'year_published': '1992'
        },
        {
            'id': 1,
            'title': 'The Ones Who Walk Away From Omelas',
            'author': 'Ursula K. Le Guin',
            'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
            'published': '1973'
        },
        {
            'id': 2,
            'title': 'Dhalgren',
            'author': 'Samuel R. Delany',
            'first_sentence': 'to wound the autumnal city.',
            'published': '1975'
        }
    ]


def get_routes():
    return [
        '/api/v1/finance/',
        '/api/v1/finance/cal-tax',
        '/api/v1/math/',
        '/api/v1/math/circle/area',
        '/api/v1/math/formula/quadratic',
        '/api/v1/person/greet/<name>',
        '/',
        '/resume',
        '/header',
        '/manager',
        '/owner',
        '/greet/<name>',
        '/routes',
        '/api/v1/resources/books/all'
    ]
