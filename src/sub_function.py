from pydantic import BaseModel
import time, re

class schema_check_text(BaseModel):
    securities: str
    cut: int
    type: str
    change: float

async def check_text(text: str):
    item = re.search(r' [A-Z]+:', text)
    cut = int(item.span()[0]+1)
    item = item[0][1:-1]

    if re.search(r'открытия', text):
        type = "change_open"
        change = float(re.search(r'\d+[.]?[\d]?', text)[0])
        
    elif re.search(r'Крупная', text):
        type = "many_lot"
        change = float(re.search(r'\d+[.]+\d+', text)[0])*1000000

    elif re.search(r'Резкое', text):
        type = "change_volume"
        change = float(re.search(r'\d+[.]+\d?', text)[0])

    return schema_check_text(securities=item, cut=cut, type=type, change=change)
