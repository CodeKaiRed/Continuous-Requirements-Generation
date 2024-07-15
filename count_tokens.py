import tiktoken
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

BASE_PRICE_PER_MILL = 0.5
INSTRUCT_BASE_PRICE_PER_MILL = 1.5
FINE_TUNE_BASE_PRICE_PER_MILL = 3.0
# encoding = tiktoken.get_encoding("cl100k_base")
# encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# tree = ET.parse('Dataset/1414117/XMLZIPFile/2009 - peppol approved.xml')
# root = tree.getroot()
# example = ET.tostring(root, encoding='utf8', method='xml')
# example = example.decode("utf-8")
with open("/Users/kailaniredding/Documents/School/Thesis/Development/data/output_srs.txt", "r") as file:
    example = file.read().replace('\n', ' ')

tkn_cnt = num_tokens_from_string(example, "gpt-3.5-turbo")

# print(f"CL100 Count is {cl100_token_count} tokens")
print(f"GPT 3.5 Turbo Count is {tkn_cnt} Tokens")
fine_tune_training_price = (FINE_TUNE_BASE_PRICE_PER_MILL / 1000000) * tkn_cnt

print(f"One epoch would cost ${fine_tune_training_price}")