import responses
from zerobounce.helper import ZeroBounceAPI


@responses.activate
def test_should_get_2375323_of_credit(zerobounce, zerobounce_response_getcredits):

    responses.add(responses.GET,
                  'https://api.zerobounce.net/v1/getcredits?apikey=123456',
                  json=zerobounce_response_getcredits,
                  status=200)

    assert zerobounce.get_credits() == 2375323


def test_should_call_validate_service(
        mocker, zerobounce, zerobounce_response_getcredits):
    requests = mocker.patch.object(ZeroBounceAPI, "_requests")

    responses.add(responses.GET,
                  'https://api.zerobounce.net/v1/getcredits?apikey=123456',
                  json=zerobounce_response_getcredits,
                  status=200)

    zerobounce.get_credits()

    assert requests.called
    requests.assert_called_with('getcredits')
