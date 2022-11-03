from fastapi import APIRouter

import majan_point

router = APIRouter()


@router.get("/point")
async def detail_point(
    m: str = '', s: str = '', p: str = '', h: str = '',
    w_m: str = '', w_s: str = '', w_p: str = '', w_h: str = '',
    dora_m: str = '', dora_s: str = '', dora_p: str = '', dora_h: str = '',
    tsumo: bool = False, bakaze: str='00'):

    mp = majan_point.MajanPoint()
    hands = {'man': m, 'sou': s, 'pin': p, 'honors': h}
    win_hand = {'man': w_m, 'sou': w_s, 'pin': w_p, 'honors': w_h}
    
    dora_indicators = {'man': dora_m, 'sou': dora_s, 'pin': dora_p, 'honors': dora_h}
    if all(not v for v in dora_indicators.values()):
        dora_indicators = None

    return mp.calc_point(hands, win_hand, dora_indicators, tsumo=tsumo)


@router.get("/point/kokushi")
async def get_kokushi_point():
    mp = majan_point.MajanPoint()
    return mp.calc_kokushi()
