from pybiomart import Server
import json

# Ensembl Biomart 서버에 연결
server = Server(host='http://www.ensembl.org')

# 데이터셋 목록 확인
datasets = server.list_marts()

server = Server(host='http://www.ensembl.org')
print(server.list_marts())
genome_mart_name = 'ENSEMBL_MART_SEQUENCE'
mart = server[genome_mart_name]
available_datasets = mart.list_datasets()

# convert available_datasets to a json file
result = {}
result[genome_mart_name] = {
    "display_name": server[genome_mart_name].display_name,
    "database_name": server[genome_mart_name].database_name,
    "datasets": available_datasets.set_index('name')['display_name'].to_dict()
}

# JSON 형태로 변환
json_data = json.dumps(result, ensure_ascii=False, indent=2)

# JSON 파일로 저장
with open('mart_datasets.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

# # 원하는 데이터셋 선택 (예: 인간 유전자)
# dataset = server.datasets['hsapiens_gene_ensembl']

# # 데이터셋의 필터와 속성 확인
# filters = dataset.list_filters()
# attributes = dataset.list_attributes()

# print("Filters:", filters)
# print("Attributes:", attributes)

# # 쿼리 실행
# results = dataset.query(attributes=['ensembl_gene_id', 'external_gene_name', 'chromosome_name'],
#                         filters={'chromosome_name': ['1', '2', '3']})

# # 결과 출력
# print(results)