import json


def replace_illegal_characters(string: str) -> str:
    """This function replaces the illegal characters in its input with the "corrected" original version of them.
    Borrowed from code pieces of repo https://github.com/qc5111/BetterQuestingAutoTranslate which is licensed under MIT License.
    Thanks to the original author.
    """

    string = string.replace("搂", "§")  # text 替换 "搂"为§
    string = string.replace("危", "Σ")
    string = string.replace("蟽", "σ")
    string = string.replace("畏", "η")
    string = string.replace("蟺", "π")
    string = string.replace("\n", "\\n")
    return string


def extract_values_from_json(path, mode: str = 'desc:8'):
    result = []

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        data = json.load(f)

    def search_dict(d):
        for key, value in d.items():
            if key == mode:
                result.append(replace_illegal_characters(value))
            elif isinstance(value, dict):
                search_dict(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        search_dict(item)

    search_dict(data)
    return result


def replace_text_with_key(path):
    index = 0
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        data = json.load(f)

    def key_replacing(d, mode):
        nonlocal index
        for key, value in d.items():
            if key == mode:
                d[key] = 'keys.betterquesting.{}.{:06d}'.format(mode[0:-2], index) + '.name'
                print('this is the %d line of %s' % (index, mode))
                index += 1
            elif isinstance(value, dict):
                key_replacing(value, mode)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        key_replacing(item, mode)
        return d

    half_replaced_data = key_replacing(data, 'name:8')

    index = 0 # reset the counter

    result = key_replacing(half_replaced_data, 'desc:8')
    with open('output_quest_json.json', 'w+', encoding='utf-8') as output_quest_json:
        output_quest_json.write(json.dumps(result))
        output_quest_json.close()


def generate_lang_file(values: list, mode: str = 'desc:8') -> str:
    index = 0
    result = []
    for value in values:
        result.append('keys.betterquesting.{}.{:06d}'.format(mode[0:-2], index) + '.name=' + value)
        index += 1
    return '\n'.join(result)


# 使用示例
file_path = r'DefaultQuests.json'
descs = extract_values_from_json(file_path, 'desc:8')
names = extract_values_from_json(file_path, 'name:8')

language_file_content = '#Descs\n\n' + generate_lang_file(descs, 'desc:8') + '\n\n#Names\n\n' + generate_lang_file(
    names, 'name:8')
print('The content of generated language file is shown below.')
print(language_file_content)
with open('xx_xx.lang', 'w', encoding='utf-8') as output:
    output.write(language_file_content)
    output.close()
replace_text_with_key(file_path)
