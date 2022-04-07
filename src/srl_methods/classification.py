from allennlp_models import pretrained
allenslr=pretrained.load_predictor('structured-prediction-srl-bert')
def sepparate(text,j):
    SP=''
    O=''
    tags=text['verbs'][j]['tags']
    words=text['words']
    for i in range(len(tags)):
        if any('ARG0' in string for string in text['verbs'][j]['tags']):
            if 'ARG0' in tags[i]:
                SP=SP+words[i]+' '
            elif 'ARG1' in tags[i]:
                O=O+words[i]+' '
            elif 'ARGM' in tags[i]:
                SP=SP+words[i]+' '
            elif 'V' in tags[i]:
                SP=SP+words[i]+' '
            elif 'ARG2' in tags[i]:
                O=O+words[i]+' '
        else:
            if 'ARG1' in tags[i]:
                SP=SP+words[i]+' '
            elif 'ARG2' in tags[i]:
                O=O+words[i]+' '
            elif 'ARGM' in tags[i]:
                SP=SP+words[i]+' '
            elif 'V' in tags[i]:
                SP=SP+words[i]+' '
    return [SP,O]
def extract(sentence):
    output=allenslr.predict(sentence)
    if len(output['verbs'])>1:
        for i in range(len(output['verbs'])):
            O='O' in output['verbs'][i]['tags']
            ARG0=any('ARG0' in string for string in output['verbs'][i]['tags'])
            ARG1=any('ARG1' in string for string in output['verbs'][i]['tags'])
            ARG2=any('ARG2' in string for string in output['verbs'][i]['tags'])
            if not O:
                if (ARG0 & ARG1) or (ARG1 & ARG2):
                    break
        output=sepparate(output,i)
    else:
        output=sepparate(output,0)
    return output
