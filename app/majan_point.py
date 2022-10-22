from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld

class MajanPoint:
    def calc_kokushi(self):
        calculator = HandCalculator()
        tiles = TilesConverter.string_to_136_array(man='19', sou='19', pin='19', honors='12345677')
        win_tile = TilesConverter.string_to_136_array(honors='7')[0]

        result = calculator.estimate_hand_value(tiles, win_tile)
        return result.cost['main']
