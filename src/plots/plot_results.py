import pandas as pd
import plotly.express as px

full_df = pd.read_json('data/final_data/doi_with_count.json', orient="index").convert_dtypes()
full_df['dois']=full_df['dois'].apply(lambda x: len(x))

open_cit_df = pd.read_json('data/final_data/open_cit_in_years.json')

#General information about number of citations and references. The open_cited and open_citing numbers are the same, as expected, since our study is about citations inside the same dataset
print(full_df[['cited', 'citing', 'open_cited', 'open_citing']].sum(axis=0))


#General plots for the 30 most citing, cited, open citing and open cited journals
df_sorted_by_citing = full_df.sort_values('citing', ascending=False).reset_index()
plot_sorted_by_citing = px.bar(df_sorted_by_citing.iloc[:30,:], x='title', y='citing',
             hover_data=['citing'], color='title',
             labels={'journals citations'}, height=1200, width=1200)
plot_sorted_by_citing.show()

df_sorted_by_citing.head(30).to_csv('most_citing.csv')

df_sorted_by_open_citing = full_df.sort_values('open_citing', ascending=False).reset_index()
plot_sorted_by_open_citing = px.bar(df_sorted_by_open_citing.iloc[:30,:], x='title', y='open_citing',
             hover_data=['open_citing'], color='title',
             labels={'journals open_citations'}, height=1200, width=1200)
plot_sorted_by_open_citing.show()

df_sorted_by_cited = full_df.sort_values('cited', ascending=False).reset_index()
plot_sorted_by_cited = px.bar(df_sorted_by_cited.iloc[:30,:], x='title', y='cited',
             hover_data=['cited'], color='title',
             labels={'journals references'}, height=1200, width=1200)
plot_sorted_by_cited.show()

df_sorted_by_cited.head(30).to_csv('most_cited.csv')

df_sorted_by_open_cited = full_df.sort_values('open_cited', ascending=False).reset_index()
plot_sorted_by_open_cited = px.bar(df_sorted_by_open_cited.iloc[:30,:], x='title', y='open_cited',
             hover_data=['open_cited'], color='title',
             labels={'journals open_references'}, height=1200, width=1200)
plot_sorted_by_open_cited.show()


#Same plots but with the addition of the information about the number of articles indexed
sorted_by_citing_with_num_dois = px.scatter(df_sorted_by_citing.iloc[:20,:], x="title", y="citing",
	         size="dois", color="title",
                 hover_name="title", width=1200, height=1000, size_max=60)
sorted_by_citing_with_num_dois.show()

sorted_by_cited_with_num_dois = px.scatter(df_sorted_by_cited.iloc[:20,:], x="title", y="cited",
	         size="dois", color="title",
                 hover_name="title", width=1200, height=1000, size_max=60)
sorted_by_cited_with_num_dois.show()

sorted_by_open_citing_with_num_dois = px.scatter(df_sorted_by_open_citing.iloc[:20,:], x="title", y="open_citing",
	         size="dois", color="title",
                 hover_name="title", width=1200, height=1000, size_max=60)
sorted_by_open_citing_with_num_dois.show()

sorted_by_open_cited_with_num_dois = px.scatter(df_sorted_by_open_cited.iloc[:20,:], x="title", y="open_cited",
	         size="dois", color="title",
                 hover_name="title", width=1200, height=1000, size_max=60)
sorted_by_open_cited_with_num_dois.show()


# plotting the timeline of citations going and coming to open journals
open_cit_fig = px.bar(open_cit_df, x='year', y='citation_count',
                      color='citation_count',
                      height=600,
                      title='Timeline of open citations of DOAJ journals')
open_cit_fig.update_xaxes(rangeslider_visible=True)
open_cit_fig.show()

# plotting the timeline of citations going and coming to open journals in the last 20 years
open_cit_20_fig = px.bar(open_cit_df.tail(20), x='year', y='citation_count',
             hover_data=['citation_count'],
             title='Timeline of open citations of DOAJ journals in the last 20 years',
             color='citation_count',
             height=600)
open_cit_20_fig.show()
