from matplotlib.toolkits.basemap import Basemap
from matplotlib import rcParams
import sys
import pylab as P


# read in data on lat/lon grid.
hgt  = P.array(P.load('500hgtdata.gz'),'d')
lons = P.array(P.load('500hgtlons.gz'),'d')
lats = P.array(P.load('500hgtlats.gz'),'d')
lons, lats = P.meshgrid(lons, lats)

# Example to show how to make multi-panel plots.

# 2-panel plot, oriented vertically, colorbar on bottom.

rcParams['figure.subplot.hspace'] = 0.4 # more height between subplots
rcParams['figure.subplot.wspace'] = 0.5 # more width between subplots
#rcParams['figure.subplot.left'] = 0.1   # move left edge of subplot over a bit

# panel 1
mnh = Basemap(lon_0=-105,boundinglat=20.,
             resolution='c',area_thresh=10000.,projection='nplaea')
xnh,ynh = mnh(lons,lats)
fig = P.figure()
ax = fig.add_subplot(211)
CS = mnh.contour(xnh,ynh,hgt,15,linewidths=0.5,colors='k')
CS = mnh.contourf(xnh,ynh,hgt,15,cmap=P.cm.Spectral)
# colorbar on bottom.
l,b,w,h = ax.get_position()
cax = P.axes([l, b-0.05, w, 0.025]) # setup colorbar axes
P.colorbar(tickfmt='%d', cax=cax, orientation='horizontal',clabels=CS.levels[0::4]) # draw colorbar
P.axes(ax)  # make the original axes current again
mnh.drawcoastlines(linewidth=0.5)
delat = 30.
circles = P.arange(0.,90.,delat).tolist()+\
          P.arange(-delat,-90,-delat).tolist()
mnh.drawparallels(circles,labels=[1,0,0,0])
delon = 60.
meridians = P.arange(0,360,delon)
mnh.drawmeridians(meridians,labels=[1,0,0,1])
P.title('NH 500 hPa Height (cm.Spectral)')

# panel 2
msh = Basemap(lon_0=-105,boundinglat=-20.,
             resolution='c',area_thresh=10000.,projection='splaea')
xsh,ysh = msh(lons,lats)
ax = fig.add_subplot(212)
CS = msh.contour(xsh,ysh,hgt,15,linewidths=0.5,colors='k')
CS = msh.contourf(xsh,ysh,hgt,15,cmap=P.cm.Spectral)
# colorbar on bottom.
ax.apply_aspect()
l,b,w,h = ax.get_position()
cax = P.axes([l, b-0.05, w, 0.025]) # setup colorbar axes
P.colorbar(tickfmt='%d', cax=cax,orientation='horizontal',clabels=CS.levels[0::4]) # draw colorbar
P.axes(ax)  # make the original axes current again
msh.drawcoastlines(linewidth=0.5)
msh.drawparallels(circles,labels=[1,0,0,0])
msh.drawmeridians(meridians,labels=[1,0,0,1])
P.title('SH 500 hPa Height (cm.Spectral)')
P.show()

# 2-panel plot, oriented horizontally, colorbar on right.

# panel 1
fig = P.figure()
ax = fig.add_subplot(121)
CS = mnh.contour(xnh,ynh,hgt,15,linewidths=0.5,colors='k')
CS = mnh.contourf(xnh,ynh,hgt,15,cmap=P.cm.RdBu)
# colorbar on right
l,b,w,h = ax.get_position()
cax = P.axes([l+w+0.025, b, 0.025, h]) # setup colorbar axes
P.colorbar(tickfmt='%d', cax=cax, clabels=CS.levels[0::2]) # draw colorbar
P.axes(ax)  # make the original axes current again
mnh.drawcoastlines(linewidth=0.5)
mnh.drawparallels(circles,labels=[1,0,0,0])
mnh.drawmeridians(meridians,labels=[1,0,0,1])
P.title('NH 500 hPa Height (cm.RdBu)')

# panel 2
ax = fig.add_subplot(122)
CS = msh.contour(xsh,ysh,hgt,15,linewidths=0.5,colors='k')
CS = msh.contourf(xsh,ysh,hgt,15,cmap=P.cm.RdBu)
# colorbar on right.
l,b,w,h = ax.get_position()
cax = P.axes([l+w+0.025, b, 0.025, h]) # setup colorbar axes
P.colorbar(tickfmt='%d', cax=cax, clabels=CS.levels[0::2]) # draw colorbar
P.axes(ax)  # make the original axes current again
msh.drawcoastlines(linewidth=0.5)
msh.drawparallels(circles,labels=[1,0,0,0])
msh.drawmeridians(meridians,labels=[1,0,0,1])
P.title('SH 500 hPa Height (cm.RdBu)')
P.show()