# Audition Certificates Platform transcriptions

This folder contains transcriptions of audition certificates 
by the Hamburg team led by Konrad Hirschler and Said Aljoumani.

website: https://www.audition-certificates-platform.org/versions

latest data release (Dec. 2025): https://www.fdr.uni-hamburg.de/record/18150

## Folder structure

```
|- json/ : json data downloaded from https://www.fdr.uni-hamburg.de/record/18150
|- converted/ : text and yml files
|- 0_explore_data.py : first exploration of the json and filename structure 
|- 1_convert.py : converts the json files to text and yml files
|- filenames_to_be_replaced.csv : proposed corrections for filenames
|- platform : link to the Audition Certificates Platform
|- README.md : this file
```

## Filename structure

with a few exceptions (see below), the file names look like this:

`msnote_auditioncertificate_<library>_<shelfmark>_<page_no><r_or_v>.json`

NB: if the certificate spans two pages, the `_<page_no><r_or_v>` 
part of the filename is reduplicated

## Data structure of the json files:

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

### property types (d.properties.type), with keys of their attributes dictionaries:
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

NB: 'editor' is the name of the contributor of the annotation

## DATA ISSUES

### 1. INCONSISTENCY IN LIBRARY NAMES:

one filename has abbreviation kfcris, the other the full name:
msnote_auditioncertificate_king_faisal_center_for_research_and_islamic_studies_16275_7v

=============

### 2. FILENAMES WITH ERRORS:

```
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
```

=============

### 3. DUPLICATE FILES:

```
msnote_auditioncertificate_snl_3755_21_268_n_3.json
= msnote_auditioncertificate_snl_3755_21_268r_n_3.json
```

=============

### 4. FILES WITH TRAILING FOLIO NUMBERS IN THE FILENAME:

```
msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_1
-> msnote_auditioncertificate_stabi_ms_or_oct_3629_109r_n_1.json
msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2
-> msnote_auditioncertificate_stabi_ms_or_oct_3629_109r_n_2.json
```

==============

### 5. FILES WITH a/b INSTEAD OF r/v IN THE FILENAME:

```
msnote_auditioncertificate_bnf_arabe_708_2a_n_1.json
msnote_auditioncertificate_bnf_arabe_708_2a_n_2.json
msnote_auditioncertificate_bnf_arabe_708_2a_n_3.json
```

===============

### 6. FILES WITH DIFFERENT FOLIO NUMBER IN THE FILENAME AND JSON:

```
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
```

===============

### 7. FILES WITH DIFFERENT FOLIO SIDE IN FILENAME AND JSON:

```
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
```

===============

### 8. FILES WITH AUDITION CERTIFICATE NUMBER AS FOLIO NUMBER IN JSON:

```
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
```

===============

### 9. FILES WITH TRAILING WHITESPACE IN LIBRARY NAME IN JSON:

```
msnote_auditioncertificate_snl_3744_2_15v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3746_1_47r.json 'SNL '
msnote_auditioncertificate_snl_3753_2_19v_n_3.json 'SNL '
msnote_auditioncertificate_snl_3754_1_23r.json 'SNL '
msnote_auditioncertificate_snl_3754_8_50r_n_1.json 'SNL '
msnote_auditioncertificate_stabi_ms_or_quart_1936_31r.json 'Stabi '
```

=============

### 10. FILES WITH NOTE NUMBER AS PART OF THE FOLIO NUMBER IN JSON:

```
msnote_auditioncertificate_bnf_suppl_turc_984_189rm_n_1.json
folio number from json: '189rm N.1'
folio number from filename: '189r'
```

===============

### 11. FILES WITH SUPERFLUOUS SPACES IN FOLIONUMBER IN JSON:

```
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
```

### 12. NOTES ON JSON KEYS:

- "object" dictionary sometimes(?) contains two very similar keys:
"manuscript_link" and "link_to_manuscript"
- MISSING KEYS:
  -  2 files don't have "amended_by" key:
    - msnote_auditioncertificate_snl_3766_1_12r.json
    - msnote_auditioncertificate_snl_3766_1_1r.json
  - 2 files don't have "context" key:
    - msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2.json
    - msnote_auditioncertificate_stabi_wetzstein_ii_1712_116r_n_7.json
  - 2 files don't have "catalog" key:
    - msnote_auditioncertificate_stabi_ms_or_oct_3629_r_n_2.json
    - msnote_auditioncertificate_stabi_wetzstein_ii_1712_116r_n_7.json
  - 3 files don't have "type" key:
    - msnote_auditioncertificate_snl_3759_9_124v_n_2.json
    - msnote_auditioncertificate_snl_3760_2_23r.json
    - msnote_auditioncertificate_snl_3764_13_182r.json
  - 619 files don't have "audition_certificate_number" key: e.g.
    - msnote_auditioncertificate_bnf_arabe_1130_214r.json
    - msnote_auditioncertificate_bnf_arabe_1289_224v.json
    - msnote_auditioncertificate_bnf_arabe_1376_117v.json
    - msnote_auditioncertificate_bnf_arabe_1686_194v.json
    - msnote_auditioncertificate_bnf_arabe_1964_2r.json
  - 2234 files don't have "link_to_manuscript" key: e.g.
    - msnote_auditioncertificate_bnf_arabe_1130_214r.json
    - msnote_auditioncertificate_bnf_arabe_1177_196r_n_1.json
    - msnote_auditioncertificate_bnf_arabe_1177_196r_n_2.json
    - msnote_auditioncertificate_bnf_arabe_1257_139v.json
    - msnote_auditioncertificate_bnf_arabe_1271_178v.json


