from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

def clf_eval(gt, pred):
    confusion   = confusion_matrix(gt, pred)
    accuracy    = accuracy_score(gt, pred)
    precision   = precision_score(gt, pred)
    recall      = recall_score(gt, pred)
    f1_score    = 2 * precision * recall / (precision+recall)
    print('Confusion Matrix')
    print(confusion)
    
    print('\n\nAccuracy : {:2.4}%'.format(accuracy))
    print('Precision: {:.4}'.format(precision))
    print('Recall   : {:.4}'.format(recall))
    print('F1 Score : {:.4}'.format(f1_score))
    return confusion, precision, recall, accuracy, f1_score