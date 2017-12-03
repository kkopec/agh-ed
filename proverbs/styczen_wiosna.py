from proverbs.correspondence import Warm2Cold


class StyczenWiosna(Warm2Cold):
    """
    Bój się w styczniu wiosny, bo marzec zazdrosny

    łagodna pogoda w styczniu zapowiada mrozy w marcu
    
    średnia temperatura ze stycznia z wielu lat, tak samo z marca 
    i jeśli w konkretnym roku w styczniu jest wyższa niż ogólna 
    to w marcu powinna być niższa niż ogólna
    """
    FIRST_MONTH = 1
    SECOND_MONTH = 3

    def __repr__(self):
        return u"Bój się w styczniu wiosny, bo marzec zazdrosny"
