## Creating a Cricket Batsmen database along with visualisation
def batsman():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("This tool will help you create a table for batsmen along with calculating their averages and then preparing a bar chart")
    print("\n")
    n= int(input("Enter the number of batsmen:"))
    bat = {}
    print("\n")
    for i in range(n):
        name = input(f"Enter the name of the batsman {i+1}:")
        matches = int(input(f"Enter the number of matches played by {name}:"))
        print("\n")
        scores = {}
        total = 0
        out = 0
        for j in range(matches):
            runs = int(input(f"Enter the runs scored by {name} in match {j+1}:"))
            scores[f"Match {j+1}"] = runs
            outs = int(input(f"Enter '1' if {name} got out in the match, else enter '0':"))
            total = total+runs
            out = out+outs
            print("\n")
        if out == 0:
            average = "infinity"
        else:
            average = total/out
        scores['Total Runs']=total
        scores['Outs']=out
        scores['Average'] = average
        print("\n")
        print(f"The average of the {name} is {average}")
        bat[name]=scores

    print("\n")
    print(bat)

    df = pd.DataFrame(bat)
    print("\n")
    print(df)
    print("\n")
    print("Now a bar graph shall be created for a batsman of your choice")
    df_edit = df.drop(['Total Runs', 'Outs'])
    number = int(input("Enter the column number of your preferred batsman from the table"))
    try:
        sns.barplot(data=df_edit, x=df_edit.index, y=df_edit.columns[number-1])
        batsman_name = df_edit.columns[number-1]
        plt.title(f"{batsman_name}'s Statistics ")
    except:
        df_edit2 = df_edit.drop("Average")
        sns.barplot(data=df_edit2, x=df_edit2.index, y=df_edit2.columns[number-1])
        print("\n")
        print("The average is infinity, hence it cannot be plotted")

    print("\n")
    print("Your data is also exported as a CSV file")
    df.to_csv("bat.csv")

batsman()
