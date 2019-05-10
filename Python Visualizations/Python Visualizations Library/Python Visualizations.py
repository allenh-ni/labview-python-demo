import matplotlib.pyplot as plt
import numpy as np

def create_boxplot(datasets, target_image_filepath, dataset_labels, title, xaxis_label, yaxis_label): # (multiplot_data, plot_title, image_filepath):
    plt.boxplot(datasets.transpose(), labels=dataset_labels) # Transposing 2D array to better fit expected 2D array format from LabVIEW.
    plt.title(title)
    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.savefig(target_image_filepath.replace('\\','/')) # replace all instances of '\' with '/'
    # plt.show()
    plt.close()
	
	
def create_violinplot(datasets, target_image_filepath, dataset_labels, title, xaxis_label, yaxis_label): # (multiplot_data, plot_title, image_filepath):
    plt.violinplot(datasets.transpose(),
                   showmeans=False,
                   showmedians=True)
    ind = np.arange(1, len(dataset_labels)+1)   # the x locations for the groups
    plt.xticks(ind, dataset_labels)
    plt.title(title)
    plt.xlabel(xaxis_label)
    plt.ylabel(yaxis_label)
    plt.savefig(target_image_filepath.replace('\\','/')) # replace all instances of '\' with '/'
    # plt.show()
    plt.close()
	
def create_donutplot (data, target_image_filepath, labels, title, colors):
    # Labels is a string list.  Data is a numeric list. Title is string. Colors is a string list of colors.
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, colors=colors)
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})

    ax.set_title(title)
    ax.legend(labels)
    plt.savefig(target_image_filepath.replace('\\','/')) # replace all instances of '\' with '/'
    # plt.show()
    plt.close()
	
def create_testresults_stackedbargraph (pass_data, fail_data, error_data, target_image_filepath, labels, title):
    ind = np.arange(len(pass_data))   # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    plt.bar(ind, error_data, width, color='darkgrey')
    plt.bar(ind, fail_data, width, bottom=error_data, color='lightcoral')
    plt.bar(ind, pass_data, width, bottom=fail_data, color='mediumseagreen')
    # You can find a list of colors here: https://python-graph-gallery.com/python-colors/

    plt.ylabel('Number of Tests')
    plt.xticks(ind, labels)
    plt.title(title)
    plt.legend(['Error', 'Fail', 'Pass'])
    plt.savefig(target_image_filepath.replace('\\','/')) # replace all instances of '\' with '/'
    # plt.show()
    plt.close()