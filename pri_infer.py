from util.text_io import read_text, write_text
from util.token import count_token


def pri_infer(info_prompt, isAPI=True):
    separater = '-'*16
    return '\n'.join([
        info_prompt,
        separater,
        '今回インストールするパッケージの圧縮ファイルから読み取ったメタデータです。',
        read_text('workspace/metadata.yaml'),
        separater,
        read_text('pri_infer.txt'),
        'ここまでの情報からjson文字列を生成、validate_by_json_schemaにより検証してください。' if isAPI else 'ここまでの情報からjsonファイルを生成しjson schemaであるschema.jsonによりエラーを出力して検証を行ってください。エラーのある場合はリトライしてください。その後、完成したjsonファイルのダウンロードリンクを提供してください。もし、json.dump()を使用する場合は ensure_ascii=Falseを指定してください。'])


if __name__ == '__main__':
    prompt = pri_infer(read_text('workspace/gpt3_output.txt'), False)
    write_text('workspace/gpt4_input.txt', prompt)
    print(count_token(prompt))
