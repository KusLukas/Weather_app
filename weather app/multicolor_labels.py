def multicolor_ylabel(ax,list_of_strings,list_of_colors,axis='x',anchorpad=0,**kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

    # x-axis label
    if axis=='x' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',**kw))
                    for text,color in zip(list_of_strings,list_of_colors) ]
        xbox = HPacker(children=boxes,align="center",pad=0, sep=5)
        anchored_xbox1 = AnchoredOffsetbox(loc=3, child=xbox, pad=anchorpad,frameon=False,bbox_to_anchor=(-0.05, 0.2),
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_xbox1)

    # y-axis label
    if axis=='y' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw))
                     for text,color in zip(list_of_strings[::-1],list_of_colors[::-1]) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=5)
        anchored_ybox2 = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(-0.05, 0.2),
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox2)

def multicolor_ylabel_double_ax(ax,ax2,list_of_strings,list_of_colors,list_of_strings2,list_of_colors2,axis='x',anchorpad=0,**kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

    # x-axis label
    if axis=='x' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',**kw))
                    for text,color in zip(list_of_strings,list_of_colors) ]
        xbox = HPacker(children=boxes,align="center",pad=0, sep=5)
        anchored_xbox1 = AnchoredOffsetbox(loc=3, child=xbox, pad=anchorpad,frameon=False,bbox_to_anchor=(-0.05, 0.2),
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_xbox1)

    # y-axis label
    if axis=='y' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw))
                     for text,color in zip(list_of_strings[::-1],list_of_colors[::-1]) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=5)
        anchored_ybox2 = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(-0.05, 0.2),
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox2)

        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw))
                     for text,color in zip(list_of_strings2[::-1],list_of_colors2[::-1]) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=5)
        anchored_ybox2 = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(1.05, 0.2),
                                          bbox_transform=ax2.transAxes, borderpad=0.)
        ax2.add_artist(anchored_ybox2)

# ax = plt.subplot(111)
#
# x = np.linspace(0,10,1000)
# y1 = np.sin(x)
# y2 = np.sin(2*x)
#
# ax.plot(x,y1,color='r')
# ax.plot(x,y2,color='b')
#
# multicolor_ylabel(ax,('Line1','and','Line2','with','extra','colors!'),('r','k','b','k','m','g'),axis='both',size=15,weight='bold')
