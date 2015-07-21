#BiMonBUPyCon - First meeting - 3/22/2015


selection = input('Input plot #: ')
print(type(selection))

#Basic plotting 

if selection == '1':
	#Example 1: Basic importing and plotting procedures
	#-------------------------------------------------------------------------------------
	import matplotlib
	import matplotlib.pyplot as plt

	x = range(6)
	plt.plot(x)
	plt.show()
	#-------------------------------------------------------------------------------------




if selection == '2':
	#Example 2: More advanced plot and interactive
	#-------------------------------------------------------------------------------------
	import matplotlib
	import matplotlib.pyplot as plt
	plt.ion()

	import numpy as np
	x = np.arange(9)

	plt.plot(x,x**2,color='r',linewidth=2,marker='o', linestyle=':',label='A')
	plt.plot(x,3.*x**3, c='b', lw=1.5, ls='--',label='B')
	plt.scatter(x,1500.*np.ones(9),c='k',s=100,edgecolor='#FF6600',lw=4,label='C')
	plt.legend(loc='best')
	
	plt.xlabel('Time', fontsize='x-large')
	plt.ylabel(r'$\beta \; $or$\epsilon$do$\bf{m}$', fontsize='large')
	plt.title('AS### Classes - Your choice', fontsize='medium')
	
	plt.xlim(0,10)
	plt.ylim(-100,2000)
	
	plt.text(2,1000,'Your Ad Here!',ha='left', va='center',fontsize='x-large')
	plt.show()
	plt.savefig('/Users/paul/Desktop/figure.png',dpi=300)
	#-------------------------------------------------------------------------------------






