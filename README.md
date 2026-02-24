# Cocoha Project

This repository contains the code and instructions for working with the **Cocoha Dataset**, which is used for analyzing EEG responses to auditory stimuli using the **EElbrain toolkit**: [Eelbrain toolkit](https://elifesciences.org/articles/85012).

## Dataset Information

- **Dataset**: [Zenodo - Cocoha Dataset](https://zenodo.org/records/1199011)
- **Article**: [Describing the Dataset](https://www.sciencedirect.com/science/article/pii/S105381191730318X?via=ihub#s0010)

---

## Folder Structure

After downloading and preparing the dataset, your folder structure should look like this:

```
cocoha/
├── data_preprocessed/   # Preprocessed EEG data
├── stimuli/             # Audio stimuli
├── envelopes/           # Envelopes (generated in step 2)
├── eeg/                 # EEG data (generated in Step 3)
├── predictors/          # Predictor files (generated in Step 4)
├── TRFs/                # TRF estimates (generated in Step 5)
├── figures/             # Figures (generated in Step 6)
```

---

## Steps to Process the Data

### 1. **Download and Prepare the Dataset**

1. Download the **stimuli**: [AUDIO.zip](https://zenodo.org/record/1199011/files/AUDIO.zip)
2. Download the **preprocessed data**: [DATA_preproc.zip](https://zenodo.org/record/1199011/files/DATA_preproc.zip)
3. Extract the contents into the `data_preprocessed/` and `stimuli/` folders, respectively.

---

### 2. **Load the Preprocessed Data**

Run the notebook `load_data/load-preprocessed-envelopes.ipynb` to process the preprocessed data and generate attended and unattended envelopes.

```bash
# Example command to run the notebook
jupyter notebook load_data/load-preprocessed-envelopes.ipynb
```

This will:

- Load the `.mat` files from `data_preprocessed/`
- Generate attended and unattended envelopes
- Save the results in the `envelopes/` folder

---

### 3. **Generate EEG Data**

Run the notebook `import_dataset/save-eeg.ipynb` to generate EEG data files.

```bash
# Example command to run the notebook
jupyter notebook import_dataset/save-eeg.ipynb
```

This will:

- Process the EEG data
- Save the results in the `eeg/` folder

---

### 4. **Generate Predictor Files**

Run the notebook `predictors/make_gammatone_predictors.ipynb` to create the predictor files.

```bash
# Example command to run the notebook
jupyter notebook predictors/make_gammatone_predictors.ipynb
```

This will:

- Generate gammatone predictors for the stimuli
- Save the results in the `predictors/` folder

---

### 5. **Estimate TRFs**

Run the notebook `analysis/estimate_trfs.ipynb` to estimate Temporal Response Functions (TRFs).

```bash
# Example command to run the notebook
jupyter notebook analysis/estimate_trfs.ipynb
```

This step may take over an hour to complete, depending on your system.

---

### 6. **Visualize Results**

Run the notebook `figures/plot_results.ipynb` to generate and save figures.

```bash
# Example command to run the notebook
jupyter notebook figures/plot_results.ipynb
```

This will:

- Load the TRF estimates
- Generate visualizations
- Save the figures in the `figures/` folder

---

## Summary of Outputs

- **Envelopes**: `envelopes/`
- **EEG Data**: `eeg/`
- **Predictors**: `predictors/`
- **TRFs**: `TRFs/`
- **Figures**: `figures/`

---

## Notes

- Ensure all dependencies are installed before running the notebooks.
- The processing steps may take significant time depending on the size of the dataset and your system's performance.
