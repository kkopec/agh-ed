from ed.noaa import NoaaDataProvider
import proverbs
import inspect

PROVIDER = NoaaDataProvider


def test_proverb(proverb_class):
    proverb = proverb_class(PROVIDER)
    res = proverb.run()
    format_results(proverb, res)


def format_results(proverb, results):
    print('-------------------------------')
    print('# {0}:'.format(proverb))
    [print('    - {0}:\t{1}/{2}'.format(k, sum(x for x in v), len(v))) for (k, v) in results.items()]


if __name__ == "__main__":
    proverbs_list = inspect.getmembers(proverbs, inspect.isclass)
    [test_proverb(proverb) for (name, proverb) in proverbs_list]

