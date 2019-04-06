import re
import code
from config import *
from itertools import tee
from docx import Document as doc


def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def get_header_indexes(paragraph_list):
    cod_pat = re.compile(MAIN_HEADER)
    header_indexes = []
    for i, p in enumerate(paragraph_list):
        if re.search(cod_pat, p.text):
            header_indexes.append(i)
    return header_indexes

def get_pages(paragraph_list):
    pages = []
    header_indexes = get_header_indexes(d.paragraphs)
    for i_0, i_1 in pairwise(header_indexes):
        pages.append(paragraph_list[i_0:i_1])
    pages.append(paragraph_list[header_indexes[-1]:-1])
    return pages

def format_header(page):
    # orgao nao pegou
    ano, banca, orgao = '', '', ''
    for line in page:
        search_banca = re.search(BANCA_HEADER, line.text)
        search_orgao = re.search(ORGAO_HEADER, line.text)
        search_ano = re.search(ANO_HEADER, line.text)
        if search_banca or search_orgao:
            banca = search_banca.group('banca')
            orgao = search_orgao.group('orgao')
        elif search_ano:
            ano = search_ano.group('ano')
        elif ano and banca and orgao:
            break
    return OUT_MAIN_HEADER.format(ano=ano, banca=banca, orgao=orgao)

def field_filter(page):
    # returns only fields that are supposed to be inaltered
    filtered_page = []
    for line in page:
        delete_paragraphs = [re.search(pat, line.text) for pat in DELETE_HEADERS]
        if not any(delete_paragraphs):
            filtered_page.append(line.text)
    return filtered_page

def output_doc(page_list):
    num_fmt = '{num:02d}. '
    out_pages = []
    for i, page in enumerate(page_list):
        head = format_header(page)
        filtered_page = field_filter(page)
        n = num_fmt.format(num=i+1)
        # 01. (orgao - banca - ano) ← paragraph
        final_header = [n + head]
        # out_page = [parag11, parag21, parag31, ...]
        out_page = final_header + filtered_page
        # out_pages = [[parag11, parag21, parag31, ...], [parag12, parag22, parag32, ...] ...]
        out_pages.append(out_page)
    return out_pages

def save_doc(path, page_list):
    d = doc()
    # first page doesnt need page break
    for paragraph in page_list[0]:
        d.add_paragraph(paragraph)
    for page in page_list[1:]:
        # TODO set page_breaks?
        for paragraph in page:
            d.add_paragraph(paragraph)
    d.save(path)

if __name__ == '__main__':
    d = doc(FILE_INPUT_PATH)
    pages = get_pages(d.paragraphs)
    right_pages = output_doc(pages)
    paf = FILE_INPUT_PATH
    save_doc(paf, right_pages)
    #code.interact(local=locals())
