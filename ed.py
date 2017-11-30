import inspect
import proverbs
from ed.noaa import NoaaDataProvider

PROVIDER = NoaaDataProvider


def test_proverb(Proverb):
    proverb = Proverb(PROVIDER)
    proverb.run()
    proverb.print_summary()


if __name__ == "__main__":
    Proverbs = inspect.getmembers(proverbs, inspect.isclass)
    [test_proverb(Proverb) for (name, Proverb) in Proverbs]
