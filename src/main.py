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
    path = baseFilePath + filename
    with open(path, 'w') as f:
        json.dump(obj, f, indent=4)


def overallSummary(dataset):
    summary = {}
    numrecord = len(dataset)
    print('Number of Dataset: ' + str(numrecord))
    
    summary['title'] = "USDA Food Composition"
    summary['count_data'] = numrecord
    summary['food_groups'] = getFoodGroups(dataset, numrecord)
    #print(summary['food_groups'])
    return summary

def getFoodGroups(dataset, numrecord):
    foodgrouplist = []
    foodgroupnames = []
    for i in range(0, numrecord):
        food = dataset[i]
        if food['food_group'] in foodgroupnames:
            idx = foodgroupnames.index(food['food_group'])
            foodgrouplist[idx]['count'] += 1
            foodgrouplist[idx]['food_indices'].append(i)
        else:
            foodgroup = {}
            foodgroup['name'] = food['food_group']
            foodgroup['count'] = 1
            foodgroup['food_indices'] = [i]
            foodgroupnames.append(food['food_group'])
            foodgrouplist.append(foodgroup)
    return foodgrouplist

def getWaterStats(dataset, numrecord, summary):
    foodgrouplist = []
    foodgroupnames = []
    for i in range(0, numrecord):
        food = dataset[i]
        if food['food_group'] in foodgroupnames:
            idx = foodgroupnames.index(food['food_group'])
            nutrientlist = food['nutrients']
            water = 0
            for nutrient in nutrientlist:
                if nutrient['nutrient_name'] == 'Water':
                    water = nutrient['value']
            foodgrouplist[idx]['Water'] += water
        else:
            foodgroup = {}
            foodgroup['name'] = food['food_group']
            nutrientlist = food['nutrients']
            water = 0
            for nutrient in nutrientlist:
                if nutrient['nutrient_name'] == 'Water':
                    water = nutrient['value']
            foodgroup['Water'] = water
            foodgroupnames.append(food['food_group'])
            foodgrouplist.append(foodgroup)

    return foodgrouplist


if __name__ == '__main__':
    # Read Dataset
    dataset = readJSONDataSet()
    # Overall Summary (DONE)
    #summary = overallSummary(dataset) 
    #sorteddata = sorted(dataset, key=lambda k: k['nutrients'][1].get('value', 0))
    #saveJSONObject("overallsummary.json", summary)  
    #print(getWaterStats(dataset, 2395, summary))