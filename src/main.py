import json

baseFilePath = "../data/"

def readJSONDataSet():
    dataset = []
    for i in range(2, 68):
        filename = 'output' + str(i) + '.json'
        if filename:
            path = baseFilePath + "raw/" + filename
            with open(path, 'r') as f:
                datastore = json.load(f)
                dataset += datastore
    return dataset


def saveJSONObject(filename, obj):
    # Writing JSON data        
    path = baseFilePath + "raw/" + filename
    with open(path, 'w') as f:
        json.dump(obj, f, indent=4)


def overallSummary(dataset):
    summary = {}
    numrecord = len(dataset)
    print('Number of Dataset: ' + str(numrecord))
    
    summary['title'] = "USDA Food Composition"
    summary['count_data'] = numrecord
    summary['food_groups'] = getFoodGroups(dataset, numrecord)
    print(summary['food_groups'])
    saveJSONObject("overallsummary.json", summary)    


def getFoodGroups(dataset, numrecord):
    foodgrouplist = []
    foodgroupnames = []
    for i in range(0, numrecord):
        food = dataset[i]
        if food['food_group'] in foodgroupnames:
            idx = foodgroupnames.index(food['food_group'])
            foodgrouplist[idx]['count'] += 1
            #foodgrouplist[idx]['food_indexes'].append(i)
        else:
            foodgroup = {}
            foodgroup['name'] = food['food_group']
            foodgroup['count'] = 1
            #foodgroup['food_indexes'] = [i]
            foodgroupnames.append(food['food_group'])
            foodgrouplist.append(foodgroup)
    return foodgrouplist


if __name__ == '__main__':
    # Read Dataset
    dataset = readJSONDataSet()
    # Overall Summary (DONE)
    # overallSummary(dataset) 