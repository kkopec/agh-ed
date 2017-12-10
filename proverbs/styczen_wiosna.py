from ed.proverb import Warm2Cold


class StyczenWiosna(Warm2Cold):
    FIRST_MONTH = 1
    SECOND_MONTH = 3

    def __repr__(self):
        return u"Bój się w styczniu wiosny, bo marzec zazdrosny"
