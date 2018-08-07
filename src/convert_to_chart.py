import main
import random
import json

def toChart1(summary):
    path = main.baseFilePath + 'categories.json'
    with open(path, 'r') as f:
        categories = json.load(f)
    
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

def toChart3(dataset):
    path = main.baseFilePath + 'categories.json'
    with open(path, 'r') as f:
        categories = json.load(f)
    
    categdata = []
    nutrientdata = ['Carbohydrate, by difference', 'Protein', 'Total lipid (fat)', 'Sugars']
    for cat in categories:
        categdata.append(cat['category'])
    
    for food in dataset:
        if food['food_group']


def getFoodGroupCount(summary, groupname):
    for group in summary['food_groups']:
        if group['name'] == groupname:
            return group['count']

def toChart4(dataset, summary):
    path = main.baseFilePath + 'categories.json'
    with open(path, 'r') as f:
        categories = json.load(f)
    
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

    main.saveJSONObject("chartdata/chart4.json", [series, drilldownseries])

if __name__ == '__main__':
    # Read Dataset
    dataset = main.readJSONDataSet()
    # Overall Summary (DONE)
    summary = main.overallSummary(dataset)
    # toChart1(summary)
    #series = toChart2(summary, dataset)
    #main.saveJSONObject("chartdata/chart2.json", series)
    toChart4(dataset, summary)

    