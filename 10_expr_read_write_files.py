#%%
my_story = '''
This is my story
I want cycling

That is the end

'''

#%% the old way, should not use it like this
file = open("my_story.txt", "w")
file.write(my_story)
file.close()

#%% convention, how you should use it
with open("my_story.txt", "w") as file:
    file.write(my_story)
    
print("Proceed the code")

# %% read from a text file
with open("my_story.txt", "r") as file:
    content = file.read()
    
#%%
print(content)

# %%
with open("my_story.txt", "r") as file:
    content_list = file.readlines()
    
#%%
content_list
# %%
