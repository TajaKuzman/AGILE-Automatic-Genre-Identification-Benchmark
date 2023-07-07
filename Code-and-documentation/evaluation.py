import pandas as pd
import numpy as np
import json
import logging
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, f1_score,precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
import ast
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#Calculate the scores for each model
def testing(true, pred, labels):
    """
    This function takes the list of true labels and list of predictions and evaluates the model based on comparing them.
    It calculates accuracy, micro and macro F1 and provides a classification report.
    It also prints a confusion matrix.
    
    Args:
    - y_true: list of true labels
    - y_pred: list of predicted labels

    The function returns a dictionary with accuracy, micro and macro F1.
    """
    y_true = true
    y_pred = pred
    LABELS = labels

    # Calculate the scores
    macro = f1_score(y_true, y_pred, labels=LABELS, average="macro")
    micro = f1_score(y_true, y_pred, labels=LABELS,  average="micro")
    print(f"Macro f1: {macro:0.3}, Micro f1: {micro:0.3}")
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {accuracy:0.3}")

    # Plot the confusion matrix:
    cm = confusion_matrix(y_true, y_pred, labels=LABELS)
    plt.figure(figsize=(6, 6))
    plt.imshow(cm, cmap="Oranges")
    for (i, j), z in np.ndenumerate(cm):
        plt.text(j, i, '{:d}'.format(z), ha='center', va='center')
    classNames = LABELS
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=90)
    plt.yticks(tick_marks, classNames)

    plt.tight_layout()
    fig1 = plt.gcf()
    plt.show()
    plt.draw()

    try:
        print(classification_report(y_true, y_pred, target_names=LABELS))
    except:
        print("Error when calculating classification report")
    
    return {"accuracy": accuracy, "micro F1":micro, "macro F1": macro}