from utils import get_raw_data, tokenizer
from utils import prepare_text
from utils import remove_sentences_with_unknown_tokens

path = "./spa.txt"

maxlen = 3000

sp, en = get_raw_data(path)
sp, en = prepare_text(sp, en)

sp_token, sp_mapper = tokenizer(sp, maxlen)
en_token, en_mapper = tokenizer(en, maxlen)

sp_data, en_data = remove_sentences_with_unknown_tokens(sp_token, en_token, sp_mapper, en_mapper)

assert len(sp_data)==len(en_data)

for i in range(10):
    print(len(en_data[i]))    
