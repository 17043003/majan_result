from fastapi import APIRouter, HTTPException

from model import wait_tile

router = APIRouter()


@router.get("/wait")
async def wait_tiles(
    m: str = '', s: str = '', p: str = '', h: str = '', opens: str = ''
):
    hands = {'man': m, 'sou': s, 'pin': p, 'honors': h}
    wait = wait_tile.WaitTile()
    return { "win": wait.get_wait_tiles(hands, opens) }