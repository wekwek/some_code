import os
import matplotlib.pyplot as plt 
import pandas as pd 

def file_list(dirpath):
	file_list=os.listdir(dirpath)
	num=len(file_list)
	file_path=[]
	file_name=[]
	for i in range(num):
		file_path.append(dirpath+file_list[i])
		file_name.append(file_list[i].split('.')[0])
	return file_path,file_name

def xrd_graph(file_path,file_name):
	num=len(file_name)
	if num%2==1:
		num=num+1
	else:
		pass
	fig=plt.figure()
	for i in range(num):
		columns=['2Theta','Intensity']
		data=pd.read_table(file_path[i],sep='\s+',skiprows=31,header=None,names=columns)
		ax=fig.add_subplot(2,int(num/2),i+1)
		ax.plot(data['2Theta'],data['Intensity'],'k')
		ax.set_title(file_name[i])
		ax.set_xlabel('2Theta')
		ax.set_ylabel('Intensity')
		plt.show()

def main():
	dirpath='E:/MOF-B/'
	file_path,file_name=file_list(dirpath)
	xrd_graph(file_path,file_name)

if __name__ == '__main__':
	main()

