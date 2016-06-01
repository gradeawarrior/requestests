import requestests


def test_validations_using_builder_logic():
    pass
    # requestests.get(testing_url1) \
    #     .validate_code(requestests.codes.ok) \
    #     .validate_header_eq('Content-Type', 'text/html; charset=ISO-8859-1') \
    #     .validate_header_like('Content-Type', '^text/html')


def test_validate_code():
    pass
    # response1.validate_code(requestests.codes.ok)


def test_validate_not_code():
    pass
    # response1.validate_not_code(requestests.codes.created)


def test_validate_codes():
    pass
    # response1.validate_codes([requestests.codes.ok, requestests.codes.not_found, requestests.codes.created])


def test_validate_not_codes():
    pass
    # response1.validate_not_codes([requestests.codes.not_found, requestests.codes.created])


def test_validations_using_response1():
    pass
    # response1.validate_code(requestests.codes.ok)
    # response1.validate_header_eq('Content-Type', 'text/html; charset=ISO-8859-1')
    # response1.validate_header_like('Content-Type', '^text/html')


def test_restful_validations_using_builder_logic():
    pass
    # requestests.get(testing_url2) \
    #     .validate_code(requestests.codes.ok) \
    #     .validate_header_eq('Content-Type', 'application/json') \
    #     .validate_header_like('Content-Type', 'application/json')


def test_restful_validate_code():
    pass
    # response2.validate_code(requestests.codes.ok)


def test_restful_validate_not_code():
    pass
    # response2.validate_not_code(requestests.codes.created)


def test_restful_validate_codes():
    pass
    # response2.validate_codes([requestests.codes.ok, requestests.codes.not_found, requestests.codes.created])


def test_restful_validate_not_codes():
    pass
    # response2.validate_not_codes([requestests.codes.not_found, requestests.codes.created])


def test_restful_validations_using_response():
    pass
    # response2.validate_code(requestests.codes.ok)
    # response2.validate_header_eq('Content-Type', 'application/json')
    # response2.validate_header_like('Content-Type', 'application/json')


def test_restful_validate_content():
    pass
    # response2.validate_content('id')


def test_restful_validate_entity_exact_match():
    pass
    # playlist = requestests.get(testing_url2) \
    #     .validate_code(requestests.codes.ok) \
    #     .json_decode(Playlist)
    # response2.validate_entity_eq(playlist)


def test_restful_validate_entity_similar_match():
    pass
    # playlist = Playlist()
    # playlist.playlist_id = "DolbyTestPlaylist"
    # playlist.display = {'en_US': Locale()}
    # playlist.display['en_US'].title = 'Dolby Atmos Test'
    # response2.validate_entity_eq(playlist)
