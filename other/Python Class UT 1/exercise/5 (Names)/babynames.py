"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.


Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
"""
import re
import pprint
a= open('baby1990.html', mode='r')
html_code= a.read()

name_rank_list=[]


#extract year
year_match= re.search(r'h3 align="center">Popularity in (\d{4})</h3>', html_code)
if year_match:
    year= year_match.group(1)
else:
    year= 'not found'
name_rank_list.append(year)

#extract rank, Bname, Gname
ranks_bnames_gnames= re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', html_code)
print(ranks_bnames_gnames)

name_to_rank_dict= {}
for rank,Bname, Gname in ranks_bnames_gnames:
    if Bname not in name_to_rank_dict.keys():
        name_to_rank_dict[Bname]= rank
    if Gname not in name_to_rank_dict.keys():
        name_to_rank_dict[Gname]= rank

#pprint
pprint.pprint(name_to_rank_dict)

#making list
for name in sorted(name_to_rank_dict.keys()):
    name_rank_list.append(name+ ' ' + name_to_rank_dict[name])
print(name_rank_list)



my_file= open('summery.txt', mode='w')
my_file.write('\n'.join(name_rank_list))
my_file.close()
    
