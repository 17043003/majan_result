import re

from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld

class MajanPoint:
    def __init__(self):
        self.calculator = HandCalculator()

    def calc_point(self,
        hands: dict[str, str]=None,
        w_hands: dict[str, str]=None,
        opens=[], own_wind=0, field_wind=0,
        tsumo: bool = False, yakus: str = '000000'):

        # add w_hands to hands.
        wh = [{k: v} for k, v in w_hands.items() if v != ''][0]
        w_kind = list(wh.keys())[0]
        hands[w_kind] += wh[w_kind]

        def char_to_kind(c):
            if c == 'm': return 'man'
            elif c == 's': return 'sou'
            elif c == 'p': return 'pin'
            else: return 'honors'

        for t in opens:
            kind = char_to_kind(t[0])
            
            nums = re.sub(r"\D", "", t)
            hands[kind] += nums


        tiles = TilesConverter.string_to_136_array(
            man=hands['man'], sou=hands['sou'], pin=hands['pin'], honors=hands['honors'])
        win_tile = TilesConverter.string_to_136_array(
            man=w_hands['man'], sou=w_hands['sou'], pin=w_hands['pin'], honors=w_hands['honors'])[0]

        def to_meld(str):
            if(len(str) < 5):
                return None

            meld_kind = str[-1]
            types = { 'p': Meld.PON, 'c': Meld.CHI, 'k': Meld.KAN, 'o': Meld.SHOUMINKAN }

            nums = re.sub(r"\D", "", str)
            tile_kind = str[0]

            if(tile_kind == 'm'):
                tiles = TilesConverter.string_to_136_array(man=nums)
            elif(tile_kind == 's'):
                tiles = TilesConverter.string_to_136_array(sou=nums)
            elif(tile_kind == 'p'):
                tiles = TilesConverter.string_to_136_array(pin=nums)
            else:
                tiles = TilesConverter.string_to_136_array(honors=nums)

            return Meld(meld_type=types[meld_kind], tiles=tiles)

        melds = []
        if(len(opens) > 0):
            melds = [x for x in [to_meld(o) for o in opens] if x ]

        WINDS = [27, 28, 29, 30]

        # get some yakus.
        is_reach = (yakus[0] == '1') if len(yakus) > 0 else False
        is_double_reach = (yakus[1] == '1') if len(yakus) > 1 else False
        is_ippatsu = (yakus[2] == '1') if len(yakus) > 2 else False
        is_rinshan = (yakus[3] == '1') if len(yakus) > 3 else False
        is_haitei = (yakus[4] == '1') if len(yakus) > 4 else False
        is_chankan = (yakus[5] == '1') if len(yakus) > 5 else False

        config = HandConfig(
            is_tsumo=tsumo,
            is_riichi = is_reach,
            is_daburu_riichi = is_double_reach,
            is_ippatsu = is_ippatsu,
            is_rinshan = is_rinshan,
            is_chankan = is_chankan,
            is_haitei = tsumo and is_haitei,
            is_houtei = (not tsumo) and is_haitei,
            player_wind=WINDS[own_wind],
            round_wind=WINDS[field_wind],
            options=OptionalRules(has_open_tanyao=True))


        def hands_added_melds(tiles, melds):
            print(melds[0].tiles)
        
        hands_added_melds(tiles, melds)

        print(tiles, win_tile, melds)

        result = self.calculator.estimate_hand_value(
            tiles, win_tile, melds=melds, config=config)
        return result


    def calc_kokushi(self):
        tiles = TilesConverter.string_to_136_array(
            man='19', sou='19', pin='19', honors='12345677')
        win_tile = TilesConverter.string_to_136_array(
            man='', sou='', pin='', honors='7')[0]

        result = self.calculator.estimate_hand_value(tiles, win_tile)
        return result
