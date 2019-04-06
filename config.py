FILE_INPUT_PATH = './files/input_test_copy.docx'
MAIN_HEADER = r'Código:'
BANCA_HEADER = ORGAO_HEADER = r'Banca: (?P<banca>.+?) \((?P<orgao>.+?)\)'
ANO_HEADER = r'Ano: (?P<ano>\d{4})'
OUT_MAIN_HEADER = '({orgao} - {banca} - {ano})'
ESTADO_HEADER = 'Estado:'
DISCIPLINA_HEADER = 'Disciplina:'
NIVEL_HEADER = 'Nível: (.+?)'
DICA_HEADER = 'Dica do autor:'
DELETE_HEADERS = [MAIN_HEADER, BANCA_HEADER, ANO_HEADER, ESTADO_HEADER, DISCIPLINA_HEADER, NIVEL_HEADER, DICA_HEADER]
