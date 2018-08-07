import main
import random
import json

def getCategories():
    path = main.baseFilePath + 'categories.json'
    with open(path, 'r') as f:
        categories = json.load(f)
    return categories

def toChart1(summary):
    categories = getCategories()
    
    series = [{}]
    drilldownseries = []
    series[0]['name'] = summary['title']
    series[0]['colorByPoint'] = True
    series[0]['data'] = []
    foodgroups = summary['food_groups']
    for cat in categories:
        data = {}
        drilldown = {}
        drilldowndatalist = []
        data['name'] = cat['category']
        drilldown['name'] = data['name']
        drilldown['id'] = data['name']

        sum = 0
        subcategories = cat['subcategories']
        for group in foodgroups:
            if group['name'] in subcategories:
                sum += group['count']

        data['y'] = sum/summary['count_data']*100
        data['drilldown'] = data['name']
        series[0]['data'].append(data)

        for group in foodgroups:
            if group['name'] in subcategories:
                presentage = group['count']/sum*100
                drilldowndata = [group['name'], presentage]
                drilldowndatalist.append(drilldowndata)
        drilldown['data'] = drilldowndatalist
        drilldownseries.append(drilldown)

    main.saveJSONObject("chartdata/chart1.json", [series, drilldownseries])

def toChart2(summary, dataset):
    series = []
    food_groups = ['Fruits and Fruit Juices', 'Vegetables and Vegetable Products', 'Beef Products']
    for group in summary['food_groups']:
        if group['name'] in food_groups:
            category = {}        
            category['name'] = group['name']
            indices = group['food_indices']
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            category['color'] = 'rgba(' + str(r) + ', '+ str(g) +', '+ str(b) +', .5)'
            category['data'] = []
            for i in indices:
                nutrientlist = dataset[i]['nutrients']
                x = -1
                y = -1
                for nutrient in nutrientlist:
                    if nutrient['nutrient_name'] == 'Energy':
                        y = nutrient['value']
                    elif nutrient['nutrient_name'] == 'Protein':
                        x = nutrient['value']
                if x != -1 and y != -1:
                    coor = [x, y]
                    category['data'].append(coor)
            series.append(category)
    return series

def toChart3(summary, dataset):
    categories = getCategories()
    
    categdata = []
    subcategdata = []
    nutrientdata = ['Carbohydrate, by difference', 'Protein', 'Total lipid ', 'Sugars, total']
    categnutrientdata = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
    for cat in categories:
        categdata.append(cat['category'])
        subcategdata.append(cat['subcategories'])
    
    numdata = [0, 0, 0, 0, 0, 0]
    for group in summary['food_groups']:
        for i in range(0, len(categdata)):
            if group['name'] in subcategdata[i]:
                numdata[i] += group['count']
    print(numdata)
    
    for food in dataset:
        for i in range(0, len(categdata)):
            if food['food_group'] in subcategdata[i]:
                for nutrient in food['nutrients']:
                    if nutrient['nutrient_name'] in nutrientdata:
                        j = nutrientdata.index(nutrient['nutrient_name'])
                        categnutrientdata[i][j] += nutrient['value']

    print(categnutrientdata)
    for i in range(0, len(categnutrientdata)):
        for j in range(0, len(nutrientdata)):
            categnutrientdata[i][j] = categnutrientdata[i][j]/numdata[i]

    series = []
    for i in range(0, len(nutrientdata)):
        seri = {}
        seri['name'] = nutrientdata[i]
        seri['data'] = []
        for j in range(0, len(categnutrientdata)):
            seri['data'].append(categnutrientdata[j][i])
        series.append(seri)
    
    return [categdata, series]

def getFoodGroupCount(summary, groupname):
    for group in summary['food_groups']:
        if group['name'] == groupname:
            return group['count']

def toChart4(dataset, summary):
    categories = getCategories()
    
    foodwaterlist = main.getWaterStats(dataset, 2395, summary)
    print(foodwaterlist)
    series = [{}]
    drilldownseries = []
    series[0]['name'] = summary['title']
    series[0]['colorByPoint'] = True
    series[0]['data'] = []
    for cat in categories:
        data = {}
        drilldown = {}
        drilldowndatalist = []
        data['name'] = cat['category']
        drilldown['name'] = data['name']
        drilldown['id'] = data['name']

        sum = 0
        count = 0
        subcategories = cat['subcategories']
        for food in foodwaterlist:
            if food['name'] in subcategories:
                sum += food['Water']
                count += getFoodGroupCount(summary, food['name'])
                
                meanvalue = food['Water']/getFoodGroupCount(summary, food['name'])
                drilldowndata = [food['name'], meanvalue]
                drilldowndatalist.append(drilldowndata)

        data['y'] = sum/count
        data['drilldown'] = data['name']
        series[0]['data'].append(data)

        drilldown['data'] = drilldowndatalist
        drilldownseries.append(drilldown)

def chartPerGroup(dataset, summary, idx):
    # half chart
    categories = getCategories()
    subcategories = []
    categories = []
    proximates = ['Carbohydrate, by difference', 'Protein', 'Total lipid ', 'Sugars, total']
    
    for cat in categories:
        categories.append(cat['category'])
        subcategories.append(cat['subcategories'])
    indices = summary['food_groups'][idx]['food_indices']
    #for i in indices:

def toChart5(dataset, summary):
    #count cholesterol, fat rate, per category
    categlist = ['Fast Foods', 'Beef Products', 'Vegetables and Vegetable Products', 'Restaurant Foods', 'Cereal Grains and Pasta']
    nutrientlist = ['Fatty acids, total saturated', 'Cholesterol', 'Fiber, total dietary']
    nutrientrate = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    numdata = [0, 0, 0, 0, 0]
    for group in summary['food_groups']:
        if group['name'] in categlist:
            idx = categlist.index(group['name'])
            numdata[idx] = group['count']
            
    print(numdata)
    for group in summary['food_groups']:
        if group['name'] in categlist:
            i = categlist.index(group['name'])
            indices = group['food_indices']
            for k in indices:
                food = dataset[k]
                for nutrient in nutrientlist:
                    sum, j = getNutrientValue(food, nutrient, nutrientlist)
                    if (j != -1):
                        nutrientrate[i][j] += sum
    print(nutrientrate)
    for i in range(0, len(nutrientrate)):
        for j in range(0, len(nutrientlist)):
            nutrientrate[i][j] = nutrientrate[i][j]/numdata[i]
    series = []
    for i in range(0, len(nutrientlist)):
        seri = {}
        seri['name'] = nutrientlist[i]
        seri['data'] = []
        for j in range(0, len(nutrientrate)):
            seri['data'].append(nutrientrate[j][i])
        series.append(seri)
    
    return [categlist, series]


def getNutrientValue(food, nutrientdata, nutrientlist):
    for nutrient in food['nutrients']:
        l = len(nutrientdata)
        if nutrient['nutrient_name'][:l] == nutrientdata:
            return nutrient['value'], nutrientlist.index(nutrient['nutrient_name'])
    return 0, -1

if __name__ == '__main__':
    # Read Dataset
    dataset = main.readJSONDataSet()
    # Overall Summary (DONE)
    summary = main.overallSummary(dataset)
    # toChart1(summary)
    #series = toChart2(summary, dataset)
    #main.saveJSONObject("chartdata/chart2.json", series)
    #obj = toChart3(summary, dataset)
    #obj = toChart5(dataset, summary)
    #main.saveJSONObject("chartdata/chart5.json", obj)

    