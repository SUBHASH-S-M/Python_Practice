def calculateOutputValues(hospitalized):
    re=[]
    re.append(max(hospitalized))
    re.append(min(hospitalized))
    hospitalized.sort(reverse=True)
    re.append(sum(hospitalized[:3]))
    hospitalized.sort()
    re.append(sum(hospitalized[:3]))
    return re




   