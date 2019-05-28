from armadillo_4cd import decipher


def test():
    data = {}
    data['cifrado'] = 'aboboraz.45#'
    data['numero_casas'] = 11
    data['decifrado'] = ''
    assert decipher(data) == 'lmzmzclk.45#'
    data['cifrado'] = 'luis.fernando1\''
    data['numero_casas'] = 11
    data['decifrado'] = ''
    assert decipher(data) == 'wftd.qpcylyoz1\''


if __name__ == '__main__':
    test()
