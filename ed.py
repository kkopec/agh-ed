from ed.noaa import NoaaDataProvider
import proverbs
import inspect

PROVIDER = NoaaDataProvider


def test_proverb(Proverb):
    proverb = Proverb(PROVIDER)
    res = proverb.run()
    format_results(proverb, res)


def format_results(proverb, results):
    print('-------------------------------')
    print('# {0}:'.format(proverb))
    [print('    - {0: <12}{1}/{2}'.format(k, sum(x for x in v), len(v))) for (k, v) in results.items()]


if __name__ == "__main__":
    Proverbs = inspect.getmembers(proverbs, inspect.isclass)
    [test_proverb(Proverb) for (name, Proverb) in Proverbs]

