from ed.wwodataprovider import WWODataProvider
from ed.wwoadapter import WWOAdapter
from proverbs.kwiecien import Kwiecien

if __name__ == "__main__":
    dp = WWODataProvider()
    kwiecien = Kwiecien(dp, WWOAdapter)
    kwiecien.run()


