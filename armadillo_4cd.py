import requests
import json
from hashlib import sha1


def request():
    try:
        url = requests.get(
            'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=1d0408fc4d2159e2b0446a0f4c3f0c525145ef69'
        )
        data_request = url.json()  # stores the response. data_request = dict
        decipher(data_request)
    except:
        print('Não foi possível obter resposta da url especificada.'
              '\nVerique sua conexão com a Internet!')


def post():
    with open("answer.json", "rb") as f:
        headers = {'Content-Type': 'multipart/form-data'}
        url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=1d0408fc4d2159e2b0446a0f4c3f0c525145ef69'
        files = {'answer': ('answer.json', f, 'multipart/form-data')}
        r = requests.post(url, files=files)
    print(r.status_code)
    print(r.json())


def decipher(data_loaded):
    text_encrypted = data_loaded['cifrado'].lower()
    text_deciphered = ''
    number_jump = data_loaded['numero_casas']
    especial_caract = '.’'
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in text_encrypted:
        if letter in especial_caract or letter.isdigit() or letter.isspace():
            text_deciphered += letter
        elif letter in alphabet:
            position_letter = alphabet.index(letter)+1
            new_letter = (position_letter - number_jump) % len(alphabet) if (position_letter - number_jump) != 0 \
                else len(alphabet)
            text_deciphered += alphabet[new_letter-1]
    data_loaded['decifrado'] = text_deciphered
    string_hash(data_loaded)
    return data_loaded['decifrado']


def string_hash(data_loaded):
    text = bytes(data_loaded['decifrado'], 'utf-8')
    hash = sha1(text).hexdigest()
    data_loaded['resumo_criptografico'] = hash
    save_json(data_loaded)


def save_json(data_request):
    with open('answer.json', 'w') as outfile:  # open the archive 'answer.json' as write. outfile = 'answer.json'
        json.dump(data_request, outfile)  # save data inside outfile. data is the dict and outfile is the archive


def load_json():
    with open('answer.json') as infile:  # open the archive 'answer.json' as read. infile = 'answer.json'
        data_loaded = json.load(infile)  # data = content of archive
    decipher(data_loaded)


if __name__ == '__main__':
    request()
    # load_json()
    post()
