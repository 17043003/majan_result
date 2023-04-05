from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld

class WaitTile:
    def __init__(self):
        self.calculator = HandCalculator()

    def get_wait_tiles(self, hands: dict[str, str]=None, opens: str=None):

        # TODO: 鳴きの牌を手牌に変換
        open_tiles = OpenTile(opens)

        pon = Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(man='444'))
        chi = Meld(meld_type=Meld.CHI, tiles=TilesConverter.string_to_136_array(man='444'))
        ankan = Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man='444'))
        minkan = Meld(meld_type=Meld.SHOUMINKAN, tiles=TilesConverter.string_to_136_array(man='444'))

        melds = [Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(man='444'))]


        config = HandConfig(options=OptionalRules(has_open_tanyao=True))

        dora = None

        def get_wait_tile(win_tile):
            tiles = TilesConverter.string_to_136_array(
                man=hands['man'] + (win_tile.get('man') or ""),
                sou=hands['sou'] + (win_tile.get('sou') or ""),
                pin=hands['pin'] + (win_tile.get('pin') or ""),
                honors=hands['honors'] + (win_tile.get('honors') or ""),
            )
            print(tiles)

            w_tile = TilesConverter.string_to_136_array(
                man=win_tile.get('man'),
                sou=win_tile.get('sou'),
                pin=win_tile.get('pin'),
                honors=win_tile.get('honors')
            )[0]

            w = TilesConverter.to_one_line_string([w_tile])

            result = self.calculator.estimate_hand_value(tiles, w_tile, config=config)
            print(result.error, w_tile, w)
            if(result.error is "hand_not_winning"):
                return None
            elif(result.error is "no_yaku"):
                return { "tile": w, "error": result.error }
            else:
                return { "tile": w, "error": "null" }

        
        mans = [{ 'man': str(i) } for i in range(1, 10)]
        sous = [{ 'sou': str(i) } for i in range(1, 10)]
        pins = [{ 'pin': str(i) } for i in range(1, 10)]
        honors = [{ 'honors': str(i) } for i in range(1, 8)]

        all_tiles = mans + sous + pins + honors
        win_hands = list(map(get_wait_tile, all_tiles))
        return [ hand for hand in win_hands if hand != None]

class OpenTile:
    def __init__(self, opens):
        self.opens = opens