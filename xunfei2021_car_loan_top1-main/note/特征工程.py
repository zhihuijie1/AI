import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import VarianceThreshold

# 示例数据
data = {
    'age': [25, 32, 28, 40, 29, 42, 19, 30],
    'salary': [50000, 64000, 58000, 52000, 72000, 80000, 42000, 62000],
    'city': ['New York', 'Los Angeles', 'New York', 'San Francisco', 'San Francisco', 'Los Angeles', 'New York', 'Los Angeles'],
    'gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male']
}
# 将字典转换为pandas DataFrame。DataFrame是pandas库中用于数据分析和操作的主要数据结构。
df = pd.DataFrame(data)

# 特征工程
# 1. 特征编码：将分类特征转换为数值特征
'''进行特征编码的原因是：将非数值类型转化成数值类型，这样便于机器学习算法来处理数据'''
categorical_features = ['city', 'gender'] # categorical_features: 指定了需要进行编码的类别型特征
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 2. 特征标准化：标准化数值特征
'''进行特征标准化的原因：不同数据集之间的数值相差可能比较大，这会对一些模型的决策产生影响，所以采用特征标准化的方式将数据放到同一个维度'''
numeric_features = ['age', 'salary']
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# 3. 组合特征处理步骤
'''数据集类型分为数值型，类别型，要对数值型进行标准化，对类别型进行编码，所以要采用不同的转换器（工具区）
ColumnTransformer可以为不同类型的类型进行指定的转化，最后，ColumnTransformer会将所有这些处理好的特征合并起来，形成一个统一的特征矩阵，
这个矩阵就可以直接用于训练机器学习模型。'''
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 4. 应用特征工程
'''preprocessor :食品加工器  df： DataFrame类型，是待处理的原始数据集。
先fit再transform -> 先学习后处理'''
X = preprocessor.fit_transform(df)
print(X)
