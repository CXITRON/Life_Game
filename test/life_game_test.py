import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from life_game import LifeGame


def test_work_increases_money_and_decreases_health():
    game = LifeGame()
    game.apply_activity('work')
    assert game.stats['money'] == 100
    assert game.stats['health'] == 90
    assert game.stats['happiness'] == 45


def test_unknown_activity_raises_error():
    game = LifeGame()
    try:
        game.apply_activity('unknown')
    except ValueError as e:
        assert 'Unknown activity' in str(e)
    else:
        assert False, 'Expected ValueError'
