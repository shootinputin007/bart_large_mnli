import json
from transformers import pipeline

# Load the classifier
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

# Load the tx data to be classified
with open('swap.json', 'r') as file:
    sim_data = json.load(file)

# Potential labels
candidate_labels = ['swap','withdraw','borrow','deposit','supply']

# Trim the data to keep only function names
def explore_json(obj, functions):
    try:
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'function':
                    functions.append(value)
                explore_json(value, functions)
        elif isinstance(obj, list):
            for item in obj:
                explore_json(item, functions)
        else:
            pass
    
    except Exception as e:
        print("explore_json error: ", e)

def extract(json_obj):
    try:
        functions = []
        explore_json(json_obj, functions)
        #functions = set(functions)
        return functions
    
    except Exception as e:
        print("extract_amounts error: ", e)

sim_data_functions = extract(sim_data)

# Transform into a string to be given to the model
sequence_to_classify = ' '.join(sim_data_functions)

# Apply the classifier
results = classifier(sequence_to_classify, candidate_labels, multi_label=True)
sequence = results['sequence']
labels = results['labels']
scores = results['scores']

print("Sequence:", sequence)
print("Labels:", labels)
print("Scores:", scores)
