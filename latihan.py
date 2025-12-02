import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata Rata", data['Nilai'].mean())
print("Mediain:" , data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("Standar Deviasi:", data['Nilai'].std())
print("Variansi:", data['Nilai'].var())

print("Nilai Tertinggi:", data['Nilai'].max())
print("Nilai Terendah:", data['Nilai'].min())
print("Jumlah Data:", data['Nilai'].count())
print("Range:", data['Nilai'].max() - data['Nilai'].min())
print("Kuartil 1:", data['Nilai'].quantile(0.25))
print("Kuartil 3:", data['Nilai'].quantile(0.75))
print("Interquartile Range (IQR):", data['Nilai'].quantile(0.75) - data['Nilai'].quantile(0.25))

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Matpel')
plt.show()