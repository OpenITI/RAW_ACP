r"""
Convert the transcriptions into mARkdown textfiles and generate yml files.

filename structure:

msnote_auditioncertificate_<shelfmark>_<page_no><r_or_v>.json
-> regex: "msnote_auditioncertificate_(\w+?)_(\d+)([rv])\.json"

data structure of the json files:

```
|- metadata <class 'dict'>
| |- characteristics <class 'dict'>
| | |- copy <class 'list'>
| | |- type <class 'list'>
| |- context <class 'dict'>
| | |- author_name <class 'list'>
| | |- author_viaf <class 'list'>
| | |- work_title <class 'list'>
| |- edit <class 'dict'>
| | |- amended_by <class 'list'>
| | |- editor <class 'list'>
| | |- status <class 'list'>
| |- object <class 'dict'>
| | |- audition_certificate_number <class 'list'>
| | |- catalog <class 'list'>
| | |- classmark <class 'list'>
| | |- folio_number <class 'list'>
| | |- library <class 'list'>
| | |- link_to_manuscript <class 'list'>
| | |- manuscript_link <class 'list'>
|- properties <class 'list'>
| |- attributes <class 'dict'>
| | |- editor <class 'list'>
| | |- link_to_person <class 'list'>
| | |- role <class 'list'>
| |- endIndex <class 'int'>
| |- guid <class 'str'>
| |- startIndex <class 'int'>
| |- text <class 'str'>
| |- type <class 'str'>
|- text <class 'str'>
```

property types, with keys of their attributes dictionaries:
- person: keys in 'attributes' dictionary:
    - editor
    - link_to_person
    - role
- place: keys in 'attributes' dictionary:
    - editor
    - location
- date: keys in 'attributes' dictionary:
    - day
    - editor
    - month
    - year
('editor' is the name of the contributor of the annotation)



ERRORS IN THE DATA:

1. one filename has abbreviation kfcris, other full name:
msnote_auditioncertificate_king_faisal_center_for_research_and_islamic_studies_16275_7v

=============

2. Filenames with errors:

msnote_auditioncertificate_asirefendi_60.json
-> add folio number: msnote_auditioncertificate_asirefendi_60_1r.json
msnote_auditioncertificate_asirefendi_65.json
-> add folio number: msnote_auditioncertificate_asirefendi_65_137r.json
msnote_auditioncertificate_bnf_arabe_687_141_r.json
-> remove underscore before r
msnote_auditioncertificate_bnf_arabe_2091_20_r_n_1.json
-> remove underscore before r
msnote_auditioncertificate_bnf_arabe_2091_20_r_n_2.json
-> remove underscore before r
msnote_auditioncertificate_bnf_suppl_turc_984_189rm_n_1.json
-> remove "m" after "r": msnote_auditioncertificate_bnf_suppl_turc_984_189r_n_1.json
msnote_auditioncertificate_bnf_suppl_turc_986_212_n_1.json
-> add r/v: msnote_auditioncertificate_bnf_suppl_turc_986_212r_n_1.json
msnote_auditioncertificate_bnf_suppl_turc_986_212_n_2.json
-> add r/v: msnote_auditioncertificate_bnf_suppl_turc_986_212r_n_1.json
msnote_auditioncertificate_snl_35r_n_2.json
-> shelfmark missing: msnote_auditioncertificate_snl_3753_2_35r_n_1.json
msnote_auditioncertificate_snl_3748_9_198_n_1.json
-> r missing (see n_2 and n_3) -> msnote_auditioncertificate_snl_3748_9_198r_n_1.json
msnote_auditioncertificate_snl_3757_12_202_n_6.json
-> r missing (see n_1 - n_5): msnote_auditioncertificate_snl_3757_12_202r_n_6.json
msnote_auditioncertificate_snl_3770_4_71.json
-> add r/v
msnote_auditioncertificate_snl_3770_9_126.json
-> add r/v
msnote_auditioncertificate_snl_3771_17_198.json
-> r missing (see json): msnote_auditioncertificate_snl_3771_17_198r.json
msnote_auditioncertificate_king_faisal_center_for_research_and_islamic_studies_16275_7v.json
-> replace full name of library with "kfcris", as in msnote_auditioncertificate_kfcris_16275_7v.json
Escorial mss: filename contains both the full name of the library and the abreviation rbme

=============

3. DUPLICATE FILES:

msnote_auditioncertificate_snl_3755_21_268_n_3.json
= msnote_auditioncertificate_snl_3755_21_268r_n_3.json

=============

4. FILES WITH TRAILING FOLIO NUMBERS IN THE FILENAME:

msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_1
-> msnote_auditioncertificate_stabi_ms_or_oct_3629_109r_n_1.json
msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2
-> msnote_auditioncertificate_stabi_ms_or_oct_3629_109r_n_2.json

==============

5. FILES WITH a/b INSTEAD OF r/v IN THE FILENAME:

msnote_auditioncertificate_bnf_arabe_708_2a_n_1.json
msnote_auditioncertificate_bnf_arabe_708_2a_n_2.json
msnote_auditioncertificate_bnf_arabe_708_2a_n_3.json

===============

6. FILES WITH DIFFERENT FOLIO NUMBER IN THE FILENAME AND JSON:

msnote_auditioncertificate_gotha_ms_orient_a_590_160v.json
folio number from json: '106v'
folio number from filename: '160v'
------------
msnote_auditioncertificate_gotha_ms_orient_a_627_36v_36v.json
folio number from json: '37v'
folio number from filename: '36v'
------------
msnote_auditioncertificate_kfcris_16275_7v.json
folio number from json: '10v'
folio number from filename: '7v'
------------
msnote_auditioncertificate_leiden_university_libraries_or_122_86r_n_1.json
folio number from json: '87r'
folio number from filename: '86r'
------------
msnote_auditioncertificate_leiden_university_libraries_or_122_86r_n_2.json
folio number from json: '87r'
folio number from filename: '86r'
------------
msnote_auditioncertificate_leiden_university_libraries_or_122_86r_n_3.json
folio number from json: '87r'
folio number from filename: '86r'
------------
msnote_auditioncertificate_leiden_university_libraries_or_580_873r.json
folio number from json: '83r'
folio number from filename: '873r'
------------
msnote_auditioncertificate_snl_3761_16_165r.json
folio number from json: '176v'
folio number from filename: '165r'
------------

===============

7. FILES WITH DIFFERENT FOLIO SIDE IN FILENAME AND JSON:

msnote_auditioncertificate_bnf_suppl_turc_983_34r.json
folio number from json: '34v'
folio number from filename: '34r'
------------
msnote_auditioncertificate_bnf_suppl_turc_983_52v_n_6.json
folio number from json: '52r'
folio number from filename: '52v'
------------
msnote_auditioncertificate_stabi_landberg_47_31r_n_1.json
folio number from json: '31v'
folio number from filename: '31r'
------------
msnote_auditioncertificate_stabi_landberg_47_31r_n_2.json
folio number from json: '31v'
folio number from filename: '31r'
------------
msnote_auditioncertificate_stabi_ms_or_oct_3574_78v_n_1.json
folio number from json: '78r'
folio number from filename: '78v'
------------
msnote_auditioncertificate_stabi_ms_or_oct_3574_78v_n_2.json
folio number from json: '78r'
folio number from filename: '78v'
------------
msnote_auditioncertificate_stabi_ms_or_quart_1936_49v_n_1.json
folio number from json: '49r'
folio number from filename: '49v'
------------
msnote_auditioncertificate_stabi_ms_or_quart_1936_49v_n_2.json
folio number from json: '49r'
folio number from filename: '49v'
------------
msnote_auditioncertificate_stabi_sprenger_96b_223r.json
folio number from json: '223v'
folio number from filename: '223r'
------------
msnote_auditioncertificate_stabi_sprenger_96b_56v.json
folio number from json: '56r'
folio number from filename: '56v'
------------
msnote_auditioncertificate_stabi_wetzstein_ii_112_97v.json
folio number from json: '97r'
folio number from filename: '97v'

===============

8. FILES WITH AUDITION CERTIFICATE NUMBER AS FOLIO NUMBER IN JSON:

msnote_auditioncertificate_bnf_arabe_708_2a_n_1.json
folio number from json: 'N. 1'
folio number from filename: '2r'
------------
msnote_auditioncertificate_bnf_arabe_708_2a_n_2.json
folio number from json: 'N. 2'
folio number from filename: '2r'
------------
msnote_auditioncertificate_bnf_arabe_708_2a_n_3.json
folio number from json: 'N. 3'
folio number from filename: '2r'
------------
msnote_auditioncertificate_bnf_arabe_708_2r_n_1.json
folio number from json: 'N. 1'
folio number from filename: '2r'

===============

9. FILES WITH TRAILING WHITESPACE IN LIBRARY NAME IN JSON:

msnote_auditioncertificate_snl_3744_2_15v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3746_1_47r.json 'SNL '
msnote_auditioncertificate_snl_3753_2_19v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3754_1_23r.json 'SNL '
msnote_auditioncertificate_snl_3754_8_50r_n_1.json 'SNL '
msnote_auditioncertificate_stabi_ms_or_quart_1936_31r.json 'Stabi '

=============

10. FILES WITH NOTE NUMBER AS PART OF THE FOLIO NUMBER IN JSON:

msnote_auditioncertificate_bnf_suppl_turc_984_189rm_n_1.json
folio number from json: '189rm N.1'
folio number from filename: '189r'

===============

11. FILES WITH SUPERFLUOUS SPACES IN FOLIONUMBER IN JSON:

msnote_auditioncertificate_bnf_arabe_2091_20_r_n_1.json
folio number from json: '20 r'
folio number from filename: '20r'
------------
msnote_auditioncertificate_bnf_arabe_2091_20_r_n_2.json
folio number from json: '20 r'
folio number from filename: '20r'
------------
msnote_auditioncertificate_bnf_arabe_687_141_r.json
folio number from json: '141 r'
folio number from filename: '141r'
------------
msnote_auditioncertificate_snl_3747_6_93r.json
folio number from json: ' 93r'
folio number from filename: '93r'
------------
msnote_auditioncertificate_snl_3747_6_95r_n_1.json
folio number from json: ' 95r'
folio number from filename: '95r'
------------
msnote_auditioncertificate_snl_3747_6_95v_n_1.json
folio number from json: ' 95v'
folio number from filename: '95v'
------------
msnote_auditioncertificate_snl_3755_23_303r.json
folio number from json: ' 303r'
folio number from filename: '303r'
------------
msnote_auditioncertificate_snl_3755_23_303r_n_2.json
folio number from json: ' 303r'
folio number from filename: '303r'
------------
msnote_auditioncertificate_snl_3757_10_179v.json
folio number from json: ' 179v'
folio number from filename: '179v'
------------
msnote_auditioncertificate_snl_3758_7_203v_n_2.json
folio number from json: ' 203v'
folio number from filename: '203v'
------------
msnote_auditioncertificate_snl_3758_7_232v_n_1.json
folio number from json: ' 232v'
folio number from filename: '232v'
------------
msnote_auditioncertificate_snl_3758_7_232v_n_2.json
folio number from json: ' 232v'
folio number from filename: '232v'
------------
msnote_auditioncertificate_snl_3761_2_14v.json
folio number from json: ' 14v'
folio number from filename: '14v'
------------

12. NOTES ON JSON KEYS:

- "object" dictionary sometimes(?) contains two very similar keys:
manuscript_link and link_to_manuscript
- MISSING KEYS:
2 files don't have "amended_by" key:
  - msnote_auditioncertificate_snl_3766_1_12r.json
  - msnote_auditioncertificate_snl_3766_1_1r.json
2 files don't have "context" key:
  - msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2.json
  - msnote_auditioncertificate_stabi_wetzstein_ii_1712_116r_n_7.json
2 files don't have "catalog" key:
  - msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2.json
  - msnote_auditioncertificate_stabi_wetzstein_ii_1712_116r_n_7.json
3 files don't have "type" key:
  - msnote_auditioncertificate_snl_3759_9_124v_n_2.json
  - msnote_auditioncertificate_snl_3760_2_23r.json
  - msnote_auditioncertificate_snl_3764_13_182r.json
619 files don't have "audition_certificate_number" key: e.g.
  - msnote_auditioncertificate_bnf_arabe_1130_214r.json
  - msnote_auditioncertificate_bnf_arabe_1289_224v.json
  - msnote_auditioncertificate_bnf_arabe_1376_117v.json
  - msnote_auditioncertificate_bnf_arabe_1686_194v.json
  - msnote_auditioncertificate_bnf_arabe_1964_2r.json
2234 files don't have "link_to_manuscript" key: e.g.
  - msnote_auditioncertificate_bnf_arabe_1130_214r.json
  - msnote_auditioncertificate_bnf_arabe_1177_196r_n_1.json
  - msnote_auditioncertificate_bnf_arabe_1177_196r_n_2.json
  - msnote_auditioncertificate_bnf_arabe_1257_139v.json
  - msnote_auditioncertificate_bnf_arabe_1271_178v.json

"""
import csv
import os
import json
import re
from collections import Counter, defaultdict
import textwrap
from openiti.helper.yml import dicToYML, ymlToDic
from openiti.helper.templates import manuscript_yml_template, transcription_yml_template

RELEASE_NO = "5.0"
COLL_ID = f"ACP{int(float(RELEASE_NO))}"  # Audition Certificates Platform, version 5
COLL_URL = "https://doi.org/10.25592/uhhfdm.18150"
COLL_DATE = "2025"
PROJ_DESCR = f"""This document contains transcriptions of the
audition certificates from manuscript %s.
The transcriptions are taken from Konrad Hirschler and
Said al-Joumani's Audition Certificates Platform
(release no. {RELEASE_NO} ({COLL_DATE}),
{COLL_URL}).
The research for this project was funded by the
Deutsche Forschungsgemeinschaft
(DFG, German Research Foundation)
under Germany's Excellence Strategy – EXC 2176
'Understanding Written Artefacts: Material,
Interaction and Transmission in Manuscript Cultures',
project no. 390893796. The research was conducted
within the scope of the Centre for the Study of Manuscript Cultures (CSMC)
at Universität Hamburg."""

# manually generated dictionaries,
# based on the analysis from 0_explore_data.py:
library_URIs = {
    'BNF': 'MS0033ParisBNF',
    'Gotha': 'MS0049GothaFB',
    'Khalidi Library': 'MS0972JerusalemKhalidi',
    'Leiden University Libraries': 'MS0031LeidenUL',
    'Real Biblioteca del Monasterio de El Escorial': 'MS0034Escorial',
    'SNL': 'MS0963DamascusSNL',
    'Stabi': 'MS0049BerlinSBB',
    'Süleymaniye Kütüphanesi': 'MS0090IstanbulSuleymaniye',
    'kfcris': "MS0966RiyadKfcris",
    }

library_fn_URIs = {
    'bnf': 'MS0033ParisBNF',
    'gotha': 'MS0049GothaFB',
    'khalidi_library': 'MS0972JerusalemKhalidi',
    'kfcris': 'MS0966RiyadKfcris',
    'king_faisal_center_for_research_and_islamic_studies': 'MS0966RiyadKfcris',
    'leiden_university_libraries': 'MS0031LeidenUL',
    'real_biblioteca_del_monasterio_de_el_escorial_rbme': 'MS0034Escorial',
    'snl': 'MS0963DamascusSNL',
    'stabi': 'MS0049BerlinSBB',
    'hafidefendi': 'MS0090IstanbulSuleymaniye',
    'asirefendi': 'MS0090IstanbulSuleymaniye'
    }

fixed_filenames = dict()
with open("filenames_to_be_replaced.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        old = row["old_fn"]
        new = row["new_fn"]
        fixed_filenames[old] = new
        
        


def build_ms_uri(lib, classmark):
    try:
        uri = library_fn_URIs[lib.strip()] + "."
    except:
        uri = library_URIs[lib.strip()] + "."
        
    prev_numeric = False
    #print(classmark)
    if not re.findall(r"[^\d_]+", classmark): # purely numeric shelfmark:
        uri += "Ms"
    for part in classmark.split("_"):
        if re.findall(r"^[ivxlc]+$", part.lower()): # Roman number
            uri += part.lower()
            prev_numeric = False
        elif re.findall(r"^[a-z]", part):
            if part == "ms":
                continue
            uri += part.title()
            prev_numeric = False
        elif re.findall(r"^[0-9]", part):
            if prev_numeric:
                uri += "_"+part
            else:
                uri += part
            prev_numeric = True
    return uri

def save_yml(yml_str, uri, outfolder):
    outfp = os.path.join(outfolder, uri+".yml")
    with open(outfp, mode="w", encoding="utf-8") as file:
        file.write(yml_str)

def get_persons(prop_list, person_list):
    for d in prop_list:
        prop_type = d["type"]
        if prop_type != "person":
            continue
        if "text" not in d:
            continue
        name = d["text"]
        if "role" in d["attributes"]:
            for role in d["attributes"]["role"]:
                if role:
                    statement = f"{role.upper()}@{name}"
                    person_list.append(statement)
        

def annotate(text, prop_list):
    """Insert annotations ("properties") into the note text"""
    annotated = ""
    prev_end = 0
    tags = {"person": "@PER", "date": "@DAT", "place": "@TOP"}
    filtered_prop_list = [d for d in prop_list if "startIndex" in d and "endIndex" in d]
    for d in sorted(filtered_prop_list, key=lambda d: d["startIndex"]):
        prop_type = d["type"]
        if prop_type not in tags:
            if prop_type != "signature_of_musmi":
                print("NO TAG DEFINED:", prop_type)
            continue
        #print(d["text"])
        start = d["startIndex"]
        end = d["endIndex"]
        
        prefixes = 0
        if start != 0 and text[start] != " ":
            for i in reversed(range(start)):
                if text[i]== " ":
                    break
                else:
                    prefixes += 1
        n_toks = len(re.findall(r"\w+", d["text"]))
        tag = f"{tags[prop_type]}{prefixes}{n_toks} " 
        
        annotated += text[prev_end:start-prefixes]
        annotated += tag
        annotated += text[start-prefixes:end]
        prev_end = end
    annotated += text[prev_end:]

    # replace page numbers:
    annotated = re.sub("\n[^ء-ي]+", " | ", annotated)
##    print(text)
##    print("------------")
##    print(annotated)
##    print("============")
    return annotated
        
def get_values_as_tuples(fn, keys, source_d, dest_d, dest_key):
    if dest_key not in dest_d:
        dest_d[dest_key] = []
    val_count = []
    for key in keys:
        if key not in source_d:
            missing_keys[key].append(fn)
        val_count.append(len(source_d[key]))
        return
    
    if set(val_count) != 1:
        print("PROBLEM:")
        for i in range(len(keys)):
            print(val_count[i], keys[i])
    else:
        
        for i in range(val_count[0]):
            tup = tuple([source_d[k][i] for k in keys])
            if tup not in dest_d[dest_key]:
                dest_d[dest_key].append(tup)
        

def get_values_from_list(fn, key, source_d, dest_d, dest_key=None):
    if not dest_key:
        dest_key = key
    if key not in source_d:
        #print("Missing key:", key)
        missing_keys[key].append(fn)
        if not dest_key in dest_d:
            dest_d[dest_key] = []
        return
    val_list = source_d[key]
    if val_list:
        if not dest_key in dest_d:
            dest_d[dest_key] = []
        dest_list = dest_d[dest_key]
        for val in val_list:
            if val and val not in dest_d[dest_key]:
                dest_d[dest_key].append(val)

def build_text(ms_uri, transcr_uri, text_d, meta_d):
    
    text = "######OpenITI#\n"
    for k,v in meta_d[ms_uri].items():
        if type(v) == list:
            text += f"\n#META# {k}: {' :: '.join(v)}"
        elif type(v) == str:
            text += f"\n#META# {k}: {v}"
    text += "\n\n#META#Header#End\n\n"
    for d in text_d[ms_uri]:
        text += f"\n# {'\n~~'.join(textwrap.wrap(d['text']))}"
        text += f"\nFolioV01P{d['page']:03d}{d['side']}"
    #print(text)
    #print("===============")

def roman_to_decimal(n):
    """https://bas.codes/posts/python-roman-numerals"""
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

    value = 0
    last_digit_value = 0
    
    for roman_digit in n.upper()[::-1]: # start backwards
        digit_value = value_map[roman_digit]

        if digit_value >= last_digit_value:
            value += digit_value         
            last_digit_value = digit_value
        else:                           
            value -= digit_value

    return value

def page_to_numeric(p):
    try:
        numeric = float(re.findall(r"\d+", p)[0])
    except:
        try:
            if p.strip()[-1] in ["rvab"]:
                numeric = roman_to_decimal(p.strip()[:-1])
            else:
                numeric = roman_to_decimal(p.strip())
        except:
            print("no number found in", p)
            return
    if re.findall("[bvBV]$", p.strip()):
        numeric += 0.5
    return numeric

def pages_to_range(pages):
    numeric_pages = []
    for page in pages:
        page = re.sub(" +", "", page)
        for p in page.split("-"):
            n = page_to_numeric(p)
            if n and n not in numeric_pages:
                numeric_pages.append(n)
    if len(numeric_pages) == 0:
        return ""
    # make sure the last page is processed, too:
    numeric_pages.append(numeric_pages[-1])
    prev_page = 0
    range_start = 0
    page_ranges = []
    for n in numeric_pages:
        if n-prev_page > 0.6 or n-prev_page == 0: # end of range
            if prev_page != 0:
                rs = f"FolioV01P{int(range_start):03d}"
                if range_start.is_integer():
                    rs += "A"
                else:
                    rs += "B"
                pp = f"FolioV01P{int(prev_page):03d}"
                if prev_page.is_integer():
                    pp += "A"
                else:
                    pp += "B"
                if rs == pp:
                    page_ranges.append(rs)
                else:
                    page_ranges.append(f"{rs}-{pp}")
            prev_page = n
            range_start = n
        else:
            prev_page = n
    
    return ",".join(page_ranges)
    
    

def build_ymls(ms_uri, transcr_uri, meta_d, outfolder="converted"):
    ms_yml = ymlToDic(manuscript_yml_template)
    ms_yml["00#MS#URI########:"] = ms_uri
    shelfmark = meta_d[ms_uri]["classmark"][0].title()
    ms_yml["10#MS#SHELFM#####:"] = shelfmark
    author_work_tups = meta_d[ms_uri]["author_work"]
    ms_yml["10#MS#AUTHOR#AR##:"] = "; ".join([t[0] for t in author_work_tups if t[0]])
    ms_yml["10#MS#TITLE#AR###:"] = "; ".join([t[2] for t in author_work_tups if t[2]])
    ms_yml["30#MS#PERSONS####:"] = ", ".join(meta_d[ms_uri]["persons"])
    ms_links = ["IMAGES@"+url for url in meta_d[ms_uri]["manuscript_link"]]
    author_viafs = ["VIAF@"+t[1] for t in author_work_tups if t[1]]
    ms_yml["80#MS#LINKS######:"] = ", ".join(ms_links+author_viafs)
    save_yml(dicToYML(ms_yml), ms_uri, outfolder)

    tr_yml = ymlToDic(transcription_yml_template)
    tr_yml["00#TRNS#URI######:"] = transcr_uri
    pages = meta_d[ms_uri]["transcribed_pages"]
    tr_yml["40#TRNS#PAGES####:"] = pages_to_range(pages)
    tr_yml["80#TRNS#LINMODEL#:"] = "MANUAL"
    tr_yml["80#TRNS#RECMODEL#:"] = "MANUAL"
    tr_yml["80#TRNS#REGMODEL#:"] = "MANUAL"
    editors = ["EDITOR@" + ed for ed in meta_d[ms_uri]["editor"] if ed]
    amenders = ["AMENDER@" + am for am in meta_d[ms_uri]["amended_by"] if am]
    tr_yml["90#TRNS#CONTRIB##:"] = ",".join(editors + amenders)
    lib_shelfmark = f"{shelfmark.strip()} ({meta_d[ms_uri]['library'][0].strip()})"
    tr_yml["90#TRNS#COMMENT##:"] = PROJ_DESCR % lib_shelfmark
    tr_yml["90#TRNS#ISSUES###:"] = "INCOMPLETE_TRANSCRIPTION, AUDITION_CERTIFICATES_ONLY"
    #print(dicToYML(tr_yml))
    save_yml(dicToYML(tr_yml), transcr_uri, outfolder)
    return

def parse_fn(fn, library_fn_regex):
    # use filename fixes if they exist:
    fn = fixed_filenames.get(fn, fn)
    #print(fn)
    # remove prefix and extension:
    fn = fn.replace("msnote_auditioncertificate_", "").replace(".json", "")
    # pop the note number from the end:
    try:
        note_no = re.findall(r"_n_(\d+)$", fn)[0]
        fn = re.sub(r"_n_\d+$", "", fn)
    except:
        note_no = ""
    # get and format the folio number(s) and side(s):
    try:
        pages = re.findall(r"(?:_[IVXLCivxlc\d]+[rv])*(?:_[IVXLCivxlc\d]+[rvab])$", fn)[0]
        #print("pages:", pages)
        fn = re.sub(r"(?:_[IVXLCivxlc\d]+[rv])*(?:_[IVXLCivxlc\d]+[rvab])$", "", fn)
        pages = pages.strip("_")
        # keep only the first page number:
        if "_" in pages:
            page = pages.split("_")[0]
            #print("pages:", pages, "> page:", page)
            #input("CONTINUE?")
        else:
            page = pages
        # split the page from the side letter:
        try:
            side = re.findall(r"[abrvABRV]", page)[0]
            page = re.findall(r"\d+", page)[0]
        except:
            page = page
            side = ""
    except:
        page = ""
        side = ""
            
    # get the library and shelfmark:
    try:
        lib = re.findall(library_fn_regex, fn)[0]
        shelfmark = re.sub(library_fn_regex, "", fn).strip("_")
    except Exception as e:
        print(i, "error:", e, fn)
        fn_errors.append(fn)

    # fix problem in filenames:
    if "efendi" in lib:
        if not re.findall("[a-zA-Z]", shelfmark):
            shelfmark = f"{lib}_{shelfmark}"
        lib = "Süleymaniye Kütüphanesi"
        
    #print([lib, shelfmark, page, side, note_no])
    return lib, shelfmark, page, side, note_no


library_fn_regex = "|".join(library_fn_URIs.keys())
library_fn_regex = "(?:" + library_fn_regex + ")"
#fn_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)_([IVXL\d]+)([rvab]?)(?:_n_)??(\d*?)\.json"
#fn_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)_((?:[IVXL\d]+[rvab]?)+)(?:_n_)??(\d*?)\.json"
fn_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)((?:_[IVXL\d]+[rvab]?)+)\.json"
shelfmark_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)"
missing_keys = defaultdict(list)
lib_to_be_stripped = []
fn_errors = []
tsv = []
text_d = defaultdict(list)
meta_d = dict()
header = "filename\tlibrary\tshelfmark\t"
folder = "json"
i = 1
for fn in os.listdir(folder):
    #print(fn)
    fp = os.path.join(folder, fn)
    if fn.startswith("."):
        continue

    # get the library, shelfmark etc from the filename:
    r = parse_fn(fn, library_fn_regex)
    lib, shelfmark, page, side, note_no = r
##    try:
##        m = re.findall(fn_regex, fixed_filenames.get(fn, fn))[0]
##        #print(fn.replace("msnote_auditioncertificate_", ""))
##        #lib, shelfmark, page, folio, note_no = m
##        lib, shelfmark, page, note_no = m
##        if "_" in page:
##            page = page.split("_")[0]
##        try:
##            folio = re.findall(r"[abrvABRV]", page)[0]
##            page = re.findall(r"\d+", page)[0]
##        except:
##            page = page
##            folio = ""
##            
##        
##    except Exception as e:
##        print(i, "error:", e, fn)
##        fn_errors.append(fn)
##        try:
##            lib, shelfmark = re.findall(shelfmark_regex, fixed_filenames.get(fn, fn))[0]
##            folio = ""
##            note_no = ""
##        except Exception as e:
##            print(i, "error:", e, fn)
##            pass
    
##    # fix problem in filenames:
##    if "efendi" in lib:
##        if not re.findall("[a-zA-Z]", shelfmark):
##            shelfmark = f"{lib}_{shelfmark}"
##        lib = "Süleymaniye Kütüphanesi"

    # build the URI based on the filename:
    uri = build_ms_uri(lib, shelfmark)
    #print(uri)

    # load the json file:
    with open(fp, mode="r", encoding="utf-8-sig") as file:
        data = json.load(file)

    if uri not in meta_d:
        i += 1
        meta_d[uri] = dict()

    # get the note type:
    #meta_d[uri]["note_type"] = ",".join(data["metadata"]["characteristics"]["type"])
    get_values_from_list(fn, "type", data["metadata"]["characteristics"], meta_d[uri])

    if data["metadata"]["characteristics"]["copy"] == True:
        print("COPY:", fn)

    # get book and author metadata:
    if "context" in data["metadata"]:
        #get_values_from_list(fn, "author_name", data["metadata"]["context"], meta_d[uri])
        #get_values_from_list(fn, "author_viaf", data["metadata"]["context"], meta_d[uri])
        #get_values_from_list(fn, "work_title", data["metadata"]["context"], meta_d[uri])
        # if multiple authors and works are mentioned:
        # make sure that the author and title remain connected
        keys = ["author_name", "author_viaf", "work_title"]
        get_values_as_tuples(fn, keys, data["metadata"]["context"], meta_d[uri], "author_work")
    else:
        missing_keys["context"].append(fn)

    # get edition data:
    get_values_from_list(fn, "amended_by", data["metadata"]["edit"],
                         meta_d[uri])
    get_values_from_list(fn, "editor", data["metadata"]["edit"],
                         meta_d[uri])

    # get audition certificate data:
    get_values_from_list(fn, "audition_certificate_number",
                         data["metadata"]["object"], meta_d[uri])
    get_values_from_list(fn, "catalog", data["metadata"]["object"],
                         meta_d[uri])
    get_values_from_list(fn, "classmark", data["metadata"]["object"],
                         meta_d[uri])
    get_values_from_list(fn, "folio_number", data["metadata"]["object"],
                         meta_d[uri], "transcribed_pages")
    get_values_from_list(fn, "library", data["metadata"]["object"],
                         meta_d[uri])
    get_values_from_list(fn, "manuscript_link", data["metadata"]["object"],
                         meta_d[uri])
    get_values_from_list(fn, "link_to_manuscript", data["metadata"]["object"],
                         meta_d[uri], "manuscript_link")

    #
    if not "persons" in meta_d[uri]:
        meta_d[uri]["persons"] = []
    get_persons(data["properties"], meta_d[uri]["persons"])
        
    try:
        folio_from_json = " :: ".join(data["metadata"]["object"]["folio_number"])
    except Exception as e:
        folio_from_json = e
##    if folio_from_json != page+side:
##        print(fn)
##        print("folio number from json:", repr(folio_from_json))
##        print("folio number from filename:", repr(page+side))
##        print("------------")

    try:
        page_no = int(re.findall(r"\d+", page)[0])
    except:
        print(fn)
        print("no page number found:", page)
        page_no = 0
    try:
        side = re.findall("[rvab]", side.lower())[0]
        side = {"r": "A", "v": "B", "a": "A", "b": "B"}[side]
    except:
        print(fn)
        print("no folio side found:", side)
        side = ""
    d = {
        "text": annotate(data["text"], data["properties"]),
        "page": page_no,
        "side": side
        }
    text_d[uri].append(d)

# create text and yml files:
i = 1
for ms_uri in text_d:
    #print(ms_uri)
    transcr_uri = f"{ms_uri}.{COLL_ID}{i:05d}Mar-ara1"
    #print(transcr_uri)
    build_text(ms_uri, transcr_uri, text_d, meta_d)
    build_ymls(ms_uri, transcr_uri, meta_d)

##for uri in meta_d:
##    if len(meta_d[uri]["author_name"]) != len(meta_d[uri]["work_title"]):
##        print(uri)
##        for author in meta_d[uri]["author_name"]:
##            print("  -", author)
##        for work in meta_d[uri]["work_title"]:
##            print("  *", work)
 

print("MISSING KEYS:")

for k,v in missing_keys.items():
    print(len(v), k)
    if len(v) < 5:
        for fn in v:
            print("  -", fn)
    else:
        for i in range(5):
            print("  -", v[i])
