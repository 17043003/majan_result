from fastapi import APIRouter, HTTPException

import majan_point

router = APIRouter()


@router.get("/point")
async def detail_point(
    m: str = '', s: str = '', p: str = '', h: str = '',
    w_m: str = '', w_s: str = '', w_p: str = '', w_h: str = '',
    opens: str = '',
    own_wind: int = 0, field_wind: int = 0,
    tsumo: bool = False, yakus: str = '000000', ):

    mp = majan_point.MajanPoint()
    hands = {'man': m, 'sou': s, 'pin': p, 'honors': h}
    win_hand = {'man': w_m, 'sou': w_s, 'pin': w_p, 'honors': w_h}

    sum_count = 1
    for count in hands.values():
        sum_count += len(count)

    melds = opens.split('_')
    sum_count += len(melds) * 3
    
    if(sum_count < 14 ):
        raise HTTPException(status_code=404, detail="hands are lack.")

    return mp.calc_point(hands, win_hand, opens=melds, own_wind=own_wind, field_wind=field_wind, tsumo=tsumo, yakus=yakus)


@router.get("/point/kokushi")
async def get_kokushi_point():
    mp = majan_point.MajanPoint()
    return mp.calc_kokushi()
