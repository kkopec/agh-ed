from ed.noaa import NoaaDataProvider
from proverbs.kwiecien import Kwiecien

if __name__ == "__main__":
    kwiecien = Kwiecien(NoaaDataProvider)
    res = kwiecien.run()
    print('Kwiecien: {0}/{1}'.format(sum(x for x in res), len(res)))
