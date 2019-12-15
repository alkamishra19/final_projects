# HR data analysis using dataset from IBM, UCI, U.S. Census Reports and Bureau of Labor Statistics
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from astropy.table import Table
import warnings
warnings.simplefilter("ignore")


def read_dataframes():
    """
        In this function,  we are are reading the required csv files from the dataset into dataframes.
        :return: We return the Ibm_df, adult_df as dataframes after reading the csv files.

    """
    Ibm_df = pd.read_csv('IBM_HR_data.csv',
                         delimiter=',', encoding='UTF-8')
    ad_df = pd.read_csv('adult.csv',
                        delimiter=',', header=None, encoding='UTF-8')
    ad_df.columns = ['Age', 'JobType', 'EmpID',
                     'EducationLevel', 'Level', 'MaritalStatus',
                     'JobPosition', 'MaritalStatus_Desc', 'Race',
                     'Gender', 'Column_1', 'Column_2',
                     'Column_3', 'Location', 'ExpectedSalary']
    adult_df = ad_df[['Age', 'JobType', 'EducationLevel',
                      'Level', 'JobPosition', 'MaritalStatus',
                      'Location', 'Gender', 'ExpectedSalary']].sort_values(by='Age', ascending=True)

    return Ibm_df, adult_df


def filter_data(adult_df):
    """
    In this function, we are are choosing adult dataset based on Job type, location and age.
    :param adult_df: dataframe with adult dataset containing values for individuals based on age and education
    :return: We return the ad_df_private_US after filtering.

    >>> ad_df = pd.read_csv('adult.csv', delimiter=',', header=None, encoding='UTF-8')
    >>> ad_df.columns = ['Age', 'JobType', 'EmpID', 'EducationLevel', 'Level', 'MaritalStatus', 'JobPosition', 'MaritalStatus_Desc', 'Race', 'Gender', 'Column_1', 'Column_2', 'Column_3', 'Location', 'ExpectedSalary']
    >>> adult_df = ad_df[['Age', 'JobType', 'EducationLevel','Level', 'JobPosition', 'MaritalStatus','Location', 'Gender', 'ExpectedSalary']].sort_values(by='Age', ascending=True)
    >>> df = filter_data(adult_df)
    >>> df.shape
    (18889, 9)
    """
    adult_df['JobType'] = adult_df['JobType'].str.strip()
    adult_df['Location'] = adult_df['Location'].str.strip()
    adult_df['Gender'] = adult_df['Gender'].str.strip()
    adult_df['JobPosition'] = adult_df['JobPosition'].str.strip()
    adult_df['EducationLevel'] = adult_df['EducationLevel'].str.strip()
    adult_df['ExpectedSalary'] = adult_df['ExpectedSalary'].str.strip()
    ad_df_private = adult_df[adult_df['JobType'] == 'Private']
    ad_df_private_US = ad_df_private[ad_df_private['Location'] == 'United-States']
    ad_df_private_US = ad_df_private_US[ad_df_private_US['Age'] > 17]
    ad_df_private_US = ad_df_private_US[ad_df_private_US['Age'] <= 60]
    return ad_df_private_US


def club_similar_values(adult_df):
    """
        In this function, we are are replacing Job position values with common positions in adult dataset so that the job positions remain common accross csv's.
        :return: We return the ad_df_private_US after replacement.

        >>> ad_df = pd.read_csv('adult.csv', delimiter=',', header=None, encoding='UTF-8')
        >>> ad_df.columns = ['Age', 'JobType', 'EmpID', 'EducationLevel', 'Level', 'MaritalStatus', 'JobPosition', 'MaritalStatus_Desc', 'Race', 'Gender', 'Column_1', 'Column_2', 'Column_3', 'Location', 'ExpectedSalary']
        >>> adult_df = ad_df[['Age', 'JobType', 'EducationLevel','Level', 'JobPosition', 'MaritalStatus','Location', 'Gender', 'ExpectedSalary']].sort_values(by='Age', ascending=True)
        >>> sim_df = club_similar_values(adult_df)
        >>> sim_df.shape
        (32563, 11)
        >>> sim_df.shape != (32563, 13)
        True
    """
    adult_df.loc[adult_df.JobPosition == "Adm-clerical", 'Education Field'] = "Human Resources"
    adult_df.loc[adult_df.JobPosition == "Farming-fishing", 'Education Field'] = "Life Sciences"
    adult_df.loc[(adult_df.JobPosition == "Machine-op-inspct") | (
            adult_df.JobPosition == "Tech-support"), 'Education Field'] = "Technical Degree"
    adult_df.loc[
        (adult_df.JobPosition == "Other-service") | (adult_df.JobPosition == "Transport-moving") | (
                adult_df.JobPosition == "Handlers-cleaners"), 'Education Field'] = "Other"
    adult_df.loc[(adult_df.JobPosition == "Protective-serv") | (
            adult_df.JobPosition == "Prof-specialty"), 'Education Field'] = "Medical"
    adult_df.loc[adult_df.JobPosition == "Sales", 'Education Field'] = "Management"

    adult_df.loc[(adult_df.EducationLevel == "10th") | (adult_df.EducationLevel == "11th") | (
            adult_df.EducationLevel == "12th") | (adult_df.EducationLevel == "1st-4th") | (
                                 adult_df.EducationLevel == "5th-6th")
                         | (adult_df.EducationLevel == "7th-8th") | (
                                 adult_df.EducationLevel == "9th"), 'Education'] = 2
    adult_df.loc[
        (adult_df.EducationLevel == "Assoc-acdm") | (adult_df.EducationLevel == "Assoc-voc") | (
                adult_df.EducationLevel == "Some-college") | (
                adult_df.EducationLevel == "HS-grad"), 'Education'] = 2
    adult_df.loc[adult_df.EducationLevel == "Bachelors", 'Education'] = 3
    adult_df.loc[(adult_df.EducationLevel == "Masters") | (
            adult_df.EducationLevel == "Prof-school"), 'Education'] = 4
    adult_df.loc[adult_df.EducationLevel == "Doctorate", 'Education'] = 5

    return adult_df


def probable_expected_salary(ad_df_private_US):
    """
        In this function, we are finding probable expected salary values based on age group degree, education field and gender.
        For probable expected value between 0 to 50 : Expected Salary is less than or equal to 50k
        For probable expected value greater than 50 : Expected Salary is less greater than 50k
        :return: We return the ad_dataframe after finding probable expected value.

        >>> ad_df = pd.read_csv('adult.csv', delimiter=',', header=None, encoding='UTF-8')
        >>> ad_df.columns = ['Age', 'JobType', 'EmpID', 'EducationLevel', 'Level', 'MaritalStatus', 'JobPosition', 'MaritalStatus_Desc', 'Race', 'Gender', 'Column_1', 'Column_2', 'Column_3', 'Location', 'ExpectedSalary']
        >>> adult_df = ad_df[['Age', 'JobType', 'EducationLevel','Level', 'JobPosition', 'MaritalStatus','Location', 'Gender', 'ExpectedSalary']].sort_values(by='Age', ascending=True)
        >>> sim_df = club_similar_values(adult_df)
        >>> probable_expected_salary(sim_df)
        ValueError: cannot set a frame with no defined index and a scalar
    """
    ad_df_private_US = ad_df_private_US.dropna(subset=['Education Field'])
    ad_df_private_US.loc[ad_df_private_US.ExpectedSalary == "<=50K", 'Probable Salary Value'] = 0
    ad_df_private_US.loc[ad_df_private_US.ExpectedSalary == ">50K", 'Probable Salary Value'] = 100
    ad_dataframe = pd.DataFrame(
        ad_df_private_US.groupby(['Age', 'Education', 'Education Field', 'Gender'])['Probable Salary Value'].mean())
    return ad_dataframe


def merge_datasets(Ibm_df, ad_dataframe):
    """
        In this function, we are merging both the datasets based on Age, EducationField, Gender and Education.
        :return: We return the sorted_dataframe after merging.

        >>> df_1 = pd.read_csv('IBM_HR_data.csv', delimiter=',', encoding='UTF-8')
        >>> df_2 = pd.read_csv('adult.csv', delimiter=',', header=None, encoding='UTF-8')
        >>> df_2.columns = ['Age', 'JobType', 'EmpID', 'EducationLevel', 'Level', 'MaritalStatus','JobPosition', 'MaritalStatus_Desc', 'Race','Gender', 'Column_1', 'Column_2','Column_3', 'Location', 'ExpectedSalary']
        >>> ad_df_1 = df_2[['Age', 'JobType', 'EducationLevel', 'Level', 'JobPosition', 'MaritalStatus','Location', 'Gender', 'ExpectedSalary']].sort_values(by='Age', ascending=True)
        >>> ad_df_1.shape != (32563, 9)
        False
        >>> sim_df = club_similar_values(ad_df_1)
        >>> merged = merge_datasets(df_1, sim_df)
        >>> merged.shape
        (0, 43)
    """
    Ibm_df['EducationField'] = Ibm_df['EducationField'].str.strip()
    merged_dataframe = pd.merge(Ibm_df, ad_dataframe, how='inner',
                                left_on=['Age', 'EducationField', 'Gender', 'Education'],
                                right_on=['Age', 'Education Field', 'Gender', 'Education'])
    sorted_dataframe = merged_dataframe.sort_values(by='Age', ascending=True)
    return sorted_dataframe


def split_dataframe_for_analysis_1(merged_dataframe):
    """
        In this function, we are splitting the dataframe based on expected salary .
        :return: We return the sorted_dataframe after merging.
    """
    merged_dataframe['Salary Earned'] = merged_dataframe.MonthlyIncome * 12
    salary_split = merged_dataframe[merged_dataframe['Attrition'] == 'Yes']
    salary_split = merged_dataframe
    salary_less = salary_split[salary_split['Probable Salary Value'] <= 50.0]
    salary_greater = salary_split[salary_split['Probable Salary Value'] > 50.0]
    return salary_less, salary_greater


def salary_attrition_analysis1(salary_less):
    """
        In this function, we are splitting the dataframe based on expected salary .
        :return: We return the sorted_dataframe after merging.

    """
    salary_data_less_attr = salary_less

    count_yes = salary_data_less_attr.apply(lambda x: True if x['Attrition'] == 'Yes' else False, axis=1)

    salary_data_less_attr = salary_less[salary_less['Attrition'] == 'Yes']
    # Count number of True in series
    numOfRowsYes = len(count_yes[count_yes == True].index)
    # print(numOfRowsYes)

    salary_data_less_attr['Is salary greater than expected'] = salary_data_less_attr['Salary Earned'].apply(
        lambda x: 'True' if x > 50000 else 'False')
    total_count = pd.DataFrame({'Count':
                                    salary_data_less_attr.groupby(['Attrition', 'Is salary greater than expected'])[
                                        'Is salary greater than expected'].count()})
    total_count['Percentage'] = total_count['Count'] / numOfRowsYes * 100
    total_count.Percentage = total_count.Percentage.round(decimals=2)
    # print(total_count)

    return total_count


def salary_attrition_analysis2(salary_less):
    """
        In this function, we are splitting the dataframe based on expected salary .
        :return: We return the sorted_dataframe after merging.

    """
    salary_data_less_attr = salary_less

    count_yes = salary_data_less_attr.apply(lambda x: True if x['Attrition'] == 'Yes' else False, axis=1)

    salary_data_less_attr = salary_less[salary_less['Attrition'] == 'Yes']
    # Count number of True in series
    numOfRowsYes = len(count_yes[count_yes == True].index)
    # print(numOfRowsYes)

    salary_data_less_attr['Is salary less than expected'] = salary_data_less_attr['Salary Earned'].apply(
        lambda x: 'True' if x <= 50000 else 'False')
    total_count = pd.DataFrame({'Count':
                                    salary_data_less_attr.groupby(['Attrition', 'Is salary less than expected'])[
                                        'Is salary less than expected'].count()})
    total_count['Percentage'] = total_count['Count'] / numOfRowsYes * 100
    total_count.Percentage = total_count.Percentage.round(decimals=2)
    # np.round(total_count, decimals=2)
    # print(total_count)

    return total_count


def total_values_travel(travel_df, frequency):
    """

    :param travel_df: Dataframe containing values for IBM
    :param frequency: Travel frequency to be passed
    :return: count of values with attrition and total count

    >>> Ibm_df = pd.read_csv('IBM_HR_data.csv', delimiter=',', encoding='UTF-8')
    >>> freq = total_values_travel(Ibm_df, 'Travel_Frequently')
    >>> freq
    (277, 69, 208)
    >>> freq = total_values_travel(Ibm_df, 'None')
    >>> freq
    (0, 0, 0)
    """
    count_freq = 0
    count_attrition_y = 0
    count_attrition_n = 0
    for b_values in travel_df.index:
        if travel_df['BusinessTravel'][b_values] == frequency:
            count_freq += 1

    count_attrition_y = attrition_values(travel_df, frequency, 'Yes')
    count_attrition_n = attrition_values(travel_df, frequency, 'No')

    return count_freq, count_attrition_y, count_attrition_n


def attrition_values(df, freq, attr_value):
    """

    :param df: Merged df with IBM
    :param freq: Business travel frequency
    :param attr_value: Either 'Yes' or 'No'
    :return:

    >>> Ibm_df = pd.read_csv('IBM_HR_data.csv', delimiter=',', encoding='UTF-8')
    >>> freq = attrition_values(Ibm_df, 'Travel_Rarely', 'Yes')
    >>> freq
    156
    """
    freq_y = 0
    for b_values in df.index:
        if df['BusinessTravel'][b_values] == freq and df['Attrition'][b_values] == attr_value:
            freq_y += 1
    return freq_y


def create_table():
    """

    :return: table based on business travel frequency
    >>> data_row = [('A', 10), ('B', 20), ('C', 40)]
    >>> t2 = Table(rows=data_row, names=('Keys', 'Values'))
    >>> print(t2)
    Keys Values
    ---- ------
       A     10
       B     20
       C     40
    """
    t = Table()
    data_rows = [('Travel_Rarely',
                  total_values_travel(Ibm_df, 'Travel_Rarely')[0],
                  total_values_travel(Ibm_df, 'Travel_Rarely')[1],
                  total_values_travel(Ibm_df, 'Travel_Rarely')[2]),
                 ('Travel_Frequently',
                  total_values_travel(Ibm_df, 'Travel_Frequently')[0],
                  total_values_travel(Ibm_df, 'Travel_Frequently')[0],
                  total_values_travel(Ibm_df, 'Travel_Frequently')[0]),
                 ('Non-Travel',
                  total_values_travel(Ibm_df, 'Non-Travel')[0],
                  total_values_travel(Ibm_df, 'Non-Travel')[1],
                  total_values_travel(Ibm_df, 'Non-Travel')[2])
                 ]
    t1 = Table(rows=data_rows,
               names=('Travel_Status', 'Total Count', 'Attriiton_yes', 'Attriiton_no'))

    return t1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    Ibm_df, adult_df = read_dataframes()
    ad_df_private_US = filter_data(adult_df)
    ad_df_private_US = club_similar_values(ad_df_private_US)
    ad_dataframe = probable_expected_salary(ad_df_private_US)
    merged_dataframe = merge_datasets(Ibm_df, ad_dataframe)
    salary_less, salary_greater = split_dataframe_for_analysis_1(merged_dataframe)
    salary_data_less_attr = salary_attrition_analysis1(salary_less)
    salary_data_greater_attr = salary_attrition_analysis2(salary_greater)

    salary_data_less = merged_dataframe[merged_dataframe['Probable Salary Value'] < 50]
    salary_data_higher = merged_dataframe[merged_dataframe['Probable Salary Value'] >= 50]

    title = "Salary vs Attrition (Expected less than 50k)"

    title = "Salary vs Attrition (Expected more than 50k)"

    print("\n Attrition percentage of people with salary expectation less than or equal to 50k : \n")
    print(salary_data_less_attr)
    print("---------------------------------------------------------------------\n\n")
    print("\n Attrition percentage of people with salary expectation greater than 50k : \n")
    print(salary_data_greater_attr)
    print("---------------------------------------------------------------------\n\n")

    salary_data_less_attr = salary_data_less[salary_data_less['Attrition'] == 'Yes']
    salary_data_higher_attr = salary_data_higher[salary_data_higher['Attrition'] == 'Yes']

    title = "Salary vs Attrition (Expected less than 50k)"
    data_h1_b = salary_data_less_attr

    title = "Salary vs Attrition (Expected more than 50k)"
    data_h1_b = salary_data_higher_attr

    """
        Box plots for hypotheses 2.1 Age vs. Salary
    """
    ad_df_specific = adult_df[['Age', 'EducationLevel', 'ExpectedSalary']].sort_values(by='Age', ascending=True)
    x = "ExpectedSalary"
    y = "Age"
    title = "Age by individual's earnings ($ >50K or <= 50K) based on adult dataset"

    """
        Box plot for hypotheses 2.2 Education vs. Salary
    """
    x = "ExpectedSalary"
    y = "EducationLevel"
    title = "Salary Earned by Education Level after grouping adult data"

    """
        Box plot for hypotheses 2.3 Education vs. Salary
    """
    x = "Education"
    y = "Salary Earned"
    title = "Salary Earned by Education Level after grouping IBM HR data"

    """
        Box plot for hypotheses 2.4 Age vs. Salary
    """
    x = "Age"
    y = "Salary Earned"
    title = "Salary Earned by Age after grouping IBM HR data"

    education_attr = merged_dataframe[['Education', 'Attrition']]
    education_attr_y = education_attr[education_attr['Attrition'] == 'Yes'].groupby(by='Education').count()

    """
        Pie chart demonstrating distribution of IBM employees as per Education Level
    """
    labels = ['Upto 11th', 'Bachelors', 'Masters', 'Doctorate']
    values = merged_dataframe.groupby(by='Education')['Education'].count()

    fig_17 = go.Figure(
        data=[go.Pie(labels=labels, values=values, title="Distribution of IBM employees by Education Level")])
    # fig_17.show()

    # calculating percentages when attrition has happened in each category
    # for travel rarely
    perc1 = round(
        (total_values_travel(Ibm_df, 'Travel_Rarely')[1] / total_values_travel(Ibm_df, 'Travel_Rarely')[0]) * 100, 2)
    # for travel frequently
    perc2 = round((total_values_travel(Ibm_df, 'Travel_Frequently')[1] /
                   total_values_travel(Ibm_df, 'Travel_Frequently')[0]) * 100, 2)
    # for non-travel
    perc3 = round((total_values_travel(Ibm_df, 'Non-Travel')[1] / total_values_travel(Ibm_df, 'Non-Travel')[0]) * 100,
                  2)
    print('Percentage of attrition for people who rarely travelled ', perc1, "%")
    print('Percentage of attrition for people who frequently travelled ', perc2, "%")
    print('Percentage of attrition for people who did not travel', perc3, "%")

    Travel = ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']
    fig_5 = go.Figure([go.Bar(x=Travel, y=[perc1, perc2, perc3])])
    # fig_5.show()

    Travel = ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']

    fig_6 = go.Figure(data=[
        go.Bar(name='Attrition_Yes', x=Travel, y=[total_values_travel(Ibm_df, 'Travel_Rarely')[1],
                                                  total_values_travel(Ibm_df, 'Travel_Frequently')[1],
                                                  total_values_travel(Ibm_df, 'Non-Travel')[1]]),
        go.Bar(name='Attrition_No', x=Travel, y=[total_values_travel(Ibm_df, 'Travel_Rarely')[2],
                                                 total_values_travel(Ibm_df, 'Travel_Frequently')[2],
                                                 total_values_travel(Ibm_df, 'Non-Travel')[2]])])
    # Change the bar mode
    fig_6.update_layout(barmode='group')
    # fig_6.show()

    Age_Travel = Ibm_df[Ibm_df['BusinessTravel'] == 'Travel_Frequently']
    Age_df = Age_Travel[Age_Travel['Attrition'] == 'Yes']
    age_list = []
    df_age_count = pd.DataFrame({'Count': Age_df.groupby(by='Department')['Department'].count()})
    dept1 = 0
    dept2 = 0
    dept3 = 0
    for ages in Age_df['Department']:
        if ages == 'Human Resources':
            dept1 += 1
        elif ages == 'Research & Development':
            dept2 += 1
        elif ages == 'Sales':
            dept3 += 1

    total_values = total_values_travel(Ibm_df, 'Travel_Rarely')[0] + total_values_travel(Ibm_df, 'Travel_Frequently')[
        0] + total_values_travel(Ibm_df, 'Non-Travel')[0]
    count_travel_rarely = total_values_travel(Ibm_df, 'Travel_Rarely')[0]
    count_travel_frequently = total_values_travel(Ibm_df, 'Travel_Frequently')[0]
    count_non_travel = total_values_travel(Ibm_df, 'Non-Travel')[0]

    fig_7 = go.Figure(go.Sunburst(
        labels=["Business Travel", "Rarely travel", "Frequently Travel", "No Travel", "Human Resource",
                "Research and Development", "Sales"],
        parents=["", "Business Travel", "Business Travel", "Business Travel", "Frequently Travel", "Frequently Travel",
                 "Frequently Travel"],
        values=[total_values, count_travel_rarely, count_travel_frequently, count_non_travel, dept1, dept2, dept3],
    ))
    # Update layout for tight margin
    # See https://plot.ly/python/creating-and-updating-figures/
    fig_7.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    # fig_7.show()

    data_row = [('A', 10), ('B', 20), ('C', 40)]
    t2 = Table(rows=data_row, names=('Keys', 'Values'))
    print(t2)
