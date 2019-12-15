# IS 590PR Final Project - Type 2
### Type 2 project for IBM HR data.

### Team members:
> Alka Mishra (alkamishra19),
> Kunal Pachori (kunalpachori),
> Urvashi Rawat (Urvashi0903)

The details for the project are as below: 

### Hypothesis 1 :
If the salary of the employee is less than expected, it leads to attrition

We have two datasets where in we would merge them based on the age and the education level. One of the datasets has the actual income and the other has a generic expected income.

#### Analysis Results:
##### Entire data with attrition 'Yes' and 'No'
![Salary vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_1.png)
![Salary vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_1b.png)
##### Records with attrition 'Yes' and 'No' individually based on salary either greater than or less than $50k
![Salary vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_1aa.png)
![Salary vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_1bb.png)
##### Percentage of attrition 
![Salary vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Count.png)

### Hypothesis 2 : 
Relationship between income and age is stronger than that between income and education.

Box plots representing data from the adult dataset as per age vs income and education vs income
![Education vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_2_1.png)
![Education vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_2_2.png)
IBM distribution of employees based on education levels:
![Education vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_2_3.png)
Box plots for IBM data with education level and age vs income
![Education vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_2_4.png)
![Education vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_2_5.png)

### Hypothesis 3 : 
Do factors such as business travel , department have any effect on the decision of an employee leaving the organization.

Heatmap for all the factors:
![Factors vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis_3.png)

We analyzed the dataset and learnt that there are three types of business travel : 
a) Frequently travel 
b) Rarely travel
c) No travel

![Business Travel vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis%203.4.png)

Thorough analysis helped us to idnetify that people who travel frequently leave the organization. 

Analysis Graphs : 
1. The travel category and attrition : 
![Business Travel vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis3.1.png)

2. The percentage of people with different travel category : 
![Business Travel vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis3.2.png)

3. The corelation between department and travel category that leads to attrition : 
![Business Travel vs Attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis%203.3%20.png)

### Hypothesis 4: 
To analyze if the ‘distance from home’ a factor that leads to attrition. 

1. When the distance from home is less than 25 
![Distance from home < 25](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis%204.1.png)

2. When the distance from home is more than 25 
![Distance from home > 25](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis%204.2.png)

3. Comparing the two to understand the percentage of people who stay and leave an organization
![Distance from home and attrition](https://github.com/kunalpachori/final_projects/blob/master/Analysis/Analysis%204.3%20.png) 

### Dataset links:

https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset - IBM Dataset
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data - Income dataset
https://www.kaggle.com/jonavery/incomes-by-career-and-gender - Incomes by position and gender from Bureau of Labor Statistics (BLS)
https://www.kaggle.com/goldenoakresearch/us-acs-mortgage-equity-loans-rent-statistics - Rent/Marital status/Mean salary/Expenses etc.

### Citation:
https://rpubs.com/asriram/278252

### Presentation link 
https://drive.google.com/drive/folders/1SHsTVTkGNT8j1SX1q63ATiSeZpLsn_A0?usp=sharing

