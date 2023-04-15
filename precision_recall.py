from sklearn.metrics import confusion_matrix, classification_report

# true class of the test objects   
y_true = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']

# predicted class by the classifier
y_pred = ['A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B']

# calculate the confusion matrix
cm = confusion_matrix(y_true, y_pred)

# print the confusion matrix
print("Confusion matrix:")
print(cm)

# calculate the classification report which includes precision, recall, f1-score and support
cr = classification_report(y_true, y_pred)

# print the classification report
print("Classification report:")
print(cr)
