import requests


def term_extraction(text, out, type):
    denotations = out['denotations']
    relavent_terms = []

    if type == 'drug':
        drug_terms = []
        for i in denotations:
            if i['obj'] == 'drug':
                drug_terms.append((i['span']['begin'], i['span']['end']))

        for i in drug_terms:
            start = i[0]
            end = i[1]
            relavent_terms.append(text[start:end])
    return (relavent_terms)


def query_raw(text, url="https://bern.korea.ac.kr/plain"):
  return requests.post(url, data={'sample_text': text}).json()


def druglist(text):
    out = query_raw(text)
    dname = term_extraction(text, out, 'drug')
    return dname
