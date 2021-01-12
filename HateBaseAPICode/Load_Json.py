import csv
import json
setProbability = 60
years = list(range(2015, 2021))
hateTypes = ["classOnly", "disabilityOnly", "ethnicityOnly",
             "genderOnly", "nationalityOnly", "religionOnly", "sexualOnly"]
for hateType in hateTypes:
    hateTypeTermDict = {}
    for year in years:
        print("working on ", hateType, year)
        # read file
        with open(hateType+'\\'+hateType+str(year)+'.txt', 'r') as f:
            data = json.load(f)
            f.close()
        # write term, count to dict
        termDict = {}
        for i in range(len(data['result'])):
            term = data['result'][i]['term']
            probability = data['result'][i]['probability']
            if probability is not None and probability >= setProbability:
                if not termDict.get(term):
                    termDict[term] = 1
                else:
                    termDict[term] += 1
                if not hateTypeTermDict.get(term):
                    hateTypeTermDict[term] = 1
                else:
                    hateTypeTermDict[term] += 1
        # print(termDict)
        # write dict to csv file
        with open(hateType+'\\'+hateType+str(year)+'output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Term", "Count"])
            totalCount = 0
            # use key's letter to sort
            # for term in sorted(termDict):
            # use count to sort
            for term in sorted(termDict, key=termDict.get, reverse=True):
                writer.writerow([term, termDict[term]])
                totalCount += termDict[term]
            csvfile.close()

        #  check Dict counts are match to the records
        if totalCount != len(data['result']):
            print(hateType+str(year)+"'s Dict Count = ", totalCount,
                  "len of result = ", len(data['result']), ", " + str(len(data['result']) - totalCount) + " terms probability <= ", setProbability)
    # write hate type dict to csv file
    with open(hateType+'2015-2020_output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Term", "Count"])
        # use key's letter to sort
        # for term in sorted(hateTypeTermDict):
        # use count to sort
        for term in sorted(hateTypeTermDict, key=hateTypeTermDict.get, reverse=True):
            writer.writerow([term, hateTypeTermDict[term]])
        csvfile.close()
