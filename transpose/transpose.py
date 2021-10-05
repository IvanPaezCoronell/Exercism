import itertools


def transpose(lines):
    i = itertools.zip_longest(*lines.splitlines(), fillvalue='$')
    transp = '\n'.join(''.join(x).rstrip('$').replace('$', ' ') for x in i)
    return transp
