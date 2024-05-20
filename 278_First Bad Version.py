# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def firstBadVersion(self, n: int) -> int:
    lo , hi = 1, n
    while lo<=hi:
        mi = (lo+hi)//2
        if isBadVersion(mi):
            if mi == 1 or not isBadVersion(mi-1):
                return mi
            else:
                hi = mi-1
        else:
            lo = mi+1    
    return None            

        