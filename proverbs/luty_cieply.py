from proverbs.cieplo_zimno import CieploZimno


class LutyCieply(CieploZimno):
    """
    Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa
    """
    month_warm = 2
    month_cold = 3

    def __repr__(self):
        return u"Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa"
