import PyPDF2

# PDFファイルのパス
pdf_file_path = "./wellarchitected-security-pillar.pdf"

# 抽出した行を格納するリスト
output_lines = []

# 指定したキーワード
keywords = ["SEC", "このベストプラクティスが確立されていない場合のリスクレベル"]

# PDFファイルを読み取りモードで開く
with open(pdf_file_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # print(pdf_reader)
    
    # 各ページを処理
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        
        # ページテキストを行ごとに分割
        lines = page_text.split("\n")
        
        # 各行を処理
        for line in lines:
            # 各キーワードで始まるかチェック
            for keyword in keywords:
                if line.strip().startswith(keyword):
                    # 抽出した行をリストに追加
                    output_lines.append(line.strip())

# 抽出した行を表示
# for line in output_lines:
    # print(line)


# 'このベストプラクティスが確立されて'で始まったものとその前のものをだす
filtered_list = []
previous_element = None

for item in output_lines:
    if item.startswith('このベストプラクティスが確立されて'):
        if previous_element is not None:
            filtered_list.append(previous_element)
        filtered_list.append(item)
    previous_element = item

# 結果を表示
# for item in filtered_list:
#     print(item)

# "sec"で始まる要素の空白を削除する
result_list = []
for item in filtered_list:
    if item.startswith('SEC'):
        result_list.append(item[0:9])
    else:
        result_list.append(item)
print(result_list)

# CSVにする
output_csv = "\n".join([f"{result_list[i]} {result_list[i+1]}" for i in range(0, len(result_list), 2)])
print(output_csv)
