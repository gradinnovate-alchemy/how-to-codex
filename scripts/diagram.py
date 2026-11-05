from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(13,4),facecolor='#f3f0e8')
ax.set(xlim=(0,13),ylim=(0,4));ax.axis('off')
labels=[('01','OBSERVE','Read context'),('02','PLAN','Define success'),('03','ACT','Use tools'),('04','VERIFY','Inspect evidence')]
for i,(n,title,sub) in enumerate(labels):
 x=.4+i*3.25
 ax.add_patch(FancyBboxPatch((x,1.1),2.45,1.8,boxstyle='round,pad=0.1,rounding_size=0.06',fc='#fffdf7',ec='#b7b3a9',lw=1))
 ax.text(x+.2,2.5,n,color='#c64e28',fontsize=14,family='monospace')
 ax.text(x+.2,2,title,color='#252722',fontsize=16,weight='bold')
 ax.text(x+.2,1.5,sub,color='#66675f',fontsize=12)
 if i<3:ax.annotate('',xy=(x+3.05,2),xytext=(x+2.6,2),arrowprops=dict(arrowstyle='->',color='#c64e28',lw=2))
ax.annotate('',xy=(1.6,.85),xytext=(11.3,.85),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.08',color='#c64e28',lw=1.5))
ax.text(6.5,.15,'REPEAT WITH OBSERVED EVIDENCE',ha='center',fontsize=11,color='#66675f',family='monospace')
fig.savefig(Path(__file__).resolve().parents[1]/'assets/agent-loop.png',dpi=220,bbox_inches='tight',facecolor=fig.get_facecolor())
