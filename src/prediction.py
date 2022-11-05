import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import style
from data import df


def get_coefficients(cols_to_keep, predict):
    """Apply linear regression to find coeffients
    
    Keyword arguments:
    cols_to_keep -- array of strings responding to names of cols to keep ex: ['Assignment 1 Current Score', 'Assignment 2 Current Score']
    predict -- string corresponding to the name of the column to predict
    Return: array of coefficients corresponding to each column in addition to the intercept
    """
    cols_keep = df.loc[:,cols_to_keep]
    x = np.array(cols_keep)
    y = np.array(df[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    print("Accuracy of model:", linear.score(x_test, y_test))
    return [*linear.coef_, linear.intercept_]

def predict_output(input, coefficients):
    """ multiply the input by the corresponding coefficient to predict the output
    
    Keyword arguments:
    input -- array of numbers
    coefficients -- array of floats, size must be size of input + 1
    Return: number predicted
    """
    sum = 0
    for index, value in enumerate(input):
        sum += value * coefficients[index]
    
    sum += coefficients[-1]
    return sum

def get_row_by_student(student):
    return df.loc[df['Student'] == student]

def retrieve_column_value(row, col_name):
    return row[col_name].values[0]

if __name__ == '__main__':
    predict = "Current Score"
    # cols_keep = ['Student', 'last_activity_at', 'total_activity_time',
    #    'Assignment 1 (c81f04547a95da2a7b88054ef491b7c4)',
    #    'Assignment 2 (a4dc11e7e79361fc5886a9078aac66b8)',
    #    'Assignment 3 (option A) (811d93ea379b5cdd5a19f1b5dbab88cd)',
    #    'Assignment 3 (option B) (df8d1f1ff3f48fdc24a278b40c5f45cc)',
    #    'Assignment 3 (option C) (bb971b36c1578cede00150acda89aa99)',
    #    'Assignment 3 (option D) (f1ad954cd2cddda6e17f6fc225d1aa3e)',
    #    'Participation grade: Formative (not included in final grade) (5965e0b0c712861d0efdd9be54572114)',
    #    'Assignment 1 Current Score', 'Assignment 2 Current Score',
    #    'Assignment 3 Current Score',
    #    'Participation & engagement Current Score', 'Current Score',
    #    'nav_count', 'disc_count', 'avg_post_message_length', 'total_likes']
    
    # cols_keep = ['Assignment 1 Current Score', 'Assignment 2 Current Score', 'Assignment 3 Current Score', 'Participation & engagement Current Score']

    cols_keep = ['nav_count'] # Just change this, add or remove columns
    
    coefficients = get_coefficients(cols_keep, predict)
    print(coefficients)

    predictions = []
    acutal_grades = []
    for student in df["Student"].values:
        row = get_row_by_student(student)
        parsed_row = row[cols_keep]
        list_row = parsed_row.values.flatten().tolist()
        grade = retrieve_column_value(row, "Current Score")
        prediction = predict_output(list_row, coefficients)
        predictions.append(prediction)
        acutal_grades.append(grade)
        print("PREDICTED VS ACTUAL FOR " + student + ":", predict, grade)
    
    plt.scatter(predictions, acutal_grades)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()