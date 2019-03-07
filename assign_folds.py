
import numpy as np 
import pandas as pd 
from sklearn.model_selection import KFold, StratifiedKFold

# --------------------------------------------------------
# shuffles and assigns validation fold to each example, saves and returns cv key
# generate folds before modeling to maintain identicle folds across models and while ensembling/blending/stacking
# critical to safe and effective ensembling and evaluation
# NOTE: 'shuffle' in skl KFold method randomizes order of iteration, NOT fold assignment
# --------------------------------------------------------
def assign_folds(df, id_col, target_col, seed, k, stratify=False, new_index=False, save=False): # option to class-balance folds
	df = df[[id_col,target_col]] # drop unnecessary cols
	
	# randomize fold assignment
	df = df.sample(frac=1, random_state=seed)
	df = df.reset_index(drop=True)
	
	# create empty validation fold id column
	df['VAL_FOLD'] = np.nan # indicates when oof
	
	# use sklearn method (allows for easy option to stratify)
	if stratify: kf = StratifiedKFold(n_splits=k, shuffle=False) 
	else: kf = KFold(n_splits=k, shuffle=False)
	
	for i, (tidx, vidx) in enumerate(kf.split(df[id_col],df[target_col])):
		df.loc[vidx,'VAL_FOLD'] = i # set fold id

	# reset to original order
	df = df.sort_values(by=id_col)
	df = df.reset_index(drop=True)

	# save key
	if save: df.to_csv('cv_key.csv')

	return df 
