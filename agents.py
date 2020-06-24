import pandas as pd

def select_agent(agents,selection_mode,issues):
    file = open(agents)
    df = pd.read_table(file)
    availability_mask = (df['Availability'] == 'Yes')
    updated_df = df[availability_mask]
    languages = ['Tamil','Telugu','Hindi','Gujarati','Malayalam','Kannada','Marati','Odissi','Punjabi','Bengali']
    for x in issues:
        if x in languages:
            mask = (df['Language'] == x)
            updated_df = updated_df[mask]
        mask1 = (df['Role'] == x)
        updated_df = updated_df[mask1]
        if selection_mode == 'all_available':
            print('Any agent from the following list will pick the issue if they want')
            name_list = updated_df['Name'].tolist()
            return name_list
        if selection_mode == 'random':
            a = updated_df.sample()
            a['Availability'] = 'No'
            a['Busy'] = int(a['Busy'])+1 
            return a['Name']
        if selection_mode == 'least busy':
            min_val = updated_df['Busy'].min()
            busy_mask = (updated_df['Busy'] == min_val)
            updated_df = updated_df[busy_mask]
            a = updated_df.sample()
            a['Availability'] = 'No'
            a['Busy'] = int(a['Busy'])+1
            return a['Name']
        
        



