import responses
from zerobounce.helper import ZeroBounceAPI


@responses.activate
def test_should_get_status_valid_when_validate_lowerjill(
        zerobounce, zerobounce_response_validate):
    responses.add(responses.GET,
                  'https://api.zerobounce.net/v1/validate?apikey=123456&email=flowerjill@aol.com',
                  json=zerobounce_response_validate,
                  status=200)

    zerobounce = zerobounce.validate("flowerjill@aol.com")

    assert zerobounce['status'] == "Valid"
    assert zerobounce['firstname'] == "Jill"
    assert zerobounce['lastname'] == "Stein"


def test_should_call_validate_service(
        mocker, zerobounce, zerobounce_response_validate):
    requests = mocker.patch.object(ZeroBounceAPI, "_requests")

    responses.add(responses.GET,
                  'https://api.zerobounce.net/v1/validate?apikey=123456&email=flowerjill@aol.com',
                  json=zerobounce_response_validate,
                  status=200)

    zerobounce.validate("flowerjill@aol.com")

    assert requests.called
    requests.assert_called_with(
        'validate', email='flowerjill@aol.com')
