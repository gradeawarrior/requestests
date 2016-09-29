import requests
import requestests


class TestRequestests:
    test_url = 'http://www.google.com'

    def test_ttlb_and_request_url_using_requestests(self):
        response = requestests.get(self.test_url) \
            .validate_code(requestests.codes.ok)
        assert response.ttlb > 0, "There is a valid TTLB in Response - ttlb: {}".format(response.ttlb)
        assert response.request_url, "There is a valid request_url in Response - url: {}".format(response.request_url)

    def test_ttlb_and_request_url_using_requests(self):
        response = requests.get(self.test_url) \
            .validate_code(requests.codes.ok)
        assert response.ttlb > 0, "There is a valid TTLB in Response - ttlb: {}".format(response.ttlb)
        assert response.request_url, "There is a valid request_url in Response - url: {}".format(response.request_url)

    def test_validate_ttlb(self):
        requestests.get(self.test_url) \
            .validate_code(requestests.codes.ok) \
            .validate_ttlb_lt(60)

    def test_validate_duration(self):
        requestests.get(self.test_url) \
            .validate_code(requestests.codes.ok) \
            .validate_duration_lt(60)

    def test_validate_ttlb_failure(self):
        try:
            requestests.get(self.test_url) \
                .validate_code(requestests.codes.ok) \
                .validate_ttlb_lt(0)
            assert False, "Expected validate duration < 0 to fail"
        except AssertionError:
            pass

    def test_validate_duration_failure(self):
        try:
            requestests.get(self.test_url) \
                .validate_code(requestests.codes.ok) \
                .validate_duration_lt(0)
            assert False, "Expected validate duration < 0 to fail"
        except AssertionError:
            pass

    def test_validations_using_builder_logic(self):
        pass
        # requestests.get(testing_url1) \
        #     .validate_code(requestests.codes.ok) \
        #     .validate_header_eq('Content-Type', 'text/html; charset=ISO-8859-1') \
        #     .validate_header_like('Content-Type', '^text/html')

    def test_validate_code(self):
        requests.get(self.test_url).validate_code(requests.codes.ok)

    def test_validate_code_failure(self):
        try:
            requests.get(self.test_url).validate_code(requests.codes.not_found)
            assert False, "Expected validate_code to fail"
        except AssertionError:
            pass

    def test_validate_not_code(self):
        pass
        # response1.validate_not_code(requestests.codes.created)

    def test_validate_codes(self):
        pass
        # response1.validate_codes([requestests.codes.ok, requestests.codes.not_found, requestests.codes.created])

    def test_validate_not_codes(self):
        pass
        # response1.validate_not_codes([requestests.codes.not_found, requestests.codes.created])

    def test_validations_using_response1(self):
        pass
        # response1.validate_code(requestests.codes.ok)
        # response1.validate_header_eq('Content-Type', 'text/html; charset=ISO-8859-1')
        # response1.validate_header_like('Content-Type', '^text/html')

    def test_restful_validations_using_builder_logic(self):
        pass
        # requestests.get(testing_url2) \
        #     .validate_code(requestests.codes.ok) \
        #     .validate_header_eq('Content-Type', 'application/json') \
        #     .validate_header_like('Content-Type', 'application/json')

    def test_restful_validate_code(self):
        pass
        # response2.validate_code(requestests.codes.ok)

    def test_restful_validate_not_code(self):
        pass
        # response2.validate_not_code(requestests.codes.created)

    def test_restful_validate_codes(self):
        pass
        # response2.validate_codes([requestests.codes.ok, requestests.codes.not_found, requestests.codes.created])

    def test_restful_validate_not_codes(self):
        pass
        # response2.validate_not_codes([requestests.codes.not_found, requestests.codes.created])

    def test_restful_validations_using_response(self):
        pass
        # response2.validate_code(requestests.codes.ok)
        # response2.validate_header_eq('Content-Type', 'application/json')
        # response2.validate_header_like('Content-Type', 'application/json')

    def test_restful_validate_content(self):
        pass
        # response2.validate_content('id')

    def test_restful_validate_entity_exact_match(self):
        pass
        # playlist = requestests.get(testing_url2) \
        #     .validate_code(requestests.codes.ok) \
        #     .json_decode(Playlist)
        # response2.validate_entity_eq(playlist)

    def test_restful_validate_entity_similar_match(self):
        pass
        # playlist = Playlist()
        # playlist.playlist_id = "DolbyTestPlaylist"
        # playlist.display = {'en_US': Locale()}
        # playlist.display['en_US'].title = 'Dolby Atmos Test'
        # response2.validate_entity_eq(playlist)
