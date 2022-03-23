import bar_chart_race as bcr
import pandas as pd
import sys
import traceback

try:
    print('run bar chart race for telemetry tagged spring chinook')
    #Get the CSV and load it into a Pandas frame.
    df0 = pd.read_csv('/home/gerry/Python/bar_chart_race/2019fish.csv')
    #These data are long, process them as wide...
    df_values, df_ranks = bcr.prepare_long_data(df0, index='date', columns='fish',values='MILE')
    
    
    df = df_values
    #Replace the NAN values with 0.
    df.fillna(0, inplace=True)
    
    thisfile ='/home/gerry/Python/bar_chart_race/2019ChinookTelemetryBCR.mp4'      
    
    bcr.bar_chart_race(
        df,
        filename=thisfile,
        orientation='h',
        sort='desc',
        n_bars=20,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=4,
        interpolate_period=False,
        label_bars=True,
        bar_size=0.9,
        #period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
        ##period_fmt='%B %d, %Y',
        #period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                          #'s': f'Swim Miles: {v.nlargest(6).sum():,.0f}',
                                          #'ha': 'right', 'size': 8, 'family': 'DejaVu Sans'},
        #perpendicular_bar_func='median',
        period_length=500,
        figsize=(10, 6),
        dpi=144,
        cmap='Set1',
        title='2019 Nooksack River Tagged Chinook Swim Distances',
        title_size=16,
        bar_label_size=12,
        tick_label_size=12,
        shared_fontdict={'family' : 'DejaVu Sans', 'color' : '.1'},
        #scale='linear',
        writer=None,
        fig=None,
        bar_kwargs={'alpha': .7},
        filter_column_colors=True)  

    print('finished without error.')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))