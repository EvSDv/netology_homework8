import requests


def translate_it(path_text, path_result, lang_text, lang_translate = 'ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    with open(path_text, 'r', encoding='utf8') as text_file:
        text = text_file.read()


    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': f'{lang_text}-{lang_translate}',
        'text': text,
    }
    response = requests.get(url, params=params).json()
    with open(path_result, 'w', encoding='utf8') as result_file:
        result_file.write(' '.join(response.get('text', [])))



if __name__ == '__main__':
    translate_it('./DE.txt', './DE_t.txt', 'de')
    translate_it('./ES.txt', './ES_t.txt', 'es')
    translate_it('./FR.txt', './FR_t.txt', 'fr')



