import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

# read in our previous scores
if __name__ == "__main__":
    old_scores = js_r('current_scores.json')
# write to a new json file, "old_scores"
writeToJSONFile('','old_scores',old_scores)
