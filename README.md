Find the dataset: https://zenodo.org/records/1199011
Article describing the dataset: https://www.sciencedirect.com/science/article/pii/S105381191730318X?via=ihub#s0010


Steps:
1. Download the stimuli: AUDIO.zip
2. Download the preprocessed data: DATA_preproc.zip
3. Generate high-resolution gammatone spectrograms with: `predictors/make_gammatone.ipynb` (apprx. 20 min)
4. Generate predictor files with: `predictors/make_gammatone_predictors.ipynb` (approx 8 min)
5. Estimate TRFs with: `analysis/estimate_trfs.ipynb` (>1 hour :0)
