from utils import get_raw_data
from utils import prepare_text

path = "./spa.txt"

sp, en = get_raw_data(path)
sp, en = prepare_text(sp, en)