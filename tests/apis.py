# Description: This file contains the functions for the api calls.

API_URL = "http://IP-Address:5000"

def post_message(message_prompt: str) -> int:
    message_json = json.dumps(message_prompt)
    print(message_json)
    return 404


def get_answer(message_id: int) -> str:
    return str(message_id) + " not implemented yet"


def put_answer() -> int:
    pass


def delete_message() -> int:
    pass







# Get a list of match ids by puuid.
def get_match_ids_by_puuid(
        api_key: str,
        puuid: str,
        start: int,
        match_type: str = 'ranked',
        count: int = 100,
        server: str = 'europe',
        start_time: float = 1672444800) -> requests.models.Response:
    return requests.get(
        "https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?startTime={}&type={}&start={}&count={}"
        .format(server, puuid, start_time, match_type, start, count), headers={"X-Riot-Token": api_key})

def get_puuid(self, summoner_name: str, server: str = 'euw1') -> str | None:
    """
    This function gets the puuid of a player from a SummonerDTO.

    Args:
        summoner_name (str): The player's summoner name.
        server (str): Server which the summoner is registered on.

    Returns:
        tuple (int, str): The status code and if the request was successful, the puuid.
    """
    # Call limiter functions to stay within api rate limitations.
    self._reset_rate_limit_counts()
    self._wait_if_needed()

    # Make api call
    self._logger.info(f"Calling get_summoner_by_name, name:{summoner_name}, server:{server}")
    response = summoner.get_summoner_by_name(self.api_key, summoner_name, server)
    if response.status_code != 200:
        self._logger.warning(f"Response, status:{response.status_code}, msg:{response.json()}")

    # Update rate_limit_counts
    for duration in self.rate_limits:
        self.rate_limit_counts[duration] += 1

    # Return results
    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        self._logger.warning(f'Failed requesting puuid for: {summoner_name}')
        return None