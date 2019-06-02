import requests
import json
import hashlib


# def request():
#     try:
#         url = requests.get(
#             'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=1d0408fc4d2159e2b0446a0f4c3f0c525145ef69'
#         )
#         data_request = url.json()  # stores the response. data_request = dict
#         decipher(data_request)
#     except:
#         print('Não foi possível obter resposta da url especificada.'
#               '\nVerique sua conexão com a Internet!')


def post():
    with open('answer.json', 'rb') as f:
        headers = {'Content-Type': 'multipart/form-data'}
        url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=1d0408fc4d2159e2b0446a0f4c3f0c525145ef69'
        r = requests.post(url, files={'answer': f}, headers=headers)
    print(r.status_code)
    print(r.json())


# def decipher(data_loaded):
#     text_encrypted = data_loaded['cifrado'].lower()
#     text_deciphered = ''
#     number_jump = data_loaded['numero_casas']
#     especial_caract = '´’,.+-*//?°:;<>,.~^]}º[{ª´`+=§_-)(*&¨%$#@!¬¢£³²¹"\'\\'
#     alphabet = {1: 'aáàâãä', 2: 'b', 3: 'c', 4: 'd', 5: 'eéèêë', 6: 'f', 7: 'g', 8: 'h', 9: 'iííîï', 10: 'j',
#                 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'oóòôõö', 16: 'p', 17: 'q', 18: 'r', 19: 's',
#                 20: 't', 21: 'uúùûü', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
#
#     for letter in text_encrypted:
#         for key, value in alphabet.items():
#             if letter in value:
#                 position_letter = key
#                 new_letter = (position_letter + number_jump) % len(alphabet) if (position_letter + number_jump) % len(alphabet) != 0 \
#                     else (position_letter + number_jump)
#                 text_deciphered += alphabet[new_letter][0]
#                 break
#             elif letter in especial_caract or letter.isspace() or letter.isdigit():
#                 text_deciphered += letter
#                 break
#
#     data_loaded['decifrado'] = text_deciphered
#     string_hash(data_loaded)
#     return data_loaded['decifrado']

# def decipher(data_loaded):
#     text_encrypted = data_loaded['cifrado'].lower()
#     text_deciphered = ''
#     number_jump = data_loaded['numero_casas']
#     especial_caract = '´’,.+-*//?°:;<>,.~^]}º[{ª´`+=§_-)(*&¨%$#@!¬¢£³²¹"\'\\'
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#     for letter in text_encrypted:
#         if letter in especial_caract or letter.isspace() or letter.isdigit():
#             text_deciphered += letter
#         else:
#             position_letter = alphabet.index(letter)+1
#             new_letter = (position_letter + number_jump) % len(alphabet) if (position_letter + number_jump) % len(alphabet) != 0 \
#                 else (position_letter + number_jump)
#             text_deciphered += alphabet[new_letter-1]
#
#     data_loaded['decifrado'] = text_deciphered
#     string_hash(data_loaded)
#     return data_loaded['decifrado']


# def string_hash(data_loaded):
#     text = bytes(data_loaded['decifrado'], 'UTF-8')
#     hash = hashlib.new("sha1", text).hexdigest()
#     data_loaded['resumo_criptografico'] = hash
#     save_json(data_loaded)


# def save_json(data_request):
#     with open('answer.json', 'w') as outfile:  # open the archive 'answer.json' as write. outfile = 'answer.json'
#         json.dump(data_request, outfile)  # save data inside outfile. data is the dict and outfile is the archive
#
#
# def load_json():
#     with open('answer.json') as infile:  # open the archive 'answer.json' as read. infile = 'answer.json'
#         data_loaded = json.load(infile)  # data = content of archive


if __name__ == '__main__':
    # request()
    # load_json()
    post()
