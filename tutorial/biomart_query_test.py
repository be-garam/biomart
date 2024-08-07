import json
from pybiomart import Dataset

with open('mart_datasets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

human_dataset_name = data['ENSEMBL_MART_ENSEMBL']['datasets']['hsapiens_gene_ensembl']
human_dataset = Dataset(name="hsapiens_gene_ensembl", host='http://www.ensembl.org')

# 데이터셋의 필터와 속성 확인
human_dataset.list_attributes().to_csv('dataset_attributes.csv', index=False)
print("Attributes saved to 'dataset_attributes.csv'")

# result = human_dataset.query(attributes=['ensembl_gene_id', 'external_gene_name', 'chromosome_name'],
#                        filters={'chromosome_name': ['1', '2', '3']})

# # 결과를 로컬 파일로 저장
# result.to_csv('hsapiens_genes.csv', index=False)
# print("Saved to 'hsapiens_genes.csv'")