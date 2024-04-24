# Using bart_large_mnli to label transaction types

Model: https://huggingface.co/facebook/bart-large-mnli

### Purpose
Labeling specific types of transactions before sending them to the model can be useful for a few things:
* Different types of transactions could require different system prompts for optimal explanation; providing labels before running the model would allow for dynamic changing of system prompts
* Large transactions, as well as transactions with multiple similar values for different assets, sometimes hallucinate and require a better model to get the decimals and amounts right; if we can label them beforehand, we can upgrade the model immediately

### Flow
* Import the classifier from huggingface
* Import a Tenderly json object for a transaction
* Provide a list of candidate labels
* Parse the names of functions used in the transaction
* Transform them into a string and give them to the classifier
* The classifier returns:
    * 1) the string that was processed,
    * 2) a list of labels sorted from the most probable one to the least probable one, and
    * 3) a list of probabilities for each label

### Issues:
* Bannanagun overrepresented in training data-> every swap is detected as a bannanagun swap

### Ideas:
* By parsing the data differently, we could assess different things about the transaction more easily
    * For example, I parsed function names to determine the type of transaction
    * By parsing all the values, we could classify if the Tenderly object has too many similar values, which is a probable cause of some of the hallucinations
 
### To do:
* Think more about the different ways of classifying we want to do (example: swap VS withdrawal VS ETH transfer; simple tx VS complex tx VS tx with repetitive values; etc)
* Create a comprehensive list (or lists) of adequate labels for different types of classificaltion we may want to do
* More in-depth testing of the successfulness of classification for different transaction types
