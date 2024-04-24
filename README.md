# Using bart_large_mnli to label transaction types

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

### Ideas:
* By parsing the data differently, we could assess different things about the transaction more easily
    * For example, I parsed function names to determine the type of transaction
    * By parsing all the values, we could classify if the Tenderly object has too many similar values, which is a probable cause of some of the hallucinations
