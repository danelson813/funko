# funko/main.py
from utils.util import main, get_url
import pandas as pd
        

if __name__ == '__main__':
    results_ = []
    pages = int(2580/20+1)
    for i in range(pages):
        url = get_url(i)
        results_ += main(url)
    df = pd.DataFrame(results_)
    df.to_csv('data/results.csv', index=False)
 