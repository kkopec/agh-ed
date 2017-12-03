from proverbs.correspondence import Warm2Cold


class LutyCieply(Warm2Cold):
    """
    Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa
    """
    FIRST_MONTH = 2
    SECOND_MONTH = 3

    def __repr__(self):
        return u"Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa"
