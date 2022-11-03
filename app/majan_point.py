from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld


class MajanPoint:
    def __init__(self):
        self.calculator = HandCalculator()

    def calc_point(self, hands: dict[str, str]=None, w_hands: dict[str, str]=None, dora_indicators: dict[str, str]=None, tsumo: bool = False):
        tiles = TilesConverter.string_to_136_array(
            man=hands['man'], sou=hands['sou'], pin=hands['pin'], honors=hands['honors'])
        win_tile = TilesConverter.string_to_136_array(
            man=w_hands['man'], sou=w_hands['sou'], pin=w_hands['pin'], honors=w_hands['honors'])[0]

        config = HandConfig(
            is_tsumo=tsumo, options=OptionalRules(has_open_tanyao=True))

        dora = None
        if dora_indicators is not None:
            dora = []
            for k, v in dora_indicators.items():
                if not v:
                    continue

                # count dora.
                for c in v:
                    if k is 'man':
                        dora += [TilesConverter.string_to_136_array(man=c)[0]]
                    if k is 'sou':
                        dora += [TilesConverter.string_to_136_array(sou=c)[0]]
                    if k is 'pin':
                        dora += [TilesConverter.string_to_136_array(pin=c)[0]]
                    if k is 'honors':
                        dora += [TilesConverter.string_to_136_array(honors=c)[0]]

        result = self.calculator.estimate_hand_value(
            tiles, win_tile, dora_indicators=dora, config=config)
        return result

    def calc_kokushi(self):
        tiles = TilesConverter.string_to_136_array(
            man='19', sou='19', pin='19', honors='12345677')
        win_tile = TilesConverter.string_to_136_array(
            man='', sou='', pin='', honors='7')[0]

        result = self.calculator.estimate_hand_value(tiles, win_tile)
        return result
