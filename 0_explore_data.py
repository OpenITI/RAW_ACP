r"""
data structure:

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

filename structure:
msnote_auditioncertificate_<shelfmark>_<page_no><r_or_v>.json
-> regex: "msnote_auditioncertificate_(\w+?)_(\d+)_([rv])\.json"



NB: errors in the data:

one filename has abbreviation kfcris, other full name:
msnote_auditioncertificate_king_faisal_center_for_research_and_islamic_studies_16275_7v

=============
Filenames with errors:
msnote_auditioncertificate_asirefendi_60.json
-> add folio number: msnote_auditioncertificate_asirefendi_60_1r.json
msnote_auditioncertificate_asirefendi_65.json
-> add folio number: msnote_auditioncertificate_asirefendi_65_137r.json
msnote_auditioncertificate_bnf_arabe_687_141_r.json
-> remove underscore before r
msnote_auditioncertificate_king_faisal_center_for_research_and_islamic_studies_16275_7v.json
-> replace full name of library with "kfcris", as in msnote_auditioncertificate_kfcris_16275_7v.json
Escorial mss: filename contains both the full name of the library and the abreviation rbme
=============
files with trailing whitespace in library name:
msnote_auditioncertificate_snl_3744_2_15v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3746_1_47r.json 'SNL '
msnote_auditioncertificate_snl_3753_2_19v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3754_1_23r.json 'SNL '
msnote_auditioncertificate_snl_3754_8_50r_n_1.json 'SNL '
msnote_auditioncertificate_stabi_ms_or_quart_1936_31r.json 'Stabi '

"object" dictionary sometimes(?) contains two very similar keys:
manuscript_link and link_to_manuscript


"""

import os
import json
import re
from collections import Counter

struct_d = dict()
prop_d = dict()
all_libraries = Counter()
lib_to_be_stripped = []
fn_errors = []

library_URIs = {
    'BNF': 'MS0033ParisBNF',
    'Gotha': 'MS0049Gotha',
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
    'gotha': 'MS0049Gotha',
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
library_fn_regex = "|".join(library_fn_URIs.keys())
library_fn_regex = "(?:" + library_fn_regex + ")"
print(library_fn_regex)

def walk(d, level):
    """Print the structure of a dictionary"""
    for k in d:
        print("| "*(level)+"|-", k, type(d[k]))
        sk = f"{level}-{k}"
        if sk not in struct_d:
            struct_d[sk] = {"type": type(d[k])}

        if k == "properties":
            for pd in d[k]:
                if pd["type"] not in prop_d:
                    prop_d[pd["type"]] = {"attributes": []}
                for ak in pd["attributes"]:
                    if ak not in prop_d[pd["type"]]["attributes"]:
                        prop_d[pd["type"]]["attributes"].append(ak)
            
        if type(d[k]) == dict:
            walk(d[k], level+1)

        elif type(d[k]) == list:
            if len(d[k]) > 0:
                if type(d[k][0]) == dict:
                    walk(d[k][0], level+1)

    

#fn_regex = r"msnote_auditioncertificate_(\w+?)_(\d+)(_?[rv]?)(?:_n_)?(\d*)\.json"
#fn_regex = r"msnote_auditioncertificate_([a-zA-Z]+)_(\w+?)_([IVXL\d]+)([rv]?)(?:_n_)?(\d*)\.json"
fn_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)_([IVXL\d]+)([rv]?)(?:_n_)?(\d*)\.json"
shelfmark_regex = rf"msnote_auditioncertificate_({library_fn_regex})_(\w+?)"
open_files = False

folder = "msnotesannotator_audition_certificates_data-master"
i = 0
for fn in os.listdir(folder):
    #print(fn)
    fp = os.path.join(folder, fn)
    if fn.startswith("."):
        continue

    # check for filenames that don't match the fn_regex:
    try:
        m = re.findall(fn_regex, fn)[0]
        #print(fn.replace("msnote_auditioncertificate_", ""))
        lib, shelfmark, page, folio, note_no = m
        all_libraries[lib.strip()] += 1
    except Exception as e:
        #print(i, "error:", e, fn)
        fn_errors.append(fn)
    
            

    if open_files or i == 0:
        with open(fp, mode="r", encoding="utf-8-sig") as file:
                data = json.load(file)

        # print the data structure (of the first file only):
        if i == 0:
            # walk the json:
            walk(data, 0)
    i += 1
    if open_files:
        # collect a set of all libraries in the collection:
        try:
            for lib in data["metadata"]["object"]["library"]:
                all_libraries[lib.strip()] += 1
                if lib != lib.strip():
                    lib_to_be_stripped.append((fn, lib))
                if lib.strip().replace(" ", "_").lower() not in fn.lower():
                    print(lib, "not in filename", fn)
        except Exception as e:
            print(i, e)
            print("no library found:")
            print(json.dumps(data, indent=2))

        

print("=============")
#print(json.dumps(prop_d, indent=2))
print("property types, with keys of their attributes dictionaries:")
for type_ in prop_d:
    print(f"- {type_}: keys in 'attributes' dictionary:")
    for k in prop_d[type_]["attributes"]:
        print("    -", k)
print("('editor' is the name of the contributor of the annotation)")

print("=============")
print("all libraries:")
for lib, count in sorted(all_libraries.items()):
    print(count, repr(lib))


if fn_errors:
    print("=============")
    print("Filenames with errors:")
    for fn in fn_errors:
        print(fn)

if lib_to_be_stripped:
    print("=============")
    print("files with trailing whitespace in library name:")
    for fn, lib in lib_to_be_stripped:
        print(fn, repr(lib))
