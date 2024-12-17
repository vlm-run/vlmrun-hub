from vlmrun.hub.schemas.media.nba_game_state import NBAGameState
from vlmrun.hub.schemas.media.nfl_game_state import NFLGameState


def test_nba_game_state_schema():
    data = {
        "description": "Lakers vs Warriors - Q3",
        "teams": [{"name": "Lakers", "score": 85}, {"name": "Warriors", "score": 82}],
        "status": "in_progress",
        "quarter": 3,
        "clock_time": "6:45",
    }
    game = NBAGameState(**data)
    assert len(game.teams) == 2
    assert game.teams[0].score == 85
